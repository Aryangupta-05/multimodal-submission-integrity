# Evaluation

Measured locally on 4 November 2026 using the committed synthetic corpus, real PDF/DOCX extraction, FFmpeg decoding, Whisper tiny.en CPU int8 transcription and MiniLM embeddings. No mocks establish the ingestion/model/reporting results.

## Dataset and evaluation policy

The benchmark contains 15 submissions: 5 valid PDFs, 5 DOCX, 3 English TTS MP4s, 1 MP4 without an audio track, and 1 zero-byte PDF. The spoken clips are 20.965, 16.317 and 19.621 seconds before container resampling. The no-audio clip is 12 seconds. All content is synthetic and Codex-assisted; the garden document is explicitly labelled as the LLM example. Independent content does not imply human authorship. The manifest records source relationships, SHA256 hashes, media provenance and intended speech.

Ground truth: exactly five unordered positive peer pairs (PDF exact copy, two PDF/video relations involving that copy, clinic paraphrase pair, and external PDF/video pair). Every other pair among assessable files is negative. Configured common prompt text is legitimate shared material, not a positive relationship. Ground truth and intended transcripts are read only by generation/evaluation. Runtime uses no relationship labels or transcript substitution.

The **peer evaluation unit is an unordered assessable document pair**. A prediction is positive when either directional coverage is >=15%, based on windows with cosine >=0.80 and >=12 words per side. The 13 assessable inputs produce 78 pairs; the empty PDF and no-audio video are excluded from classification and evaluated separately as unavailable. Excluding them is not credit for true negatives.

The **external evaluation unit is one assessable document** against the separate local reference corpus. Only the external PDF and its spoken excerpt are labelled positive; all other 11 assessable files are negative. This evaluates the known local reference, not open-web recall. AI classification precision/recall is deliberately not reported: there are no verified human negatives or calibrated detector in this dataset.

Thresholds were chosen as a simple prototype operating point. This is a constructed development benchmark, with a dataset-informed retrieval fix. There is no held-out real-world accuracy claim, no confidence interval suggesting generalization, and no score-based misconduct decision.

## Measured results

| Task | Unit count | TP | FP | FN | TN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Peer relationships | 78 | 5 | 0 | 0 | 73 | 1.000 | 1.000 | 1.000 |
| Local external matches | 13 | 2 | 0 | 0 | 11 | 1.000 | 1.000 | 1.000 |

These perfect results apply only to this very small synthetic benchmark. Additional challenge results below show material limitations. Pair predictions and all denominators are in `evaluation/metrics.json`; rerun `python scripts/evaluate.py` after the root pipeline.

ASR word error rate compares **actual extracted transcript** to generation-only intended speech. Tokens are lowercase `\w+`; edit distance includes insertions, deletions and substitutions. Spelling differences count as errors. Punctuation is ignored. Word error rates do not measure timestamp accuracy.

| Clip | Reference words | Edit distance | WER |
|---|---:|---:|---:|
| 11_harbor_pitch.mp4 | 49 | 1 | 2.04% |
| 12_external_pitch.mp4 | 44 | 2 | 4.55% |
| 13_independent_pitch.mp4 | 50 | 1 | 2.00% |

Observed substitutions include “wait and shade” for “wait in shade” and “by” for “buy”. Word alignment corrected out-of-bounds ASR segment timing but omitted a word in one transcript. The speech is clean local TTS; these low WERs are not evidence of robustness to real accents, noise or long recordings.

## Five required scenarios

| Scenario | Actual evidence | Outcome |
|---|---|---|
| Cross-modal duplication | `11_harbor_pitch.mp4` retrieves `01_harbor.pdf` page 2. First exact sentence maps to ASR 00:00:00.000-00:00:04.720. Both raw passages and spans are in the JSON/Markdown. | Pass on constructed case |
| Semantic paraphrase | Clinic DOCX pair uses distinct wording; accepted cosine exceeds 0.80 with low lexical Jaccard. Paragraph ordinals are present and no page numbers are invented. | Pass on constructed case |
| Empty/corrupt/no audio | Zero-byte PDF is `empty`; silent video is `no_audio`; scores are null, while 13 other files remain assessable. Challenge corrupt PDF/MP4/DOCX also return unavailable reports. | Pass |
| Common formatting | Five files share the same 151-word prompt, which is visible in exclusions. All five have 0% peer coverage on their independent answers. Separate prompt+copied-answer challenge still has 100% matching answer coverage. | Pass on configured and challenge cases |
| Mixed-format batch | All 15 inputs receive JSON and Markdown, directional coverage/cosine matrices, extraction/index artifacts and a batch summary. | Pass |

Prompt-only input is unable to assess after exclusions rather than a fabricated zero score. A muted audio stream is `silent`, distinct from the absent-track sample. Blank/scanned PDFs are `unextractable`; partial PDF extraction assesses only the text-bearing page and records an OCR warning. Unsupported files receive a per-input report. Tests verify self exclusion by identity while separate identical files remain matches.

## Observed failures and ambiguities

### 1. Short external excerpt diluted by context and page furniture (fixed on this corpus)

The initial real run missed the external PDF/video peer relation and both external positives. Its peer confusion was TP=4, FN=1; external TP=0, FN=2. Initial PDF-to-video maximum cosine was 0.628991 and PDF-to-reference maximum was about 0.7121, below 0.80 despite intended copied content. Single-page institutional margins remained in the text and fixed windows embedded mismatched amounts of context.

