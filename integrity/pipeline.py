"""Batch orchestration. Runtime never opens dataset_manifest.json."""

from dataclasses import asdict
from hashlib import sha256
import csv
import json
from pathlib import Path
import platform
import time

import psutil

from .extractors import Extractor
from .index import Embedder, cosine_matrix
from .matching import find_matches, coverage
from .reporting import make_report, write_report
from .text import (
    normalize,
    exclude_known,
    exclude_repeated_prefixes,
    make_windows,
    sentence_windows,
)
from .types import Document, Unit


ROOT = Path(__file__).resolve().parent.parent


def load_config(path=None):
    config = json.loads(Path(path or ROOT / "config.json").read_text(encoding="utf-8"))
    for key in ["embedding_model_path", "asr_model_path", "cache_dir", "reference_dir"]:
        config[key] = str((ROOT / config[key]).resolve())
    config["boilerplate_files"] = [str((ROOT / p).resolve()) for p in config["boilerplate_files"]]
    if not 0 < config["semantic_threshold"] <= 1:
        raise ValueError("semantic_threshold must be in (0, 1]")
    if not 0 <= config["chunk_overlap"] < config["chunk_tokens"] <= 250:
        raise ValueError(
            "chunk_tokens must be <=250 (MiniLM max 256) and overlap smaller than chunk"
        )
    if not 0 <= config["evidence_overlap"] < config["evidence_tokens"] <= 250:
        raise ValueError("Invalid evidence window sizing")
    return config


def reference_documents(path):
    docs = []
    for entry in sorted(Path(path).glob("*.json")):
        data = json.loads(entry.read_text(encoding="utf-8"))
        doc = Document(
            "reference:" + entry.stem,
            "reference",
            sha256(data["text"].encode()).hexdigest(),
            metadata={k: v for k, v in data.items() if k != "text"},
        )
        doc.units = [Unit(data["text"], {"paragraph": 1, "section": data["title"]})]
        docs.append(normalize(doc))
    return docs


