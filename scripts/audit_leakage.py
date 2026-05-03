"""CLI for leakage audit utilities."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.audits.leakage import run_leakage_audit


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Run leakage-audit utilities. Use --dry-run to validate input and "
            "show planned outputs without writing audit files."
        )
    )
    parser.add_argument("--input", required=True, help="Input dataset CSV path.")
    parser.add_argument("--output-dir", default="results/audits", help="Directory for audit outputs.")
    parser.add_argument("--sequence-col", default="sequence")
    parser.add_argument("--label-col", default="label")
    parser.add_argument("--source-col", default="source")
    parser.add_argument("--n-splits", type=int, default=5)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--kmer-size", type=int, default=3)
    parser.add_argument("--jaccard-threshold", type=float, default=0.8)
    parser.add_argument("--max-pairs", type=int, default=10000)
    parser.add_argument("--dry-run", action="store_true", help="Validate and report plan without writing outputs.")
    return parser.parse_args()


def main() -> None:
    """Run the leakage-audit CLI."""
    args = parse_args()
    summary = run_leakage_audit(
        input_path=args.input,
        output_dir=args.output_dir,
        sequence_col=args.sequence_col,
        label_col=args.label_col,
        source_col=args.source_col,
        n_splits=args.n_splits,
        random_state=args.random_state,
        kmer_size=args.kmer_size,
        jaccard_threshold=args.jaccard_threshold,
        max_pairs=args.max_pairs,
        dry_run=args.dry_run,
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

