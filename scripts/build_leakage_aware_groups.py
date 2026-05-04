"""CLI for leakage-aware grouping utilities."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_signal_ml.audits.grouping import (
    assess_source_group_feasibility,
    build_combined_similarity_groups,
    build_exact_duplicate_groups,
    build_kmer_jaccard_groups,
    build_near_duplicate_graph_groups,
    export_group_assignments,
    summarize_grouping,
    write_grouping_summary,
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Build leakage-aware sequence group assignments. Use --dry-run to "
            "summarize assignments and planned outputs without writing files."
        )
    )
    parser.add_argument(
        "--input",
        default="data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv",
        help="Input dataset CSV path.",
    )
    parser.add_argument("--output-dir", default="results/sensitivity", help="Directory for future outputs.")
    parser.add_argument("--sequence-col", default="sequence")
    parser.add_argument("--source-col", default="source")
    parser.add_argument("--method", choices=["exact", "near", "kmer", "combined"], default="combined")
    parser.add_argument("--edit-distance-threshold", type=int, default=1)
    parser.add_argument("--kmer-size", type=int, default=3)
    parser.add_argument("--jaccard-threshold", type=float, default=0.8)
    parser.add_argument("--max-pairs", type=int, default=10000)
    parser.add_argument("--dry-run", action="store_true", help="Report plan without writing outputs.")
    return parser.parse_args()


def build_groups(args: argparse.Namespace, frame: pd.DataFrame) -> pd.DataFrame:
    """Dispatch grouping method."""
    if args.method == "exact":
        return build_exact_duplicate_groups(frame, sequence_col=args.sequence_col)
    if args.method == "near":
        return build_near_duplicate_graph_groups(
            frame,
            sequence_col=args.sequence_col,
            max_distance=args.edit_distance_threshold,
            max_pairs=args.max_pairs,
        )
    if args.method == "kmer":
        return build_kmer_jaccard_groups(
            frame,
            sequence_col=args.sequence_col,
            k=args.kmer_size,
            threshold=args.jaccard_threshold,
            max_pairs=args.max_pairs,
        )
    return build_combined_similarity_groups(
        frame,
        sequence_col=args.sequence_col,
        edit_distance_threshold=args.edit_distance_threshold,
        k=args.kmer_size,
        jaccard_threshold=args.jaccard_threshold,
        max_pairs=args.max_pairs,
    )


def main() -> None:
    """Run the grouping CLI."""
    args = parse_args()
    frame = pd.read_csv(args.input)
    group_df = build_groups(args, frame)
    output_dir = Path(args.output_dir)
    assignments_path = output_dir / f"group_assignments_{args.method}.csv"
    summary_path = output_dir / f"grouping_summary_{args.method}.json"

    summary = summarize_grouping(group_df)
    summary.update(
        {
            "dry_run": bool(args.dry_run),
            "input_path": str(args.input),
            "method": args.method,
            "planned_outputs": [str(assignments_path), str(summary_path)],
            "outputs_written": [],
            "source_group_feasibility": assess_source_group_feasibility(frame, source_col=args.source_col),
        }
    )

    if not args.dry_run:
        export_group_assignments(group_df, assignments_path)
        summary["outputs_written"] = [str(assignments_path), str(summary_path)]
        write_grouping_summary(summary, summary_path)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
