# Leakage-Aware Grouping Utilities v0.1

## Purpose

This document describes the leakage-aware grouping utilities implemented for future benchmark sensitivity analysis.

The utilities build sequence group assignments for exact duplicates, edit-distance near duplicates, k-mer Jaccard similarity groups, and combined similarity groups. They do not create leakage-aware fold manifests, do not train models, do not generate leakage-aware metrics, do not update manuscript claims, and do not establish that the benchmark is leakage-free.

Public preprint status remains **Hold / not submission-ready**.

## Implemented Utilities

Code location:

- `src/permea_signal_ml/audits/grouping.py`

Implemented functions:

- `normalize_sequence_for_grouping(seq)` normalizes sequence strings for grouping.
- `build_exact_duplicate_groups(df, sequence_col="sequence")` assigns rows to identical-normalized-sequence groups.
- `edit_distance(a, b, max_distance=None)` exposes the standard-library edit-distance helper for grouping use.
- `build_near_duplicate_graph_groups(df, sequence_col="sequence", max_distance=1, max_pairs=None)` assigns connected components from edit-distance edges.
- `kmer_set(seq, k)` returns k-mer sets.
- `jaccard_similarity(a, b)` computes Jaccard similarity.
- `build_kmer_jaccard_groups(df, sequence_col="sequence", k=3, threshold=0.8, max_pairs=None)` assigns connected components from k-mer similarity edges.
- `build_combined_similarity_groups(df, sequence_col="sequence", edit_distance_threshold=1, k=3, jaccard_threshold=0.8, max_pairs=None)` combines exact duplicate, edit-distance, and k-mer Jaccard edges.
- `summarize_grouping(group_df)` summarizes assignment counts, group counts, singleton groups, non-singleton groups, largest group size, method, and caveats.
- `assess_source_group_feasibility(df, source_col="source")` reports whether source-aware group splitting is feasible from the available source column.
- `export_group_assignments(group_df, output_path)` writes group assignments only when explicitly called.

## Command-Line Utility

CLI location:

- `scripts/build_leakage_aware_groups.py`

Dry-run example:

```bash
python3 scripts/build_leakage_aware_groups.py \
  --input data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv \
  --output-dir results/sensitivity \
  --method combined \
  --dry-run
```

Dry-run mode loads the dataset, builds group assignments in memory, prints a JSON summary, prints planned output paths, and writes no files.

Future non-dry-run example:

```bash
python3 scripts/build_leakage_aware_groups.py \
  --input data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv \
  --output-dir results/sensitivity \
  --method combined
```

Non-dry-run mode is intended for a future approved task. It would write group assignments and a grouping summary JSON under the selected output directory. It does not train models or compute benchmark performance metrics.

## Expected Future Outputs

Future approved tasks may create:

- `results/sensitivity/group_assignments_combined.csv`
- `results/sensitivity/grouping_summary_combined.json`
- leakage-aware split manifests
- leakage-aware baseline metric tables
- random-stratified versus leakage-aware delta tables
- a human-readable leakage-aware sensitivity report

These outputs are not created by this documentation task unless the CLI is explicitly run without `--dry-run` in a later approved task.

## Source/Group Feasibility

The current rerun-ready dataset includes a `source` column, but the known value is `legacy_bbb_import`. That source field is too coarse for source-aware group split control. Source-aware splitting would require richer source, assay, peptide-family, dataset-source, or provenance metadata.

## Limitations

- Edit-distance grouping is sequence-only and threshold-dependent.
- k-mer Jaccard grouping is heuristic and threshold-dependent.
- Connected components may become large when multiple similarity definitions are combined.
- `max_pairs` can stop pairwise comparison early to prevent expensive runs; summaries include a caveat if this occurs.
- Group assignments are not fold assignments.
- Group assignments are not leakage-aware performance results.
- Future split construction must check class balance and fold feasibility before model reruns.

## Current Status

- Leakage-aware grouping utilities are implemented.
- Unit tests cover in-memory fixtures only.
- CLI dry-run is available.
- No leakage-aware split manifest has been generated.
- No leakage-aware metric has been generated.
- Baseline models have not been rerun.
- Current metrics remain random-stratified baseline metrics and may be optimistic.
- Public preprint remains **Hold / not submission-ready**.
