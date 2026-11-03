# Integrity audit: 11_harbor_pitch.mp4

Review priority: **HIGH**
Extraction: `ok`; assessable: `True`.

| Signal | Value |
|---|---:|
| Peer candidate coverage | 100.0 |
| External candidate coverage | 0.0 |
| AI style indicator (uncalibrated) | None |

> Null means unable to assess, not zero overlap. Coverage is not proof of plagiarism. AI indicator is not a calibrated probability.

16 peer and 0 external evidence windows above cosine 0.8. Review exact source spans before any conclusion. AI style index is uncalibrated.

## Extraction and scoring

Eligible words: 48; excluded: 0.
100 * union of query word positions in accepted windows / eligible query words
Coverage of candidate semantic windows; can include unmatched context. Not percentage proven plagiarized. Peer and external percentages are separate, not additive.

## Quick review

Strongest evidence per source (up to three); all accepted windows follow below.

**01_harbor.pdf**, cosine **1.0000**

`{"query_timestamp": "00:00:00.000 - 00:00:04.720", "query_start_seconds": 0.0, "query_end_seconds": 4.72, "matched_page": 2, "matched_pages": [2]}`

Query:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source:

> The harbor cooperative should repair its cold storage before buying another delivery truck

**02_harbor_copy.pdf**, cosine **1.0000**

`{"query_timestamp": "00:00:00.000 - 00:00:04.720", "query_start_seconds": 0.0, "query_end_seconds": 4.72, "matched_page": 2, "matched_pages": [2]}`

Query:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source:

> The harbor cooperative should repair its cold storage before buying another delivery truck

- Warning: ASR passages are model transcripts, not verified verbatim speech; timestamps have segment resolution.

## Excluded material


## Peer evidence

### 1. 01_harbor.pdf | cosine 1.0000

Location: `{"query_timestamp": "00:00:00.000 - 00:00:04.720", "query_start_seconds": 0.0, "query_end_seconds": 4.72, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

### 2. 01_harbor.pdf | cosine 1.0000

Location: `{"query_timestamp": "00:00:05.800 - 00:00:16.700", "query_start_seconds": 5.8, "query_end_seconds": 16.7, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

### 3. 01_harbor.pdf | cosine 0.9968

Location: `{"query_timestamp": "00:00:05.800 - 00:00:20.140", "query_start_seconds": 5.8, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 4. 01_harbor.pdf | cosine 0.9965

Location: `{"query_timestamp": "00:00:05.800 - 00:00:20.140", "query_start_seconds": 5.8, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 5. 01_harbor.pdf | cosine 0.9918

Location: `{"query_timestamp": "00:00:11.540 - 00:00:20.140", "query_start_seconds": 11.54, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 6. 01_harbor.pdf | cosine 0.9894

Location: `{"query_timestamp": "00:00:00.000 - 00:00:11.540", "query_start_seconds": 0.0, "query_end_seconds": 11.54, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

### 7. 01_harbor.pdf | cosine 0.9847

Location: `{"query_timestamp": "00:00:00.000 - 00:00:20.140", "query_start_seconds": 0.0, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 8. 01_harbor.pdf | cosine 0.9827

Location: `{"query_timestamp": "00:00:00.000 - 00:00:16.700", "query_start_seconds": 0.0, "query_end_seconds": 16.7, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

### 9. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_timestamp": "00:00:00.000 - 00:00:04.720", "query_start_seconds": 0.0, "query_end_seconds": 4.72, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck

### 10. 02_harbor_copy.pdf | cosine 1.0000

Location: `{"query_timestamp": "00:00:05.800 - 00:00:16.700", "query_start_seconds": 5.8, "query_end_seconds": 16.7, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch

### 11. 02_harbor_copy.pdf | cosine 0.9968

Location: `{"query_timestamp": "00:00:05.800 - 00:00:20.140", "query_start_seconds": 5.8, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 12. 02_harbor_copy.pdf | cosine 0.9965

Location: `{"query_timestamp": "00:00:05.800 - 00:00:20.140", "query_start_seconds": 5.8, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 13. 02_harbor_copy.pdf | cosine 0.9918

Location: `{"query_timestamp": "00:00:11.540 - 00:00:20.140", "query_start_seconds": 11.54, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 14. 02_harbor_copy.pdf | cosine 0.9894

Location: `{"query_timestamp": "00:00:00.000 - 00:00:11.540", "query_start_seconds": 0.0, "query_end_seconds": 11.54, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice

### 15. 02_harbor_copy.pdf | cosine 0.9847

Location: `{"query_timestamp": "00:00:00.000 - 00:00:20.140", "query_start_seconds": 0.0, "query_end_seconds": 20.14, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch. We would measure discarded kilograms each morning and
> expansion until spoilage falls for four consecutive weeks

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch. We would measure discarded kilograms each morning and pause
> expansion until spoilage falls for four consecutive weeks

### 16. 02_harbor_copy.pdf | cosine 0.9827

Location: `{"query_timestamp": "00:00:00.000 - 00:00:16.700", "query_start_seconds": 0.0, "query_end_seconds": 16.7, "matched_page": 2, "matched_pages": [2]}`

Query passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck
> Fish currently spoil while drivers wait for ice. A shared maintenance schedule and insulated
> crates would protect the catch

Source passage:

> The harbor cooperative should repair its cold storage before buying another delivery truck. Fish
> currently spoil while drivers wait for ice. A shared maintenance schedule and insulated crates
> would protect the catch


## External evidence

No accepted evidence windows (or extraction unavailable).

## AI indicator

{
  "score": null,
  "status": "insufficient_text",
  "calibrated": false,
  "explanation": "Need at least 50 words and 3 sentences; no reliable inference for short clips."
}
