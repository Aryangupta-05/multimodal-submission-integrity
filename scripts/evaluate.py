"""Compute measured benchmark metrics from reports; labels never enter runtime."""

from itertools import combinations
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def metrics(labels, predictions):
    tp = sum(a and b for a, b in zip(labels, predictions))
    fp = sum(not a and b for a, b in zip(labels, predictions))
    fn = sum(a and not b for a, b in zip(labels, predictions))
    tn = sum(not a and not b for a, b in zip(labels, predictions))
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    return {
        "n": len(labels),
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": precision,
        "recall": recall,
        "f1": 2 * precision * recall / (precision + recall) if precision + recall else 0,
    }


def wer(expected, actual):
    a = re.findall(r"\w+", expected.casefold())
    b = re.findall(r"\w+", actual.casefold())
    row = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        nxt = [i]
        for j, y in enumerate(b, 1):
            nxt.append(min(nxt[-1] + 1, row[j] + 1, row[j - 1] + (x != y)))
        row = nxt
    return {"reference_words": len(a), "edits": row[-1], "wer": row[-1] / max(1, len(a))}


def evaluate(folder="reports"):
    report_dir = ROOT / folder
    manifest = json.loads((ROOT / "sample_submissions/dataset_manifest.json").read_text())
    matrix = json.loads((report_dir / "similarity_matrix.json").read_text())
    summary = json.loads((report_dir / "batch_summary.json").read_text())
    ids = [f["file"] for f in manifest["files"] if f["assessable"]]
    positives = {frozenset(p) for p in manifest["positive_peer_pairs"]}
    pairs = []
    for a, b in combinations(ids, 2):
        score = max(matrix[a][b] or 0, matrix[b][a] or 0)
        pairs.append(
            {
                "a": a,
                "b": b,
                "expected": frozenset([a, b]) in positives,
                "predicted": score >= 15,
                "max_directional_coverage": score,
            }
        )
    result = {
        "unit": "unordered assessable document pair",
        "pair_rule": "Either direction has >=15% candidate coverage with cosine >=0.80 and >=12-word evidence windows.",
        "peer": metrics([p["expected"] for p in pairs], [p["predicted"] for p in pairs]),
        "pairs": pairs,
    }
    external = []
    for doc_id in ids:
        path = report_dir / "individual" / (doc_id + ".json")
        r = (
            json.loads(path.read_text())
            if path.exists()
            else {"scores": next(x for x in summary["reports"] if x["document_id"] == doc_id)}
        )
        external.append(
            {
                "file": doc_id,
                "expected": doc_id in manifest["external_positive_files"],
                "predicted": (r["scores"]["external_similarity_percentage"] or 0) >= 15,
                "coverage": r["scores"]["external_similarity_percentage"],
            }
        )
    result["external"] = metrics(
        [e["expected"] for e in external], [e["predicted"] for e in external]
    )
    result["external_cases"] = external
    extraction = (
        json.loads((report_dir / "extracted_documents.json").read_text())
        if (report_dir / "extracted_documents.json").exists()
        else {}
    )
    result["asr"] = {
        name: wer(text, " ".join(u["text"] for u in extraction[name]["units"]))
        for name, text in manifest["intended_transcripts"].items()
        if name in extraction
    }
    result["boilerplate"] = {
        name: next(r for r in summary["reports"] if r["document_id"] == name)[
            "peer_similarity_percentage"
        ]
        for name in manifest["shared_prompt_files"]
    }
    result["measured_resources"] = {
        k: summary[k] for k in ["runtime_seconds", "cpu_seconds", "peak_working_set_mb", "hardware"]
    }
    return result


def main():
    output = ROOT / "evaluation"
    output.mkdir(exist_ok=True)
    result = evaluate()
    (output / "metrics.json").write_text(json.dumps(result, indent=2))
    baseline = ROOT / "evaluation/baseline"
    if baseline.exists():
        (output / "baseline_metrics.json").write_text(
            json.dumps(evaluate("evaluation/baseline"), indent=2)
        )
    challenge = ROOT / "challenge_reports/similarity_matrix.json"
    if challenge.exists():
        matrix = json.loads(challenge.read_text())
        cosine = json.loads((ROOT / "challenge_reports/max_cosine_matrix.json").read_text())
        labels = json.loads((output / "challenge_ground_truth.json").read_text())
        for item in labels["ambiguities"]:
            a, b = item["files"]
            item["max_cosine"] = cosine[a][b]
            item["coverage_a_to_b"] = matrix[a][b]
            item["coverage_b_to_a"] = matrix[b][a]
        (output / "challenge_results.json").write_text(json.dumps(labels, indent=2))
    print(json.dumps({k: result[k] for k in ["peer", "external", "asr", "boilerplate"]}, indent=2))


if __name__ == "__main__":
    main()
