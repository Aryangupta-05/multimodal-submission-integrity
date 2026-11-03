"""Explainable deterministic style indicator; deliberately not a trained detector."""

import re
import statistics
from .text import words


def ai_indicator(text):
    tokens = words(text)
    sentences = [words(x) for x in re.split(r"[.!?]+", text) if len(words(x)) >= 3]
    if len(tokens) < 50 or len(sentences) < 3:
        return {
            "score": None,
            "status": "insufficient_text",
            "calibrated": False,
            "explanation": "Need at least 50 words and 3 sentences; no reliable inference for short clips.",
        }
    lengths = [len(s) for s in sentences]
    cv = statistics.pstdev(lengths) / max(statistics.mean(lengths), 1)
    diversity = len(set(tokens)) / len(tokens)
    transitions = sum(
        text.casefold().count(s)
        for s in ["furthermore", "moreover", "in conclusion", "additionally", "it is essential"]
    )
    regularity = max(0, 1 - min(cv, 1))
    repetition = 1 - diversity
    score = round(100 * (0.55 * regularity + 0.30 * repetition + 0.15 * min(transitions / 4, 1)), 2)
    return {
        "score": score,
        "status": "heuristic_only",
        "calibrated": False,
        "features": {
            "sentence_length_cv": round(cv, 4),
            "type_token_ratio": round(diversity, 4),
            "transition_count": transitions,
            "words": len(tokens),
        },
        "explanation": "Weighted style regularity/repetition/transition index. Not a calibrated probability or proof of AI authorship. Synthetic AI labels do not establish detector validity.",
    }
