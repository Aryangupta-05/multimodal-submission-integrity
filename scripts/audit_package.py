"""Inspect only Git-tracked deliverables; never read credential stores."""

import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    names = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    names = [name for name in names if name]
    issues = []
    total = 0
    patterns = [
        r"gh[pousr]_[A-Za-z0-9]{30,}",
        r"sk-[A-Za-z0-9]{30,}",
        r"AKIA[A-Z0-9]{16}",
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    ]
    binaries = {".pdf", ".docx", ".mp4", ".npz", ".png"}
    for name in names:
        path = ROOT / name
        total += path.stat().st_size
        if any(
            part in {".models", ".venv", ".cache", "__pycache__", ".env", "venv"}
            for part in path.relative_to(ROOT).parts
        ):
            issues.append({"path": name, "issue": "environment/cache/credential path"})
        if path.suffix in {".safetensors", ".pt", ".bin", ".onnx"}:
            issues.append({"path": name, "issue": "unnecessary model weights"})
        if path.suffix in binaries:
            staged = subprocess.check_output(["git", "show", ":" + name], cwd=ROOT)
            if staged != path.read_bytes():
                issues.append(
                    {
                        "path": name,
                        "issue": "binary Git content differs from evaluated working bytes",
                    }
                )
        else:
            content = path.read_text(encoding="utf-8-sig", errors="replace")
            if any(re.search(pattern, content) for pattern in patterns):
                issues.append(
                    {
                        "path": name,
                        "issue": "possible credential pattern; inspect without printing value",
                    }
                )
    result = {
        "tracked_files": len(names),
        "total_bytes": total,
        "issues": issues,
        "scope": "Known credential-pattern/path scan and binary-byte verification, not a guarantee of detecting every possible secret.",
    }
    (ROOT / "evaluation/package_audit.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