def run(input_dir, output_dir, config):
    start = time.perf_counter()
    process = psutil.Process()
    cpu_start = process.cpu_times()
    output = Path(output_dir).resolve()
    source = Path(input_dir).resolve()
    if not source.is_dir():
        raise ValueError(f"Input directory does not exist: {source}")
    if output == source:
        raise ValueError("Output directory must differ from input directory")
    paths = sorted(
        p
        for p in source.rglob("*")
        if p.is_file()
        and p.name != "dataset_manifest.json"
        and output not in p.resolve().parents
        and not any(part.startswith(".") for part in p.relative_to(source).parts)
    )
    if not paths:
        raise ValueError("Input directory contains no submissions")
    output.mkdir(parents=True, exist_ok=True)
    extractor = Extractor(config)
    docs = []
    extraction_timings = {}
    for path in paths:
        t = time.perf_counter()
        doc = normalize(extractor.extract(path, path.relative_to(source).as_posix()))
        docs.append(doc)
        extraction_timings[doc.document_id] = round(time.perf_counter() - t, 4)
        print(f"Extracted {doc.document_id}: {doc.status}, {len(doc.tokens)} words", flush=True)
    texts = [
        Path(p).read_text(encoding="utf-8") for p in config["boilerplate_files"] if Path(p).exists()
    ]
    for doc in docs:
        exclude_known(doc, texts)
    exclude_repeated_prefixes(docs)
    refs = reference_documents(config["reference_dir"])
    all_docs = {d.document_id: d for d in docs + refs}
    embed_start = time.perf_counter()
    embedder = Embedder(config)
    windows = []
    chunks = []
    for doc in docs + refs:
        if doc.status not in {"ok", "partial"}:
            continue
        main = make_windows(
            doc, embedder.tokenizer, config["chunk_tokens"], config["chunk_overlap"]
        )
        chunks += main
        windows += main
        windows += make_windows(
            doc,
            embedder.tokenizer,
            config["evidence_tokens"],
            config["evidence_overlap"],
            role="evidence",
        )
        windows += sentence_windows(doc, embedder.tokenizer, config["evidence_tokens"])
    vectors = embedder.encode(windows)
    matrix = cosine_matrix(vectors)
    embed_seconds = time.perf_counter() - embed_start
    np_path = output / "vectors.npz"
    import numpy as np

    np.savez_compressed(np_path, embeddings=vectors)
    (output / "index_windows.json").write_text(
        json.dumps([asdict(w) for w in windows], indent=2), encoding="utf-8"
    )
    # Store raw extraction and token offsets to independently verify report passages.
    (output / "extracted_documents.json").write_text(
        json.dumps({d.document_id: asdict(d) for d in docs + refs}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    reports = []
    peer_matrix, max_cosine = {}, {}
    for doc in docs:
        peer = find_matches(
            doc,
            all_docs,
            windows,
            matrix,
            config["semantic_threshold"],
            config["minimum_evidence_words"],
        )
        external = find_matches(
            doc,
            all_docs,
            windows,
            matrix,
            config["semantic_threshold"],
            config["minimum_evidence_words"],
            external=True,
        )
        report = make_report(doc, peer, external, config)
        reports.append(report)
        write_report(report, output / "individual")
        peer_matrix[doc.document_id], max_cosine[doc.document_id] = {}, {}
        for other in docs:
            assessable = (
                report["extraction"]["assessable"]
                and other.status in {"ok", "partial"}
                and len(other.tokens) - len(other.excluded) >= config["minimum_evidence_words"]
            )
            ms = [m for m in peer if m["matched_file"] == other.document_id]
            peer_matrix[doc.document_id][other.document_id] = (
                coverage(ms, len(doc.tokens) - len(doc.excluded))
                if assessable and other.document_id != doc.document_id
                else None
            )
            qidx = [i for i, w in enumerate(windows) if w.document_id == doc.document_id]
            sidx = [i for i, w in enumerate(windows) if w.document_id == other.document_id]
            max_cosine[doc.document_id][other.document_id] = (
                round(float(matrix[np.ix_(qidx, sidx)].max()), 6)
                if qidx and sidx and other.document_id != doc.document_id
                else None
            )
    for name, data in [("similarity_matrix", peer_matrix), ("max_cosine_matrix", max_cosine)]:
        (output / f"{name}.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
        with (output / f"{name}.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            ids = [d.document_id for d in docs]
            writer.writerow(["query\\source"] + ids)
            for doc_id in ids:
                writer.writerow([doc_id] + [data[doc_id][i] for i in ids])
    cpu_end = process.cpu_times()
    memory = process.memory_info()
    summary = {
        "documents": len(docs),
        "assessable": sum(r["extraction"]["assessable"] for r in reports),
        "statuses": {d.document_id: d.status for d in docs},
        "chunks": len(chunks),
        "indexed_windows": len(windows),
        "runtime_seconds": round(time.perf_counter() - start, 4),
        "embedding_and_index_seconds": round(embed_seconds, 4),
        "extraction_seconds": extraction_timings,
        "cpu_seconds": round(cpu_end.user + cpu_end.system - cpu_start.user - cpu_start.system, 4),
        "rss_end_mb": round(memory.rss / 1024**2, 2),
        "peak_working_set_mb": round(getattr(memory, "peak_wset", memory.rss) / 1024**2, 2),
        "hardware": {
            "platform": platform.platform(),
            "processor": platform.processor(),
            "logical_cpus": psutil.cpu_count(),
            "ram_gb": round(psutil.virtual_memory().total / 1024**3, 2),
        },
        "models": {
            "embedding": config["embedding_model"],
            "embedding_revision": config["embedding_revision"],
            "asr": config["asr_model"],
            "asr_revision": config["asr_revision"],
        },
        "config": {
            k: v
            for k, v in config.items()
            if not k.endswith("_path")
            and k not in ["cache_dir", "boilerplate_files", "reference_dir"]
        },
        "warning": "Measured on synthetic English/TTS data. Pairwise coverage is directional. Null diagonal/self or unavailable. AI scores never prove misconduct.",
        "reports": [
            {
                "document_id": r["document_id"],
                "status": r["extraction"]["status"],
                "risk": r["total_integrity_risk"],
                **r["scores"],
            }
            for r in reports
        ],
    }
    (output / "batch_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    lines = [
        "# Batch summary",
        "",
        f"Processed {len(docs)} files; {summary['assessable']} assessable.",
        f"Measured wall time: {summary['runtime_seconds']} seconds; peak working set: {summary['peak_working_set_mb']} MiB.",
        "",
        "| Document | Status | Peer % | External % | AI style % |",
        "|---|---|---:|---:|---:|",
    ]
    lines += [
        f"| {r['document_id']} | {r['status']} | {r['peer_similarity_percentage']} | {r['external_similarity_percentage']} | {r['ai_generated_probability']} |"
        for r in summary["reports"]
    ]
    lines += [
        "",
        summary["warning"],
        "",
        "See individual/*.md for passages and locations; similarity_matrix.csv is coverage, max_cosine_matrix.csv is cosine.",
    ]
    (output / "batch_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary
