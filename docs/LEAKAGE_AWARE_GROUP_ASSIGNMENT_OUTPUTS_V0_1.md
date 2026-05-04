# Leakage-Aware Group Assignment Outputs v0.1

## Purpose

This report summarizes the first leakage-aware group assignment outputs generated for the BBB-oriented Permea Signal ML benchmark.

These outputs are group assignments only. They are not leakage-aware split manifests, do not assign train/test folds, do not rerun baseline models, do not generate leakage-aware model metrics, and do not establish robust generalization or leakage-free status. Public preprint status remains **Hold / not submission-ready**.

## Inputs

| Field | Value |
|---|---|
| Input dataset | `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` |
| Output directory | `results/sensitivity/` |
| Grouping method | `combined` |
| Sequence column | `sequence` |
| Source column | `source` |
| Edit-distance threshold | `1` |
| k-mer size | `3` |
| Jaccard threshold | `0.8` |
| `max_pairs` | `10000` |

## Generated Outputs

| Output | Status |
|---|---|
| `results/sensitivity/group_assignments_combined.csv` | Generated |
| `results/sensitivity/grouping_summary_combined.json` | Generated |

No leakage-aware split manifest was generated. No leakage-aware model metric table was generated.

## Summary

| Field | Value |
|---|---:|
| Rows assigned | 2,959 |
| Groups | 2,958 |
| Singleton groups | 2,957 |
| Non-singleton groups | 1 |
| Largest group size | 2 |

Grouping method:

- `combined_exact+edit_distance<=1+kmer3_jaccard>=0.8`

Caveat:

- Pairwise comparison stopped after `max_pairs=10000`; grouping may be incomplete.

## Source/Group Feasibility

| Field | Value |
|---|---|
| Source column present | true |
| Unique source values | 1 |
| Source counts | `legacy_bbb_import`: 2,959 |
| Feasible for source-aware group split | false |
| Caveat | Source field is too coarse for source-aware group splitting. |

## Interpretation

The generated grouping outputs support future leakage-aware split-manifest generation. They do not themselves provide model-performance evidence, do not measure leakage-aware performance, and do not change the interpretation of existing random-stratified baseline metrics.

The next technical step is to generate leakage-aware split manifests from these group assignments, with explicit checks for class balance, fold feasibility, and grouping caveats.

## Recommended Next Task

Task 085 - Commit Leakage-Aware Group Assignment Outputs
