"""Download public model snapshots by immutable commit; no API key required."""

import json
from pathlib import Path
from huggingface_hub import snapshot_download

ROOT = Path(__file__).resolve().parents[1]


def main():
    config = json.loads((ROOT / "config.json").read_text())
    for kind, path in [("embedding", "embedding_model_path"), ("asr", "asr_model_path")]:
        revision = config[kind + "_revision"]
        if revision == "pending":
            raise ValueError("Pin ASR model revision before release")
        snapshot_download(
            repo_id=config[kind + "_model"],
            revision=revision,
            local_dir=ROOT / config[path],
            ignore_patterns=[
                "onnx/*",
                "openvino/*",
                "*.h5",
                "*.msgpack",
                "rust_model.ot",
                "pytorch_model.bin",
            ]
            if kind == "embedding"
            else None,
        )
        print(f"Ready: {kind} {revision}")


if __name__ == "__main__":
    main()
