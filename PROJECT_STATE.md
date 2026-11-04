# Preparation checkpoint

The latest specification is **AI Engineer Assignment (2).pdf**, ten pages. The repository is **PUBLIC**, as required by its revised page 9 and explicitly authorized by the candidate. Source: https://github.com/Aryangupta-05/multimodal-submission-integrity.

The 5 November 2026 re-audit reran the actual multimodal pipeline, including an initially empty embedding cache, validated newly generated reports, cloned the public repository and checked the sample-file hashes. See `AUDIT_2026-11-05.md`, `evaluation/reaudit_2026-11-05.json` and `REQUIREMENTS.md` for exact evidence and outstanding user responsibilities. Original clean-environment and full dataset-regeneration evidence remains in `evaluation/clean_environment.md`.

Implemented: real PDF pages, DOCX paragraph/section/table references, FFmpeg/Whisper transcription with bounded timestamps, source-preserving normalization, overlapping chunks, MiniLM embeddings, exact vector search, self-match filtering, separate external corpus, reproducible uncertain AI indicator, coverage-based scores, per-file JSON/Markdown and aggregate matrices. The repository includes fifteen benchmark files, sixteen diagnostic cases, generators, pinned dependencies, model setup, evaluations and scaling/interview documentation.

Known model limitations, including contradictory statements with high cosine, short copied excerpts below the evidence floor, ASR errors and no OCR, are documented. The brief requires an honest working prototype and failure analysis; it does not establish perfect hidden-test accuracy or require measured production throughput for 10,000 submissions.

## Revised submission instructions

1. Submit the **public repository URL** by replying to the company's assessment email or using the candidate portal. Public access resolves the previous missing-reviewer-handle issue. The PDF does not provide a portal URL; email is an available route. A commit hash can identify the version but is no longer explicitly required by the revised submission bullet.
2. Complete all review and testing **before** submission. After submission, do not modify code, instructions or Markdown files.
3. Contact listed in the revised brief: `careers@unstop.com`. This agent has not contacted the hiring team or submitted the assessment; the candidate performs the final send/Submit action.

## Remaining external/user responsibilities

The README and AI_USE.md accurately disclose substantial AI assistance. The brief explicitly mentions boilerplate/debugging assistance; acceptance of broader assistance has not been established. The candidate must clarify that scope and be prepared to explain the architecture and code. This cannot be resolved through a fabricated independent-authorship statement or an agent declaring permission on the company's behalf.

The original invitation was received on 3 November 2026 at 17:16:47 IST. The revision arrived on 4 November 2026 at 10:48:57 IST and did not explicitly extend the deadline. Use the earlier original-receipt-derived deadline, **6 November 2026 at 17:16:47 IST**, unless the company confirms another deadline.

The hourly continuation automation remains paused; it does not promise ongoing background work. The workspace `work/PROGRESS.md` records audit/recovery state. Read the delivered commit with `git rev-parse HEAD`; the external submission handoff records its final full hash.

Reproduce: `python setup.py`, activate `.venv`, run `python run_integrity_check.py --input_dir ./sample_submissions --output_dir ./reports`, then `python -m pytest -q tests` and `python scripts/evaluate.py`. To inspect a different report run, use `--reports-dir=PATH` and `--challenge-reports-dir=PATH` with the tests.
