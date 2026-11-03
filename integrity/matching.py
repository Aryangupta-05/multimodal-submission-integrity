"""Evidence retrieval and token-union coverage, not cosine-as-percentage."""

from collections import defaultdict
from .text import passage


def stamp(seconds):
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{int(hours):02}:{int(minutes):02}:{secs:06.3f}"


def location_fields(spans, prefix):
    result = {prefix + "_spans": spans}
    pages = sorted({s["page"] for s in spans if "page" in s})
    paragraphs = sorted({s["paragraph"] for s in spans if "paragraph" in s})
    if pages:
        result[prefix + "_page"] = pages[0]
        result[prefix + "_pages"] = pages
    if paragraphs:
        result[prefix + "_paragraphs"] = paragraphs
        result[prefix + "_sections"] = list(
            dict.fromkeys(s["section"] for s in spans if "section" in s)
        )
    timed = [s for s in spans if "start_seconds" in s]
    if timed:
        start = min(s["start_seconds"] for s in timed)
        end = max(s["end_seconds"] for s in timed)
        result[prefix + "_timestamp"] = f"{stamp(start)} - {stamp(end)}"
        result[prefix + "_start_seconds"] = start
        result[prefix + "_end_seconds"] = end
    return result


def find_matches(doc, documents, windows, matrix, threshold, minimum_words, external=False):
    """Best source window per query window per source; no filename/content-hash self filtering."""
    by_file = defaultdict(list)
    query_indices = [i for i, w in enumerate(windows) if w.document_id == doc.document_id]
    sources = [
        i
        for i, w in enumerate(windows)
        if w.document_id != doc.document_id
        and (documents[w.document_id].kind == "reference") == external
    ]
    seen = set()
    for qi in query_indices:
        query = windows[qi]
        if len(query.token_ids) < minimum_words:
            continue
        best = {}
        for si in sources:
            source = windows[si]
            if len(source.token_ids) < minimum_words:
                continue
            score = float(matrix[qi, si])
            if score >= threshold and (
                source.document_id not in best or score > best[source.document_id][0]
            ):
                best[source.document_id] = (score, si)
        for source_id, (score, si) in best.items():
            source = windows[si]
            key = (source_id, tuple(query.token_ids), tuple(source.token_ids))
            if key in seen:
                continue
            seen.add(key)
            query_text, query_spans = passage(doc, query.token_ids)
            source_doc = documents[source_id]
            source_text, source_spans = passage(source_doc, source.token_ids)
            qvalues = {doc.tokens[i].value for i in query.token_ids}
            svalues = {source_doc.tokens[i].value for i in source.token_ids}
            match = {
                "matched_file": source_id,
                "similarity_score": round(score, 6),
                "query_passage": query_text,
                "matched_passage": source_text,
                "location": {
                    **location_fields(query_spans, "query"),
                    **location_fields(source_spans, "matched"),
                },
                "query_token_ids": query.token_ids,
                "matched_token_ids": source.token_ids,
                "query_window_role": query.role,
                "matched_window_role": source.role,
                "lexical_jaccard": round(
                    len(qvalues & svalues) / max(1, len(qvalues | svalues)), 4
                ),
                "interpretation": "Candidate semantic overlap requiring human review; not a misconduct finding.",
            }
            if external:
                match["provenance"] = source_doc.metadata
            by_file[source_id].append(match)
    matches = [
        m
        for file in sorted(by_file)
        for m in sorted(by_file[file], key=lambda m: -m["similarity_score"])
    ]
    return matches


def coverage(matches, eligible_count):
    if eligible_count == 0:
        return None
    ids = {i for m in matches for i in m["query_token_ids"]}
    return round(100 * len(ids) / eligible_count, 2)
