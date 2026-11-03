# Clean environment verification

Verified on 4 November 2026 on the same Windows x64 machine, using a fresh local Git checkout and a newly created Python 3.11 virtual environment without system site packages. This is a clean environment on the same machine, not a second OS or hardware validation.

Commands executed from the fresh repository root:

```powershell
python setup.py
.venv/Scripts/python.exe run_integrity_check.py --input_dir ./sample_submissions --output_dir ./reports_clean
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe -m ruff check .
.venv/Scripts/python.exe -m pip check
```

Setup completed successfully: all locked dependencies installed, pip reported no broken requirements, and both model snapshots downloaded successfully at the pinned immutable revisions. Public wheel/model caches were available; the virtual environment and local model directories began empty. No API key was required.

The real pipeline processed all 15 committed files in **38.4452 seconds**, with **60.9688 main-process CPU seconds** and **748.62 MiB peak Python working set**. All 15 sample hashes survived Git checkout unchanged. All 15 fresh reports had identical signal values, extraction statuses, risks, accepted match counts, passages and locations compared with the committed example reports. Maximum observed cosine difference was **0**. This comparison ignores runtime/resource measurements, which naturally vary.

The clean checkout passed **25 tests**, Ruff checks and pip dependency checks. Tests inspect committed artifacts and fresh parsers/models; the separately compared `reports_clean` run establishes the real ingestion/ASR/embedding/reporting path in the clean environment. Source code tested was commit `048bfb3b88602439a6eb565c24219b6c67b81126`; subsequent delivery changes are documentation/audit metadata only unless recorded otherwise. Machine-readable comparison is in `clean_reproduction.json`.

The prototype has not been independently executed on Linux/macOS or a second hardware platform. Optional Linux dataset regeneration requires espeak-ng; Windows-only dependencies have environment markers in the lock. No claim is made that TTS or DOCX ZIP bytes are identical across operating systems.

The full dataset generator was then executed in the disposable checkout using the pinned dependencies and the installed English SAPI voice. It generated all 15 inputs again, including three speech/audio MP4s of 20.965, 16.317 and 19.621 seconds. A real run over the regenerated files completed in 16.71 seconds (embedding cache warm, ASR still executed). The regenerated manifest's 15 hashes were valid; peer metrics again were TP5/TN73/FP0/FN0 and external metrics TP2/TN11/FP0/FN0. See `regeneration_verification.json`. This establishes content/relationship reproducibility on this machine; container metadata can differ, as documented.
