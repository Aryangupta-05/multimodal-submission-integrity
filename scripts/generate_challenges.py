"""Additional edge/ambiguity inputs, isolated from the 15-file benchmark."""

from pathlib import Path
import io
import json
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.generate_dataset import docx, ROOT


def main():
    import fitz
    from PIL import Image, ImageDraw
    import imageio_ffmpeg

    target = ROOT / "challenge_submissions"
    target.mkdir(exist_ok=True)
    (target / "corrupt.pdf").write_bytes(b"%PDF-1.7\nthis is not a PDF")
    (target / "broken.mp4").write_bytes(b"invalid MP4 container")
    (target / "invalid.docx").write_bytes(b"not a zip archive")
    (target / "unsupported.xyz").write_text(
        "An unsupported file should receive its own unavailable audit."
    )
    d = fitz.open()
    d.new_page()
    d.save(target / "blank.pdf")
    img = Image.new("RGB", (800, 300), "white")
    ImageDraw.Draw(img).text((40, 100), "Scanned page requiring OCR", fill="black")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    d = fitz.open()
    p = d.new_page()
    p.insert_image(fitz.Rect(20, 20, 550, 220), stream=buffer.getvalue())
    d.save(target / "scanned.pdf")
    prompt = (ROOT / "config/common_prompt.txt").read_text()
    docx(target / "only_prompt.docx", [prompt])
    docx(
        target / "opposite_a.docx",
        [
            "The city should introduce a congestion charge for private cars entering the centre. The charge would reduce traffic and improve air quality. Revenue should pay for public buses rather than additional parking spaces. Drivers who cannot afford the charge should receive discounted transit passes."
        ],
    )
    docx(
        target / "opposite_b.docx",
        [
            "The city should not introduce a congestion charge for private cars entering the centre. The charge would not reduce traffic or improve air quality. Revenue should pay for additional parking spaces rather than public buses. Drivers who cannot afford the charge should not receive discounted transit passes."
        ],
    )
    copied = "Copper lanterns guide midnight ferries across the frozen estuary."
    docx(
        target / "short_copy_a.docx",
        [
            copied,
            "A robotics workshop can teach children to sort coloured blocks by writing simple rules on paper. The session uses cardboard pieces instead of expensive motors. Volunteers can count how many rule cards lead to the intended arrangement. No account registration is needed, and each child can take home the instructions after the exercise. The organiser will compare different teaching sequences during the following school term.",
        ],
    )
    docx(
        target / "short_copy_b.docx",
        [
            copied,
            "A municipal choir wants to choose a rehearsal venue with a comfortable acoustic response. Singers will perform the same melody in three borrowed rooms while listeners record which words remain understandable. Heavy curtains may reduce troublesome echoes. The committee should compare the notes before renting a permanent hall, because low rent alone cannot compensate for severe reverberation. The final decision will include travel time from nearby bus stops.",
        ],
    )
    docx(
        target / "attributed.docx",
        [
            '"Copper lanterns guide midnight ferries across the frozen estuary" (Source: synthetic poem).',
            "References:\nSynthetic poem, CC0, local challenge corpus.",
        ],
    )
    # A real audio stream containing all-zero samples exercises RMS silence detection.
    subprocess.run(
        [
            imageio_ffmpeg.get_ffmpeg_exe(),
            "-nostdin",
            "-y",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-i",
            "color=c=black:s=320x240:r=10",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=16000:cl=mono",
            "-t",
            "10",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            str(target / "muted.mp4"),
        ],
        check=True,
    )
    # A PDF with one extracted page and one image-only/blank page must be partial, not zero.
    d = fitz.open(ROOT / "sample_submissions/10_external.pdf")
    d.new_page()
    d.save(target / "partial.pdf")
    # Shared prompt plus a copied answer must still be found after prompt suppression.
    from scripts.generate_dataset import ANSWERS

    docx(target / "prompt_copy_a.docx", [prompt, ANSWERS["07_prompt_bakery.docx"]])
    docx(target / "prompt_copy_b.docx", [prompt, ANSWERS["07_prompt_bakery.docx"]])
    labels = {
        "ambiguities": [
            {
                "files": ["opposite_a.docx", "opposite_b.docx"],
                "question": "Does high semantic similarity distinguish opposite policy conclusions?",
                "expected": "similarity may be high; recommendation polarity differs",
            },
            {
                "files": ["short_copy_a.docx", "short_copy_b.docx"],
                "question": "Can a ten-word literal excerpt survive the twelve-word evidence floor?",
                "expected": "short overlap can be missed",
            },
        ],
        "statuses": {
            "corrupt.pdf": "error",
            "broken.mp4": "error",
            "invalid.docx": "error",
            "unsupported.xyz": "unsupported",
            "blank.pdf": "unextractable",
            "scanned.pdf": "unextractable",
            "muted.mp4": "silent",
            "partial.pdf": "partial",
        },
        "provenance": "All synthetic Codex-assisted CC0; diagnostic inputs, not an independent validation set.",
    }
    (ROOT / "evaluation/challenge_ground_truth.json").write_text(json.dumps(labels, indent=2))
    print(f"Created {len(list(target.iterdir()))} challenges.")


if __name__ == "__main__":
    main()
