# Technical walkthrough

## A five minute demonstration

Run `python run_integrity_check.py --input_dir ./sample_submissions --output_dir ./reports`. Open `reports/batch_summary.md`, then `reports/individual/11_harbor_pitch.mp4.md`. Its first evidence card points to page 2 of `01_harbor.pdf` and an actual ASR time range in the video. Play the clip at that range and compare the PDF paragraph. Open the clinic DOCX report to show reworded arguments and paragraph references. Finally show the silent video and zero-byte PDF reports: their scores are null because there is nothing assessable.

## Follow one passage through the code

1. `Extractor.extract()` dispatches by format. PDF text units are real pages. DOCX units are body/table paragraphs tagged with the most recent heading. MP4 passes through FFmpeg to 16 kHz mono audio, then real Whisper tiny.en ASR. The runtime has no access to intended transcripts.
2. `normalize()` records each normalized word and its raw unit/character offsets. Raw text is never overwritten. `exclude_known()` and the conservative shared-prefix rule mark common prompts, explicit attributed quotations and references; those tokens remain visible in the audit.
3. `make_windows()` assembles eligible words into 220-model-piece chunks with overlap. Sentence and short evidence windows improve retrieval for a paragraph embedded inside a longer report. Each window retains token IDs and both raw and normalized text.
4. `Embedder.encode()` produces normalized 384-dimensional MiniLM vectors. The cache key includes model revision and normalized content. `cosine_matrix()` is the exact Flat index: normalized dot products equal cosine.
5. `find_matches()` filters out the same document ID, not the same content hash. Thus another file containing identical bytes still matches. External references are a separate namespace. For each query window/source file, retain the strongest accepted source window at cosine >=0.80 with at least 12 words on each side.
6. `coverage()` unions query token IDs across accepted windows. This prevents overlapping windows or multiple sources from counting the same word twice. It reports candidate semantic-window coverage, which is broader than proven literal copying.
7. `make_report()` combines separate peer/external coverage and an uncertain style signal. The reporter slices raw text using offsets, attaches all constituent locations, and writes schema-compatible JSON and Markdown. HIGH is a review priority, not a verdict.

## Decisions to be able to explain

**Why MiniLM and Whisper tiny?** They fit commodity CPU/RAM, have public checkpoints and require no inference billing. MiniLM is useful for semantic retrieval and tiny Whisper integrates short speech without a large model. Both have limitations: negation is difficult for the embedding model, and ASR can substitute words or drift in timestamps. Models are pinned by commit and run locally.

**Why NumPy instead of a vector database?** The evaluated corpus has only hundreds of windows. Exact matrix multiplication is simple to inspect and repeat, and the brief explicitly permits it. It becomes quadratic in windows; the 10,000-document plan uses filtered HNSW candidates plus exact reranking and a durable metadata store.

**Why not 300 words per chunk?** Words and model tokens differ. MiniLM has a 256-token context; 300 words would truncate. The main 220-piece budget leaves room for special tokens. Short evidence windows supplement the main chunks without pretending they are the required 200-400-token ingestion chunks.

**What does 100% coverage mean?** All eligible query word positions lie inside accepted semantic windows. It does not establish that every word was copied, that attribution is absent, or who copied whom. An embedded shorter passage can mark neighbouring context. The percentage is an explicit review aid; cosine is only a retrieval criterion.

**How are DOCX pages handled?** They are not invented. DOCX XML contains paragraph structure but no reliable rendered pagination. The report gives body paragraph ordinals, section heading text and table coordinates where available. PDF references are actual container pages.

**How can a reviewer verify source accuracy?** Each match contains exact query/source text, `*_spans` with unit and character offsets, token IDs, and readable locations. `tests/test_integrity.py` reconstructs every reported passage, compares fresh PDF/DOCX extraction against saved units, checks page/timestamp bounds, and recomputes coverage unions. ASR text remains a model transcript with uncertainty, not ground-truth speech.

**What prevents a shared prompt from dominating?** Known prompt tokens are excluded before embedding and from the denominator. Automatic discovery is restricted to a long repeated opening prefix shared by five files. A separate challenge demonstrates that copied answers following the prompt still match. Coordinated copied openings can resemble templates, so exclusions must remain reviewable.

**Is the AI score a probability?** No. The required field name is preserved, but the number is a weighted style index. There is no labelled human validation or calibration. It must not establish misconduct and does not raise risk by itself.

**What did testing actually establish?** The committed small synthetic corpus and additional diagnostics ran through real extraction, ASR, embeddings and reporting. See EVALUATION.md for exact measured confusion matrices. Synthetic/TTS results and dataset-informed fixes do not establish natural-submission accuracy. Challenge cases expose both high similarity despite opposite conclusions and a missed short copy.

## Useful experiments before an interview

Change `semantic_threshold` in a copy of `config.json`, run with `--config`, and inspect new false positives/misses. Add an independent file with similar terminology. Put a copied paragraph after a different introduction. Inspect the query/source token union instead of relying on the headline percentage. Use `reports/index_windows.json` to compare the main-chunk role and sentence-evidence role. Explain which components would need recalibration on a held-out real dataset.

Be candid about AI use: Codex built most of this project. Review the source, reproduce the commands and ask the evaluator whether the disclosed assistance is acceptable before presenting it as your assessment solution.
