"""Normalization with immutable raw offsets, exclusions and overlapping windows."""

from collections import defaultdict
import re
import unicodedata

from .types import Token, Window

WORD = re.compile(r"\b\w+(?:['\u2019-]\w+)*\b", re.UNICODE)


def words(text):
    return [
        unicodedata.normalize("NFKC", m.group()).casefold().replace("\u2019", "'")
        for m in WORD.finditer(text)
    ]


def normalized_text(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().replace("\u2019", "'").split())


def normalize(doc):
    for unit_no, unit in enumerate(doc.units):
        for match in WORD.finditer(unit.text):
            value = unicodedata.normalize("NFKC", match.group()).casefold().replace("\u2019", "'")
            doc.tokens.append(Token(value, unit_no, match.start(), match.end()))
    return doc


def exclude_known(doc, boilerplate_texts):
    """Known challenge prompts are task config, never dataset relationship labels."""
    values = [t.value for t in doc.tokens]
    for template in boilerplate_texts:
        target = words(template)
        if not target:
            continue
        for start in range(len(values) - len(target) + 1):
            if values[start : start + len(target)] == target:
                for i in range(start, start + len(target)):
                    doc.excluded[i] = "configured_common_prompt"
    for ui, unit in enumerate(doc.units):
        # Reference section detection is conservative and per paragraph/page unit.
        if re.match(r"^\s*(references|bibliography)\s*[:\n]", unit.text, re.I):
            for i, token in enumerate(doc.tokens):
                if token.unit == ui:
                    doc.excluded[i] = "reference_list"
        # Only explicitly attributed quotations are discounted, and remain auditable.
        for match in re.finditer(
            r'["\u201c]([^"\u201d]{20,})["\u201d]\s*\((?:source|cited)\s*:[^)]+\)', unit.text, re.I
        ):
            for i, token in enumerate(doc.tokens):
                if token.unit == ui and token.start >= match.start() and token.end <= match.end():
                    doc.excluded[i] = "explicitly_attributed_quotation"


def exclude_repeated_prefixes(docs, min_documents=5, min_words=40, max_words=200):
    """Discover only long identical opening prefixes. Never remove interior repeats."""
    prefix_groups = defaultdict(list)
    for doc in docs:
        if len(doc.tokens) >= min_words:
            prefix_groups[tuple(t.value for t in doc.tokens[:min_words])].append(doc)
    for group in prefix_groups.values():
        if len(group) < min_documents:
            continue
        common = min(max_words, min(len(d.tokens) for d in group))
        for i in range(min_words, common):
            if len({d.tokens[i].value for d in group}) != 1:
                common = i
                break
        for doc in group:
            for i in range(common):
                doc.excluded.setdefault(i, "discovered_common_opening_prefix")
            doc.warnings.append(
                "Repeated opening prefix discounted across >=5 files; inspect exclusions because coordinated copies can resemble templates."
            )


def eligible_runs(doc):
    run = []
    for i in range(len(doc.tokens)):
        if i in doc.excluded:
            if run:
                yield run
                run = []
        else:
            run.append(i)
    if run:
        yield run


def passage(doc, token_ids):
    """Return exact slices from raw units; no reconstructed normalized prose."""
    grouped = []
    previous_tid = None
    for tid in token_ids:
        token = doc.tokens[tid]
        if grouped and grouped[-1][0] == token.unit and previous_tid == tid - 1:
            grouped[-1][2] = token.end
        else:
            grouped.append([token.unit, token.start, token.end])
        previous_tid = tid
    spans = [
        {
            "unit_index": ui,
            "char_start": a,
            "char_end": b,
            "text": doc.units[ui].text[a:b],
            **doc.units[ui].location,
        }
        for ui, a, b in grouped
    ]
    return "\n".join(s["text"] for s in spans), spans


def make_windows(doc, tokenizer, target=220, overlap=35, role="chunk"):
    result = []
    costs = [max(1, len(tokenizer.encode(t.value, add_special_tokens=False))) for t in doc.tokens]
    for run in eligible_runs(doc):
        start = 0
        while start < len(run):
            end, budget = start, 0
            while end < len(run) and budget + costs[run[end]] <= target:
                budget += costs[run[end]]
                end += 1
            if end == start:
                end += 1
            ids = run[start:end]
            text, _ = passage(doc, ids)
            # Count actual model pieces including punctuation. Never rely on word estimates.
            while len(tokenizer.encode(text, add_special_tokens=False)) > target and len(ids) > 1:
                end -= 1
                ids = run[start:end]
                text, _ = passage(doc, ids)
            n = len(tokenizer.encode(text, add_special_tokens=False))
            if len(ids) >= 6:
                result.append(Window(doc.document_id, ids, text, n, role, normalized_text(text)))
            if end >= len(run):
                break
            next_start, used = end, 0
            while next_start > start + 1 and used < overlap:
                next_start -= 1
                used += costs[run[next_start]]
            start = max(start + 1, next_start)
    return result


def sentence_windows(doc, tokenizer, target=95):
    """Sentence-aligned evidence avoids diluting short copied excerpts with context.

    Raw sentence boundaries come from punctuation; ASR segments can be combined.
    Consecutive sentence groups begin at every boundary, up to target pieces.
    """
    sentences = []
    for run in eligible_runs(doc):
        current = []
        for pos, tid in enumerate(run):
            current.append(tid)
            token = doc.tokens[tid]
            next_tid = run[pos + 1] if pos + 1 < len(run) else None
            next_token = doc.tokens[next_tid] if next_tid is not None else None
            unit = doc.units[token.unit]
            stop = (
                next_token.start if next_token and next_token.unit == token.unit else len(unit.text)
            )
            suffix = unit.text[token.end : stop]
            if re.search(r"[.!?]", suffix) or next_tid is None:
                sentences.append(current)
                current = []
    result = []
    for i in range(len(sentences)):
        ids = []
        for sentence in sentences[i : i + 4]:
            if ids and sentence[0] != ids[-1] + 1:
                break
            candidate = ids + sentence
            text, _ = passage(doc, candidate)
            count = len(tokenizer.encode(text, add_special_tokens=False))
            if count > target:
                break
            ids = candidate
            if len(ids) >= 12:
                result.append(
                    Window(
                        doc.document_id,
                        ids.copy(),
                        text,
                        count,
                        "sentence_evidence",
                        normalized_text(text),
                    )
                )
    return result
