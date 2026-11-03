"""Refresh human-readable reports from existing JSON without model inference."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from integrity.reporting import write_report

ROOT = Path(__file__).resolve().parents[1]
for folder in [ROOT / "reports/individual", ROOT / "challenge_reports/individual"]:
    for path in folder.glob("*.json"):
        write_report(json.loads(path.read_text(encoding="utf-8")), folder)
print("Markdown refreshed.")
