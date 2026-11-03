# Integrity audit: 10_external.pdf

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 82.67 |
| External candidate coverage | 100.0 |
| AI style indicator (uncalibrated) | 50.97 |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

8 peer and 15 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 75; excluded: 0.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**12_external_pitch.mp4**, cosine **1.0000**

`{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:00.000 - 00:00:04.840", "matched_start_seconds": 0.0, "matched_end_seconds": 4.84}`

Query:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands

Source:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

**reference:queue_design**, cosine **1.0000**

`{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query:

> A queue works best when arrivals can see how service order is decided. Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source:

> A queue works best when arrivals can see how service order is decided. Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk. A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand


## Excluded material


## Peer evidence

### 1. 12_external_pitch.mp4 | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:00.000 - 00:00:04.840", "matched_start_seconds": 0.0, "matched_end_seconds": 4.84}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

### 2. 12_external_pitch.mp4 | cosine 0.9802

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:00.000 - 00:00:09.860", "matched_start_seconds": 0.0, "matched_end_seconds": 9.86}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn

### 3. 12_external_pitch.mp4 | cosine 0.9762

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:05.740 - 00:00:09.860", "matched_start_seconds": 5.74, "matched_end_seconds": 9.86}`

Query passage:

> This lets people sit, read,
> or wait in shade without losing their turn

Source passage:

> This lets people sit, read, or wait and shade without losing their turn

### 4. 12_external_pitch.mp4 | cosine 0.9518

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:00.000 - 00:00:15.520", "matched_start_seconds": 0.0, "matched_end_seconds": 15.52}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

### 5. 12_external_pitch.mp4 | cosine 0.9102

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:00.000 - 00:00:15.520", "matched_start_seconds": 0.0, "matched_end_seconds": 15.52}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands
> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

### 6. 12_external_pitch.mp4 | cosine 0.8988

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:05.740 - 00:00:15.520", "matched_start_seconds": 5.74, "matched_end_seconds": 15.52}`

Query passage:

> This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk

### 7. 12_external_pitch.mp4 | cosine 0.8885

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:10.560 - 00:00:15.520", "matched_start_seconds": 10.56, "matched_end_seconds": 15.52}`

Query passage:

> The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> The organizer should announce exceptions openly and keep an accessible route to the service desk

### 8. 12_external_pitch.mp4 | cosine 0.8081

Location: `{"query_page": 1, "query_pages": [1], "matched_timestamp": "00:00:05.740 - 00:00:15.520", "matched_start_seconds": 5.74, "matched_end_seconds": 15.52}`

Query passage:

> This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> This lets people sit, read, or wait and shade without losing their turn
> The organizer should announce exceptions openly and keep an accessible route to the service desk


## External evidence

### 1. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk. A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 2. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> A queue works best when arrivals can see how service order is decided

Source passage:

> A queue works best when arrivals can see how service order is decided

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 3. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets
> separate a visitor's place in line from the place where that visitor stands

Source passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 4. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn

Source passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 5. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> A queue works best when arrivals can see how service order is decided. Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 6. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 7. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 8. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 9. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> Numbered tickets
> separate a visitor's place in line from the place where that visitor stands. This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> Numbered tickets separate a visitor's place in line from the place where that visitor stands. This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk. A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 10. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> This lets people sit, read,
> or wait in shade without losing their turn

Source passage:

> This lets people sit, read, or wait in shade without losing their turn

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 11. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 12. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> This lets people sit, read,
> or wait in shade without losing their turn. The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> This lets people sit, read, or wait in shade without losing their turn. The organiser should announce exceptions openly and keep an accessible route to the service desk. A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 13. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> The organiser should announce exceptions openly and
> keep an accessible route to the service desk

Source passage:

> The organiser should announce exceptions openly and keep an accessible route to the service desk

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 14. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> The organiser should announce exceptions openly and
> keep an accessible route to the service desk. A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> The organiser should announce exceptions openly and keep an accessible route to the service desk. A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json
### 15. reference:queue_design | cosine 1.0000

Location: `{"query_page": 1, "query_pages": [1], "matched_paragraphs": [1], "matched_sections": ["Transparent queue design"]}`

Query passage:

> A ticket system does not create more service
> capacity; it only makes the existing waiting process easier to understand

Source passage:

> A ticket system does not create more service capacity; it only makes the existing waiting process easier to understand

Source URL: https://github.com/Aryangupta-05/multimodal-submission-integrity/blob/main/reference_corpus/queue_design.json

## AI indicator

{
  "score": 50.97,
  "status": "heuristic_only",
  "calibrated": false,
  "features": {
    "sentence_length_cv": 0.1461,
    "type_token_ratio": 0.8667,
    "transition_count": 0,
    "words": 75
  },
  "explanation": "Weighted style regularity/repetition/transition index. Not a calibrated probability or proof of AI authorship. Synthetic AI labels do not establish detector validity."
}