The fix added configured margin removal for this institutional template and sentence-aligned evidence groups alongside the main 220-piece chunks. Final metrics above improve without lowering the threshold. `evaluation/baseline/` retains the original summary/matrices and `baseline_metrics.json` computes the original outcome. This was a development-set-informed fix, not an independent generalization result. Test unknown headers, multi-column layouts and shorter natural excerpts before broad deployment. A future lexical exact-span channel could complement semantic retrieval.

### 2. ASR timestamps beyond the clip duration (fixed bounds, residual transcription error)

Before word alignment, the harbor clip's final segment ended at **23.48 s** although decoded audio lasted **20.991 s**. The astronomy clip ended at **22.72 s** against roughly **19.64 s** of decoded audio. The first integration test failed on this invalid citation. Raw evidence is saved in `evaluation/observed_asr_timing_before_fix.json`.

Enabled Whisper word timestamps and retained raw predictions. Reported segment bounds are now constrained to real media duration, and invalid out-of-range segments would be dropped with a warning. Word-aligned harbor output ends at 20.14 s. The content still loses “pause”, so improved bounds do not prove a perfect transcript. The current test establishes valid bounds and source locations, not human-annotated per-word timing accuracy. A stronger system would benchmark forced alignment against manually annotated speech and assess alternate ASR on difficult clips.

### 3. Opposite conclusions remain semantically similar (unresolved ambiguity)

`opposite_a.docx` recommends a congestion charge; `opposite_b.docx` uses closely related wording but rejects it. Maximum cosine is **0.990573**, with **100.0% / 100.0%** coverage. These are deliberately mirrored diagnostic propositions, so this is not labelled an independently authored true negative or added to the main confusion matrix. It demonstrates that high similarity does not imply agreement or copying provenance.

Likely cause: sentence embeddings emphasize shared subject and wording more than polarity. Proposed improvement: present contradiction/negation cues, rerank with an open entailment/contradiction model, and keep human review. Do not silently discard contradictory copied language: a person may copy a paragraph and change “not”. The safe interpretation remains candidate relatedness.

### 4. Ten-word literal copied phrase missed (unresolved false negative)

`short_copy_a.docx` and `short_copy_b.docx` share “Copper lanterns guide midnight ferries across the frozen estuary.” Their longer surrounding paragraphs concern different subjects. Observed maximum cosine is **0.763941**, with **0.0% / 0.0%** accepted coverage. The exact sentence is below the twelve-word evidence minimum; larger windows dilute it. This is a real diagnostic miss excluded from the benchmark's five labelled relations, not a passed test disguised as model accuracy.

A proposed exact n-gram span channel with low-frequency filtering and separate short-quote reporting could recover it. Lowering the semantic threshold globally would increase common-jargon false positives. The current code intentionally documents this limit rather than tailoring away the challenge failure.

## Verification evidence

`tests/test_integrity.py` validates the required report keys, all raw passage/offset reconstruction, fresh PDF/DOCX extraction consistency, actual model context limits/vector norms, video decode/audio presence, copied-file identity, page 2/timestamp bounds, semantic paraphrases, coverage unions, external separation/provenance, AI uncertainty, boilerplate and copied residual answers, null unavailable scores, and diagnostic statuses. No ingestion/model mocks are used. See `evaluation/test_results.txt` for the final executed result and `evaluation/clean_environment.md` for the clean setup/run check.

All five DOCX sample pages and all distinct valid PDF pages were rendered and visually inspected; the exact PDF duplicate is byte-identical. The packaged DOCX renderer was attempted but had no LibreOffice executable on Windows; installed Microsoft Word exported PDF/PNG for visual QA. This rendering is unrelated to runtime DOCX extraction, which uses paragraph XML, not Word pagination.

## Runtime and resources

Final development run: **25.3875 seconds wall time**, **57.5938 main-process CPU seconds**, **747.03 MiB peak Python working set**. There were 16 main chunks and 478 total indexed windows (including sentence evidence and local references). Hardware: 12 logical CPUs, 7.31 GiB physical RAM; AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD. Configuration bounds PyTorch/ASR CPU work to four threads. Both models were local; embeddings could use the content-addressed cache. Every run still extracts documents and performs real ASR; there is no transcript cache. Python CPU/memory figures do not sum FFmpeg subprocess resources and are not a whole-machine peak.

The initial run took 33.561 s at 745.75 MiB peak with model startup and uncached embeddings. Later runs differ in extraction settings/window counts and cache state, so the difference is not a controlled speed comparison. Setup/download time and installed dependency footprint are separate from runtime. The clean verification records another real run. All 10,000-document rates/costs in README are explicitly planning assumptions; no production throughput was measured.

## Trade-offs and remaining validation

MiniLM (384 dimensions, 256-token context) and int8 tiny Whisper keep CPU/RAM modest. They trade contextual nuance and ASR robustness for low resource use. NumPy Flat search is exact, easy to inspect and reproducible at this scale, but quadratic in windows; sentence evidence expands the index considerably. HNSW with exact reranking and tenant/challenge metadata filters is the production option described in README.

Remaining limits include no OCR, English-only ASR, narrow reference/quotation syntax, template-discovery risk for coordinated copied openings, context-based overcoverage, short-copy misses, approximate ASR timestamps, uncalibrated AI indicators, and no human/held-out natural submissions. Reported evidence is suitable for inspection, not automated sanctions.
