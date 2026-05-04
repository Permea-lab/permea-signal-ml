"""CLI for leakage-aware split manifest generation."""

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

from permea_signal_ml.audits.splits import (
    assign_group_stratified_folds,
    attach_labels_to_groups,
    build_split_manifest,
    export_split_manifest,
    load_group_assignments,
    summarize_groups_for_splitting,
    summarize_split_manifest,
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Generate leakage-aware split manifests from group assignments. "
            "Use --dry-run to summarize planned outputs without writing files."
        )
    )
    parser.add_argument(
        "--input",
        default="data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv",
        help="Input dataset CSV path.",
    )
    parser.add_argument(
        "--groups",
        default="results/sensitivity/group_assignments_combined.csv",
        help="Group assignment CSV path.",
    )
    parser.add_argument("--output-dir", default="results/sensitivity", help="Output directory.")
    parser.add_argument("--label-col", default="label")
    parser.add_argument("--sequence-id-col", default="sequence_id")
    parser.add_argument("--n-splits", type=int, default=5)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true", help="Report plan without writing files.")
    return parser.parse_args()


def main() -> None:
    """Build a split manifest or dry-run summary."""
    args = parse_args()
    dataset = pd.read_csv(args.input)
    groups = load_group_assignments(args.groups)
    groups_with_labels = attach_labels_to_groups(dataset, groups, label_col=args.label_col)
    group_summary = summarize_groups_for_splitting(groups_with_labels, label_col=args.label_col)
    group_to_fold = assign_group_stratified_folds(
        group_summary,
        n_splits=args.n_splits,
        random_state=args.random_state,
    )
    split_manifest = build_split_manifest(
        dataset,
        groups,
        group_to_fold,
        label_col=args.label_col,
        sequence_id_col=args.sequence_id_col,
    )
    summary = summarize_split_manifest(split_manifest, label_col="label")
    output_dir = Path(args.output_dir)
    manifest_path = output_dir / "combined_group_stratified_split_manifest.csv"
    summary_path = output_dir / "combined_group_stratified_split_summary.json"
    summary.update(
        {
            "dry_run": bool(args.dry_run),
            "input_path": str(args.input),
            "group_assignment_path": str(args.groups),
            "split_policy": "leakage_aware_group_stratified",
            "n_splits_requested": int(args.n_splits),
            "random_state": int(args.random_state),
            "planned_outputs": [str(manifest_path), str(summary_path)],
            "outputs_written": [],
        }
    )

    if not args.dry_run:
        summary["outputs_written"] = [str(manifest_path), str(summary_path)]
        export_split_manifest(split_manifest, summary, output_dir)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
