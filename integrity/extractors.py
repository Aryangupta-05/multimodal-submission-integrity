"""Real parsers and ASR. No manifest or intended transcript is read here."""

from collections import Counter
from hashlib import sha256, file_digest
from pathlib import Path
import re
import subprocess
import tempfile
import wave

import fitz
from docx import Document as Docx
import numpy as np

from .types import Document, Unit


def ffmpeg_executable():
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


class Extractor:
    def __init__(self, config):
        self.config = config
        self.asr = None

    def extract(self, path: Path, document_id=None):
        doc = Document(document_id or path.name, path.suffix.lower().lstrip("."))
        try:
            if path.stat().st_size == 0:
                doc.sha256 = sha256(b"").hexdigest()
                doc.status = "empty"
                doc.warnings.append("Zero-byte file: unable to assess.")
                return doc
            if path.stat().st_size > self.config["max_file_mb"] * 1024**2:
                doc.status = "limit_exceeded"
                doc.warnings.append("File exceeds configured size limit: unable to assess.")
                return doc
            with path.open("rb") as handle:
                doc.sha256 = file_digest(handle, "sha256").hexdigest()
            if doc.kind == "pdf":
                self._pdf(path, doc)
            elif doc.kind == "docx":
                self._docx(path, doc)
            elif doc.kind == "mp4":
                self._video(path, doc)
            else:
                doc.status = "unsupported"
                doc.warnings.append(f"Unsupported format .{doc.kind}: unable to assess.")
            if doc.status == "ok" and not any(u.text.strip() for u in doc.units):
                doc.status = "unextractable"
                doc.warnings.append("No extractable text. Scanned PDFs need OCR (not implemented).")
        except Exception as exc:
            doc.status = "error"
            doc.units.clear()
            doc.warnings.append(f"{type(exc).__name__}: {exc}. Unable to assess this file.")
        return doc

    def _pdf(self, path, doc):
        with fitz.open(path) as pdf:
            if pdf.needs_pass:
                raise ValueError("Password-protected PDF")
            if len(pdf) > self.config["max_pdf_pages"]:
                raise ValueError("PDF page limit exceeded")
            pages = []
            margins = Counter()
            for page in pdf:
                lines = []
                for block in page.get_text("dict", sort=True)["blocks"]:
                    for line in block.get("lines", []):
                        txt = "".join(s["text"] for s in line["spans"])
                        y0, y1 = line["bbox"][1], line["bbox"][3]
                        margin = y0 < page.rect.height * 0.08 or y1 > page.rect.height * 0.92
                        key = re.sub(r"\d+", "#", txt.strip().casefold())
                        lines.append((txt, margin, key))
                margins.update({key for _, margin, key in lines if margin and key})
                pages.append(lines)
            repeated = {
                k for k, n in margins.items() if len(pdf) >= 2 and n >= max(2, len(pdf) * 0.6)
            }
            removed = []
            empty_pages = []
            for i, lines in enumerate(pages, 1):
                kept = []
                for txt, margin, key in lines:
                    configured = any(
                        re.fullmatch(pattern, txt.strip(), re.I)
                        for pattern in self.config.get("ignored_margin_patterns", [])
                    )
                    page_label = bool(
                        re.fullmatch(r"(?:page\s+)?\d+(?:\s+(?:of|/)\s+\d+)?", txt.strip(), re.I)
                    )
                    if margin and (key in repeated or configured or page_label):
                        reason = (
                            "configured_margin"
                            if configured
                            else "page_number_label"
                            if page_label
                            else "repeated_margin"
                        )
                        removed.append({"page": i, "text": txt, "reason": reason})
                    else:
                        kept.append(txt)
                text = "\n".join(kept)
                if not text.strip():
                    empty_pages.append(i)
                doc.units.append(Unit(text, {"page": i}))
            doc.metadata.update(page_count=len(pdf), removed_margins=removed)
            if empty_pages:
                doc.warnings.append(
                    f"Pages {empty_pages} have no extractable text; OCR not implemented."
                )
                doc.metadata["unextractable_pages"] = empty_pages
                if len(empty_pages) < len(pdf):
                    doc.status = "partial"

    def _docx(self, path, doc):
        source = Docx(path)
        section = "Document body"
        paragraph = 0
        # iter_inner_content retains interleaved body paragraphs and tables.
        for element in source.iter_inner_content():
            if hasattr(element, "rows"):
                for row_no, row in enumerate(element.rows, 1):
                    for col_no, cell in enumerate(row.cells, 1):
                        for p in cell.paragraphs:
                            paragraph += 1
                            doc.units.append(
                                Unit(
                                    p.text,
                                    {
                                        "paragraph": paragraph,
                                        "section": section,
                                        "table_row": row_no,
                                        "table_column": col_no,
                                    },
                                )
                            )
            else:
                paragraph += 1
                if element.style and element.style.name.startswith("Heading"):
                    section = element.text
                doc.units.append(Unit(element.text, {"paragraph": paragraph, "section": section}))
        doc.metadata["pagination"] = (
            "Unavailable in DOCX XML; references are body paragraph ordinals."
        )
        doc.metadata["headers_footers"] = "Separate DOCX header/footer parts excluded from scoring."

    def _video(self, path, doc):
        with tempfile.TemporaryDirectory(prefix="integrity-asr-") as tmp:
            wav_path = Path(tmp) / "audio.wav"
            result = subprocess.run(
                [
                    ffmpeg_executable(),
                    "-nostdin",
                    "-v",
                    "error",
                    "-y",
                    "-i",
                    str(path),
                    "-t",
                    str(self.config["max_video_seconds"] + 1),
                    "-vn",
                    "-ac",
                    "1",
                    "-ar",
                    "16000",
                    "-acodec",
                    "pcm_s16le",
                    str(wav_path),
                ],
                capture_output=True,
                text=True,
                timeout=self.config["decode_timeout_seconds"],
            )
            if result.returncode:
                if (
                    "does not contain any stream" in result.stderr
                    or "matches no streams" in result.stderr
                ):
                    doc.status = "no_audio"
                    doc.warnings.append("Video has no audio track: unable to assess.")
                    return
                raise ValueError("Audio decode failed: " + result.stderr.strip()[-400:])
            with wave.open(str(wav_path), "rb") as wav:
                audio = (
                    np.frombuffer(wav.readframes(wav.getnframes()), dtype="<i2").astype(np.float32)
                    / 32768
                )
                duration = wav.getnframes() / wav.getframerate()
            doc.metadata.update(
                duration_seconds=round(duration, 3),
                audio_rms=float(np.sqrt(np.mean(audio**2))) if len(audio) else 0,
            )
            if duration > self.config["max_video_seconds"]:
                raise ValueError("Video audio duration exceeds configured limit")
            if not len(audio) or doc.metadata["audio_rms"] < self.config["silence_rms"]:
                doc.status = "silent"
                doc.warnings.append("Audio energy below silence threshold: unable to assess.")
                return
            if self.asr is None:
                from faster_whisper import WhisperModel

                self.asr = WhisperModel(
                    self.config["asr_model_path"],
                    device="cpu",
                    compute_type="int8",
                    cpu_threads=self.config["cpu_threads"],
                    local_files_only=True,
                )
            segments, info = self.asr.transcribe(
                audio,
                language="en",
                beam_size=5,
                temperature=0,
                condition_on_previous_text=False,
                vad_filter=True,
                word_timestamps=True,
            )
            segment_data = []
            for seg in segments:
                if seg.text.strip():
                    start = max(0.0, min(seg.start, duration))
                    end = max(start, min(seg.end, duration))
                    if end <= start:
                        doc.warnings.append(
                            "Dropped ASR segment outside media time bounds; review source audio."
                        )
                        continue
                    if start != seg.start or end != seg.end:
                        doc.warnings.append(
                            "ASR segment time clipped to actual media duration; raw predictions retained in metadata."
                        )
                    loc = {
                        "start_seconds": round(start, 3),
                        "end_seconds": round(end, 3),
                        "segment": len(segment_data) + 1,
                    }
                    doc.units.append(Unit(seg.text.strip(), loc))
                    segment_data.append(
                        {
                            **loc,
                            "text": seg.text.strip(),
                            "avg_logprob": seg.avg_logprob,
                            "no_speech_prob": seg.no_speech_prob,
                            "raw_asr_start_seconds": seg.start,
                            "raw_asr_end_seconds": seg.end,
                            "words": [
                                {
                                    "text": w.word,
                                    "start_seconds": max(0, min(w.start, duration)),
                                    "end_seconds": max(0, min(w.end, duration)),
                                    "probability": w.probability,
                                }
                                for w in (seg.words or [])
                            ],
                        }
                    )
            doc.metadata.update(
                asr_model="Systran/faster-whisper-tiny.en",
                asr_compute_type="int8",
                language=info.language,
                segments=segment_data,
            )
            doc.warnings.append(
                "ASR passages are model transcripts, not verified verbatim speech; timestamps have segment resolution."
            )
            if not doc.units:
                doc.status = "no_speech"
                doc.warnings.append("ASR/VAD found no speech: unable to assess.")
