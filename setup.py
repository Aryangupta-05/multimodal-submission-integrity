"""Single-command setup; creates a local venv, pins dependencies, fetches models."""

import argparse
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-install", action="store_true", help="Only fetch models using this interpreter"
    )
    args = parser.parse_args()
    if sys.version_info < (3, 11) or sys.version_info >= (3, 13):
        raise SystemExit("Use Python 3.11-3.12; tested with Python 3.11 on Windows x64.")
    if args.skip_install:
        interpreter = Path(sys.executable)
    else:
        target = ROOT / ".venv"
        if not target.exists():
            venv.EnvBuilder(with_pip=True).create(target)
        interpreter = target / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
        subprocess.run(
            [str(interpreter), "-m", "pip", "install", "-r", str(ROOT / "requirements-lock.txt")],
            check=True,
        )
        subprocess.run([str(interpreter), "-m", "pip", "check"], check=True)
    subprocess.run([str(interpreter), str(ROOT / "scripts/download_models.py")], check=True)
    print(
        "Setup complete. Activate .venv (Windows: .venv\\Scripts\\Activate.ps1; Linux: source .venv/bin/activate)."
    )
    print(
        "Then: python run_integrity_check.py --input_dir ./sample_submissions --output_dir ./reports"
    )


if __name__ == "__main__":
    main()
