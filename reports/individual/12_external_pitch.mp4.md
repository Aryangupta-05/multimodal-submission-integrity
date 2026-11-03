# Integrity audit: 12_external_pitch.mp4

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 100.0 |
| External candidate coverage | 100.0 |
| AI style indicator (uncalibrated) | None |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

6 peer and 6 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 43; excluded: 0.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**10_external.pdf**, cosine **1.0000**

`{"query_timestamp": "00:00:00.000 - 00:00:04.840", "query_start_seconds": 0.0, "query_end_seconds": 4.84, "matched_page": 1, "matched_pages": [1]}`

Query:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands

**reference:queue_design**, cosine **1.0000**

`{"query_timestamp": "00:00:00.000 - 00:00:04.840", "query_start_seconds": 0.0, "query_end_seconds": 4.84, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

- Warning: ASR passages are model transcripts, not verified verbatim speech; timestamps have segment resolution.

## Excluded material


## Peer evidence

### 1. 10_external.pdf | cosine 1.0000

Location: `{"query_timestamp": "00:00:00.000 - 00:00:04.840", "query_start_seconds": 0.0, "query_end_seconds": 4.84, "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands

### 2. 10_external.pdf | cosine 0.9802

Location: `{"query_timestamp": "00:00:00.000 - 00:00:09.860", "query_start_seconds": 0.0, "query_end_seconds": 9.86, "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn

Source passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn

### 3. 10_external.pdf | cosine 0.9762

Location: `{"query_timestamp": "00:00:05.740 - 00:00:09.860", "query_start_seconds": 5.74, "query_end_seconds": 9.86, "matched_page": 1, "matched_pages": [1]}`

Query passage:

> This lets people sit, read, or wait and shade without losing their turn

Source passage:

> This lets people sit, read,
> or wait in shade without losing their turn

### 4. 10_external.pdf | cosine 0.9518

Location: `{"query_timestamp": "00:00:00.000 - 00:00:15.520", "query_start_seconds": 0.0, "query_end_seconds": 15.52, "matched_page": 1, "matched_pages": [1]}`

Query passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

Source passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

### 5. 10_external.pdf | cosine 0.8988

Location: `{"query_timestamp": "00:00:05.740 - 00:00:15.520", "query_start_seconds": 5.74, "query_end_seconds": 15.52, "matched_page": 1, "matched_pages": [1]}`

Query passage:

> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

Source passage:

> This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

### 6. 10_external.pdf | cosine 0.8885

Location: `{"query_timestamp": "00:00:10.560 - 00:00:15.520", "query_start_seconds": 10.56, "query_end_seconds": 15.52, "matched_page": 1, "matched_pages": [1]}`

Query passage:

> The organizer should announce exceptions openly and keep an accessible route to the service desk

Source passage:

> The organiser should announce exceptions openly and
> keep an accessible route to the service desk


## External evidence

### 1. reference:queue_design | cosine 1.0000

Location: `{"query_timestamp": "00:00:00.000 - 00:00:04.840", "query_start_seconds": 0.0, "query_end_seconds": 4.84, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 2. reference:queue_design | cosine 0.9802

Location: `{"query_timestamp": "00:00:00.000 - 00:00:09.860", "query_start_seconds": 0.0, "query_end_seconds": 9.86, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 3. reference:queue_design | cosine 0.9762

Location: `{"query_timestamp": "00:00:05.740 - 00:00:09.860", "query_start_seconds": 5.74, "query_end_seconds": 9.86, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> This lets people sit, read, or wait and shade without losing their turn

Source passage:

> This lets people sit, read, or wait in shade without losing their turn

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 4. reference:queue_design | cosine 0.9518

Location: `{"query_timestamp": "00:00:00.000 - 00:00:15.520", "query_start_seconds": 0.0, "query_end_seconds": 15.52, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 5. reference:queue_design | cosine 0.8988

Location: `{"query_timestamp": "00:00:05.740 - 00:00:15.520", "query_start_seconds": 5.74, "query_end_seconds": 15.52, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

Source passage:

> This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 6. reference:queue_design | cosine 0.8885

Location: `{"query_timestamp": "00:00:10.560 - 00:00:15.520", "query_start_seconds": 10.56, "query_end_seconds": 15.52, "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> The organizer should announce exceptions openly and keep an accessible route to the service desk

Source passage:

> The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json

## AI indicator

{
  "score": null,
  "status": "insufficient_text",
  "calibrated": false,
  "explanation": "Need at least 50 words and 3 sentences; no reliable inference for short clips."
}
