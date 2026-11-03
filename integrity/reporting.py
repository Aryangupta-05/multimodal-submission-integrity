"""Stable JSON schema fields and compact Markdown evidence cards."""

import json
from pathlib import Path
from .matching import coverage
from .signals import ai_indicator
from .text import passage


def make_report(doc, peer_matches, external_matches, config):
    eligible = len(doc.tokens) - len(doc.excluded)
    assessable = doc.status in {"ok", "partial"} and eligible >= config["minimum_evidence_words"]
    peer = coverage(peer_matches, eligible) if assessable else None
    external = coverage(external_matches, eligible) if assessable else None
    ai_text, _ = (
        passage(doc, [i for i in range(len(doc.tokens)) if i not in doc.excluded])
        if eligible
        else ("", [])
    )
    ai = (
        ai_indicator(ai_text)
        if assessable
        else {"score": None, "status": "unable_to_assess", "calibrated": False}
    )
    high = max(peer or 0, external or 0)
    risk = (
        "UNABLE_TO_ASSESS"
        if not assessable
        else "HIGH"
        if high >= 50
        else "MEDIUM"
        if high >= 15
        else "LOW"
    )
    counts = {}
    for reason in doc.excluded.values():
        counts[reason] = counts.get(reason, 0) + 1
    exclusions = []
    for reason in sorted(counts):
        ids = [i for i, r in doc.excluded.items() if r == reason]
        text, spans = passage(doc, ids)
        exclusions.append(
            {"reason": reason, "word_count": len(ids), "passage": text, "spans": spans}
        )
    return {
        "schema_version": "1.0",
        "document_id": doc.document_id,
        "total_integrity_risk": risk,
        "scores": {
            "peer_similarity_percentage": peer,
            "external_similarity_percentage": external,
            "ai_generated_probability": ai["score"],
        },
        "peer_matches": peer_matches,
        "multimodal_matches": [
            m for m in peer_matches if doc.kind != Path(m["matched_file"]).suffix.lstrip(".")
        ],
        "external_matches": external_matches,
        "extraction": {
            "status": doc.status,
            "kind": doc.kind,
            "assessable": assessable,
            "sha256": doc.sha256,
            "raw_word_count": len(doc.tokens),
            "eligible_word_count": eligible,
            "excluded_word_count": len(doc.excluded),
            "metadata": doc.metadata,
        },
        "exclusions": exclusions,
        "warnings": doc.warnings,
        "ai_indicator": ai,
        "scoring": {
            "semantic_threshold": config["semantic_threshold"],
            "coverage_unit": "unique eligible normalized word positions",
            "percentage_formula": "100 * union of query word positions in accepted windows / eligible query words",
            "coverage_caveat": "Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.",
            "risk_rule": "HIGH coverage >=50%; MEDIUM >=15%; else LOW. AI indicator never raises risk alone.",
            "unknown_rule": "Unassessable and fully excluded documents have null scores; partial PDFs cover extracted text only.",
        },
        "explanations": f"{len(peer_matches)} peer and {len(external_matches)} external evidence windows above cosine {config['semantic_threshold']}. Review exact source spans before any conclusion. AI style index is uncalibrated.",
    }


def markdown(report):
    scores = report["scores"]
    rows = [
        f"# Integrity audit: {report['document_id']}",
        "",
        f"Review priority: **{report['total_integrity_risk']}**",
        f"Extraction: `{report['extraction']['status']}`; assessable: `{report['extraction']['assessable']}`.",
        "",
        "| Signal | Value |",
        "|---|---:|",
        f"| Peer candidate coverage | {scores['peer_similarity_percentage']} |",
        f"| External candidate coverage | {scores['external_similarity_percentage']} |",
        f"| AI style indicator (uncalibrated) | {scores['ai_generated_probability']} |",
        "",
        "> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.",
        "",
        report["explanations"],
        "",
        "## Extraction and scoring",
        "",
        f"Eligible words: {report['extraction']['eligible_word_count']}; excluded: {report['extraction']['excluded_word_count']}.",
        report["scoring"]["percentage_formula"],
        report["scoring"]["coverage_caveat"],
        "",
    ]
    # One strongest card per source lets a reviewer navigate immediately.
    quick = []
    seen_sources = set()
    for match in sorted(
        report["peer_matches"] + report["external_matches"], key=lambda m: -m["similarity_score"]
    ):
        if match["matched_file"] not in seen_sources:
            quick.append(match)
            seen_sources.add(match["matched_file"])
        if len(quick) == 3:
            break
    rows += [
        "## Quick review",
        "",
        "Strongest evidence per source (up to three); all accepted windows follow below.",
        "",
    ]
    for match in quick:
        loc = {k: v for k, v in match["location"].items() if not k.endswith("_spans")}
        rows += [
            f"**{match['matched_file']}**, cosine **{match['similarity_score']:.4f}**",
            "",
            f"`{json.dumps(loc, ensure_ascii=False)}`",
            "",
            "Query:",
            "",
            "> " + match["query_passage"].replace("\n", "\n> "),
            "",
            "Source:",
            "",
            "> " + match["matched_passage"].replace("\n", "\n> "),
            "",
        ]
    for warning in report["warnings"]:
        rows.append(f"- Warning: {warning}")
    rows += ["", "## Excluded material", ""]
    for exclusion in report["exclusions"]:
        rows += [
            f"- {exclusion['reason']}: {exclusion['word_count']} words. Exact excluded text and spans in JSON."
        ]
    for label, key in [
        ("Peer evidence", "peer_matches"),
        ("External evidence", "external_matches"),
    ]:
        rows += ["", f"## {label}", ""]
        if not report[key]:
            rows.append("No accepted evidence windows (or extraction unavailable).")
        for i, match in enumerate(report[key], 1):
            loc = {k: v for k, v in match["location"].items() if not k.endswith("_spans")}
            rows += [
                f"### {i}. {match['matched_file']} | cosine {match['similarity_score']:.4f}",
                "",
                f"Location: `{json.dumps(loc, ensure_ascii=False)}`",
                "",
                "Query passage:",
                "",
                "> " + match["query_passage"].replace("\n", "\n> "),
                "",
                "Source passage:",
                "",
                "> " + match["matched_passage"].replace("\n", "\n> "),
                "",
            ]
            if "provenance" in match:
                rows.append(f"Source URL: {match['provenance']['source_url']}")
    rows += [
        "",
        "## AI indicator",
        "",
        json.dumps(report["ai_indicator"], ensure_ascii=False, indent=2),
        "",
    ]
    return "\n".join(rows)


def write_report(report, output_dir):
    # Input ids include extensions, avoiding PDF/DOCX same-stem collisions.
    target = Path(output_dir) / report["document_id"]
    target.parent.mkdir(parents=True, exist_ok=True)
    Path(str(target) + ".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    Path(str(target) + ".md").write_text(markdown(report), encoding="utf-8")
