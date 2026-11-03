# Requirements traceability

Source: AI Engineer Assignment.pdf, 10 pages, read in full. User adds stricter reproducibility and edge-case requirements. Final audit below maps every requirement to actual implementation and verification; external/user-only handoff items are explicit.

| ID | Requirement and PDF pages | Implementation / evidence | Status |
|---|---|---|---|
| R01 | PDF extraction, true pages (2) | integrity/extractors.py; fresh parser/page and passage-span tests | PASS |
| R02 | DOCX extraction, honest paragraph/section refs (2) | Body/table paragraph ordinals and latest section heading; no DOCX pages; tests | PASS |
| R03 | MP4 audio and real open ASR with timestamps (2,4,9) | Real faster-whisper tiny.en CPU int8 with word alignment; 3 actual video transcripts | PASS |
| R04 | Whitespace, headers/footers, 200-400-token chunks with overlap, reversible references (2) | Raw offsets + normalized window text; 220 WordPiece chunks with overlap; context/offset tests | PASS |
| R05 | Robust malformed, empty, scanned, silent, unreadable, unsupported handling (2,4,9) | 15 main + 16 challenge files; malformed/empty/blank/scanned/muted/unsupported/partial statuses | PASS |
| R06 | Dense lightweight embeddings and vector index (2) | MiniLM normalized 384-d vectors; NumPy exact cosine; actual model/vector tests | PASS |
| R07 | Cross-document peer score, identity-based self exclusion, duplicate files (2,8) | Document-path self filter; identical PDF duplicate retained; tests | PASS |
| R08 | Reproducible AI signal with uncertainty and required field (3,10) | signals.py deterministic style index, null short texts, calibrated=false; AI never raises risk alone | PASS |
| R09 | Separated local external reference corpus and source provenance (3) | Separate reference namespace; CC0 synthetic local source with URL/provenance; external TP2/TN11 | PASS |
| R10 | Distinct scores and example JSON keys (3,5-6) | report_schema.json; JSON schema validated for all 15 main reports | PASS |
| R11 | Exact passages, scores and verifiable PDF/video/DOCX locations (3,6) | Every passage reconstructed from exact raw spans; fresh parser agreement; bounded ASR refs | PASS |
| R12 | Scenario 1 PDF/video match (4) | Harbor pitch -> source PDF page 2; first sentence 0.000-4.720 seconds; tested | PASS |
| R13 | Scenario 2 semantic paraphrase >0.80 (4) | Clinic DOCX max cosine 0.881572; paired Jaccard 0.1538; actual paragraphs | PASS |
| R14 | Scenario 3 corrupt PDF and silent MP4 (4) | 15_empty.pdf empty; 14_silent.mp4 no_audio; null scores; other 13 assessed | PASS |
| R15 | Scenario 4 five 150-word prompts, independent answers (4) | 151 prompt words excluded in five files, 0% residual peer; copied-answer challenge 100% | PASS |
| R16 | Scenario 5 mixed 10-20 batch, matrix, reports (4-5) | 15 main inputs; 30 individual report files; aggregate coverage/cosine matrices and summary | PASS |
| R17 | Root CLI command, modular source, JSON+MD each (5,7,9) | Root CLI and modular integrity package; required command executed on actual files | PASS |
| R18 | >=5 valid PDFs, >=5 DOCX, 2-3 spoken 10-30s videos (6) | 5 valid PDFs + 5 DOCX + spoken 20.965/16.317/19.621s + silent + empty =15 | PASS |
| R19 | Exact copy, crossmodal, paraphrase, LLM label, independent, degraded (6-7) | Manifest: 5 positive peer pairs, 2 external positives, independent answers, LLM-labelled sample | PASS |
| R20 | Synthetic/licensed data and manifest committed (7) | All synthetic Codex-assisted CC0; no private student material; generation script and SHA256 manifest | PASS |
| R21 | Dependencies, model download scripts, config (7) | Pinned requirements + full lock + immutable model snapshots; config and setup scripts | PASS |
| R22 | Precision/recall/F1/confusion, documented ground truth (7-8) | evaluation/metrics.json: peer TP5 TN73; external TP2 TN11; precision/recall/F1=1 on constructed benchmark | PASS |
| R23 | >=2 actual failures/ambiguities investigated (7) | Actual baseline retrieval miss and invalid timestamps fixed; opposite-conclusion ambiguity and short-copy miss remain documented | PASS |
| R24 | Model/index tradeoffs and resource/runtime measurements (7) | Measured runtime/CPU/peak working set in batch JSON and EVALUATION; model/index tradeoffs | PASS |
| R25 | 10k architecture: queue, CPU/GPU, HNSW/Flat, cost/throughput/latency (3,7) | README queue/bounded workers, CPU/GPU, HNSW/Flat, object store, caches, retries/idempotency, explicit estimates | PASS |
| R26 | Single-command setup, root run, clean environment (7,9) | python setup.py; fresh checkout and venv; actual model run identical; 25 tests + lint + pip check; regeneration verified | PASS |
| R27 | Accurate AI disclosure and explainability walkthrough (9) | AI_USE.md + README accurate largely AI-built disclosure; WALKTHROUGH.md | PASS |
| R28 | Private GitHub, full code/data/docs, commit hash (9) | Complete solution pushed to Aryangupta-05/multimodal-submission-integrity; privacy and remote commit verified; current hash via git rev-parse HEAD | PASS |
| R29 | Verified evaluator access (9) | invitation has no handle; pending identity | EXTERNAL BLOCKER |
| R30 | Portal submission URL/hash (9) | explicitly skipped by user; NEVER submit | USER HANDOFF |
| R31 | 72h receipt deadline, no invented date (9) | received 2026-11-03 17:16:47 IST => Nov 6 17:16:47 IST | VERIFIED |
| R32 | Coverage %, no cosine-as-plagiarism, overlap union, boilerplate/quotes/refs | Unique eligible-word union, channel separation, semantic context caveat; prompt/quote/reference exclusions; tests | PASS |
| R33 | Manifest labels not used at runtime, real ASR not transcript injection | Runtime never reads relationship labels/intended transcripts; real ASR/embeddings in all runs | PASS |
| R34 | Reproducible generation, sample videos playable, secret/model/env-free repo | All 15 hashes survive Git checkout; full generation rerun; PyAV audio/video decode; tracked package audit excludes secrets, weights and environments | PASS |
| R35 | Hourly scheduler, persistent checkpoints, concurrent-run guard | Hourly heartbeat configured with run-lock/thread-activity check, then PAUSED after independent preparation completed; persistent checkpoint retained | COMPLETE |
| R36 | AI rules: boilerplate/debugging allowed, broader use needs clarification | accurate disclosure; no authorship misrepresentation | HANDOFF |
