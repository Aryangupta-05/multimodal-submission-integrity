"""Root CLI, intentionally free of dataset labels and expected transcripts."""

import argparse
import sys
from integrity.pipeline import load_config, run


def main():
    parser = argparse.ArgumentParser(
        description="Explainable multimodal integrity audit (local CPU models)."
    )
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--config", default=None)
    args = parser.parse_args()
    try:
        summary = run(args.input_dir, args.output_dir, load_config(args.config))
    except (ValueError, OSError, RuntimeError) as exc:
        print(
            f"Pipeline setup failed: {exc}\nRun python setup.py to install dependencies and download models.",
            file=sys.stderr,
        )
        return 2
    print(f"Completed {summary['documents']} files in {summary['runtime_seconds']:.2f}s.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
