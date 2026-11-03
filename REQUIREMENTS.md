# Requirements traceability

Source: AI Engineer Assignment.pdf, 10 pages, read in full. User adds stricter reproducibility and edge-case requirements. Status starts TODO and will be audited against actual evidence.

| ID | Requirement and PDF pages | Implementation / evidence | Status |
|---|---|---|---|
| R01 | PDF extraction, true pages (2) | integrity/extractors.py; tests | TODO |
| R02 | DOCX extraction, honest paragraph/section refs (2) | integrity/extractors.py | TODO |
| R03 | MP4 audio and real open ASR with timestamps (2,4,9) | faster-whisper tiny.en; real reports | TODO |
| R04 | Whitespace, headers/footers, 200-400-token chunks with overlap, reversible references (2) | integrity/text.py; artifacts | TODO |
| R05 | Robust malformed, empty, scanned, silent, unreadable, unsupported handling (2,4,9) | extractors; edge suite | TODO |
| R06 | Dense lightweight embeddings and vector index (2) | MiniLM; NumPy Flat cosine | TODO |
| R07 | Cross-document peer score, identity-based self exclusion, duplicate files (2,8) | matching; tests | TODO |
| R08 | Reproducible AI signal with uncertainty and required field (3,10) | signals; reports | TODO |
| R09 | Separated local external reference corpus and source provenance (3) | reference_corpus; external reports | TODO |
| R10 | Distinct scores and example JSON keys (3,5-6) | report schema; validation | TODO |
| R11 | Exact passages, scores and verifiable PDF/video/DOCX locations (3,6) | provenance spans; accuracy audit | TODO |
| R12 | Scenario 1 PDF/video match (4) | evaluation | TODO |
| R13 | Scenario 2 semantic paraphrase >0.80 (4) | DOCX pair; evaluation | TODO |
| R14 | Scenario 3 corrupt PDF and silent MP4 (4) | dataset; evaluation | TODO |
| R15 | Scenario 4 five 150-word prompts, independent answers (4) | prompt exclusion and residual matching | TODO |
| R16 | Scenario 5 mixed 10-20 batch, matrix, reports (4-5) | 15 inputs; batch summary | TODO |
| R17 | Root CLI command, modular source, JSON+MD each (5,7,9) | run_integrity_check.py | TODO |
| R18 | >=5 valid PDFs, >=5 DOCX, 2-3 spoken 10-30s videos (6) | user target 5 PDF + 5 DOCX + 3 spoken + silent + empty =15 | TODO |
| R19 | Exact copy, crossmodal, paraphrase, LLM label, independent, degraded (6-7) | manifest and generation script | TODO |
| R20 | Synthetic/licensed data and manifest committed (7) | dataset generation; provenance | TODO |
| R21 | Dependencies, model download scripts, config (7) | requirements, setup scripts | TODO |
| R22 | Precision/recall/F1/confusion, documented ground truth (7-8) | EVALUATION.md + measured JSON | TODO |
| R23 | >=2 actual failures/ambiguities investigated (7) | additional challenge cases | TODO |
| R24 | Model/index tradeoffs and resource/runtime measurements (7) | benchmark; evaluation | TODO |
| R25 | 10k architecture: queue, CPU/GPU, HNSW/Flat, cost/throughput/latency (3,7) | README | TODO |
| R26 | Single-command setup, root run, clean environment (7,9) | setup.py and clean verification | TODO |
| R27 | Accurate AI disclosure and explainability walkthrough (9) | AI_USE.md, WALKTHROUGH.md | TODO |
| R28 | Private GitHub, full code/data/docs, commit hash (9) | repository verification | TODO |
| R29 | Verified evaluator access (9) | invitation has no handle; pending identity | EXTERNAL BLOCKER |
| R30 | Portal submission URL/hash (9) | explicitly skipped by user; NEVER submit | USER HANDOFF |
| R31 | 72h receipt deadline, no invented date (9) | received 2026-11-03 17:16:47 IST => Nov 6 17:16:47 IST | VERIFIED |
| R32 | Coverage %, no cosine-as-plagiarism, overlap union, boilerplate/quotes/refs | scoring docs; tests | TODO |
| R33 | Manifest labels not used at runtime, real ASR not transcript injection | source audit; real model logs | TODO |
| R34 | Reproducible generation, sample videos playable, secret/model/env-free repo | package audit | TODO |
| R35 | Hourly scheduler, persistent checkpoints, concurrent-run guard | heartbeat created; work/PROGRESS.md | ACTIVE |
| R36 | AI rules: boilerplate/debugging allowed, broader use needs clarification | accurate disclosure; no authorship misrepresentation | HANDOFF |
