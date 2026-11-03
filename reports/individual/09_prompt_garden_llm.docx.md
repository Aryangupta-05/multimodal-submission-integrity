# Integrity audit: 09_prompt_garden_llm.docx

Review priority: **LOW**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 0.0 |
| External candidate coverage | 0.0 |
| AI style indicator (uncalibrated) | 59.08 |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

0 peer and 0 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 151; excluded: 151.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

- Warning: Repeated opening prefix discounted across >=5 files; inspect exclusions because coordinated copies can resemble templates.

## Excluded material

- configured_common_prompt: 151 words. Exact excluded text and spans in JSON.

## Peer evidence

No accepted evidence windows (or extraction unavailable).

## External evidence

No accepted evidence windows (or extraction unavailable).

## AI indicator

{
  "score": 59.08,
  "status": "heuristic_only",
  "calibrated": false,
  "features": {
    "sentence_length_cv": 0.3213,
    "type_token_ratio": 0.7748,
    "transition_count": 4,
    "words": 151
  },
  "explanation": "Weighted style regularity/repetition/transition index. Not a calibrated probability or proof of AI authorship. Synthetic AI labels do not establish detector validity."
}
