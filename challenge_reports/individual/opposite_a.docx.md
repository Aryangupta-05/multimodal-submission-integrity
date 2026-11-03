# Integrity audit: opposite_a.docx

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 100.0 |
| External candidate coverage | 0.0 |
| AI style indicator (uncalibrated) | None |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

7 peer and 0 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 44; excluded: 0.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**opposite_b.docx**, cosine **0.9906**

`{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query:

> Revenue should pay for public buses rather than additional parking spaces. Drivers who cannot afford the charge should receive discounted transit passes

Source:

> Revenue should pay for additional parking spaces rather than public buses. Drivers who cannot afford the charge should not receive discounted transit passes


## Excluded material


## Peer evidence

### 1. opposite_b.docx | cosine 0.9906

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> Revenue should pay for public buses rather than additional parking spaces. Drivers who cannot afford the charge should receive discounted transit passes

Source passage:

> Revenue should pay for additional parking spaces rather than public buses. Drivers who cannot afford the charge should not receive discounted transit passes

### 2. opposite_b.docx | cosine 0.9820

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> The charge would reduce traffic and improve air quality. Revenue should pay for public buses rather than additional parking spaces

Source passage:

> The charge would not reduce traffic or improve air quality. Revenue should pay for additional parking spaces rather than public buses

### 3. opposite_b.docx | cosine 0.9755

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> The charge would reduce traffic and improve air quality. Revenue should pay for public buses rather than additional parking spaces. Drivers who cannot afford the charge should receive discounted transit passes

Source passage:

> The charge would not reduce traffic or improve air quality. Revenue should pay for additional parking spaces rather than public buses. Drivers who cannot afford the charge should not receive discounted transit passes

### 4. opposite_b.docx | cosine 0.9566

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> The city should introduce a congestion charge for private cars entering the centre. The charge would reduce traffic and improve air quality. Revenue should pay for public buses rather than additional parking spaces

Source passage:

> The city should not introduce a congestion charge for private cars entering the centre. The charge would not reduce traffic or improve air quality. Revenue should pay for additional parking spaces rather than public buses

### 5. opposite_b.docx | cosine 0.9452

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> The city should introduce a congestion charge for private cars entering the centre. The charge would reduce traffic and improve air quality. Revenue should pay for public buses rather than additional parking spaces. Drivers who cannot afford the charge should receive discounted transit passes

Source passage:

> The city should not introduce a congestion charge for private cars entering the centre. The charge would not reduce traffic or improve air quality. Revenue should pay for additional parking spaces rather than public buses. Drivers who cannot afford the charge should not receive discounted transit passes

### 6. opposite_b.docx | cosine 0.9095

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> The city should introduce a congestion charge for private cars entering the centre. The charge would reduce traffic and improve air quality

Source passage:

> The city should not introduce a congestion charge for private cars entering the centre. The charge would not reduce traffic or improve air quality

### 7. opposite_b.docx | cosine 0.8958

Location: `{"query_paragraphs": [1], "query_sections": ["Document body"], "matched_paragraphs": [1], "matched_sections": ["Document body"]}`

Query passage:

> The city should introduce a congestion charge for private cars entering the centre

Source passage:

> The city should not introduce a congestion charge for private cars entering the centre


## External evidence

No accepted evidence windows (or extraction unavailable).

## AI indicator

{
  "score": null,
  "status": "insufficient_text",
  "calibrated": false,
  "explanation": "Need at least 50 words and 3 sentences; no reliable inference for short clips."
}
