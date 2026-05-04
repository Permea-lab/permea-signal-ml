# Leakage-Aware Split Manifest Report v0.1

## Purpose

This report summarizes leakage-aware split manifest generation from the combined group assignment outputs.

The split manifest is not model performance evidence. No leakage-aware model metrics were generated, baseline models were not rerun, and this does not prove robust generalization or leakage-free status. Public preprint status remains **Hold / not submission-ready**.

## Inputs

| Field | Value |
|---|---|
| Dataset path | `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` |
| Group assignment path | `results/sensitivity/group_assignments_combined.csv` |
| Output directory | `results/sensitivity/` |
| Split policy | `leakage_aware_group_stratified` |
| Number of folds | 5 |
| Random state | 42 |

## Generated Outputs

| Output | Status |
|---|---|
| `results/sensitivity/combined_group_stratified_split_manifest.csv` | Generated |
| `results/sensitivity/combined_group_stratified_split_summary.json` | Generated |

No baseline model outputs, model metrics, prediction files, ranking tables, figures, or manuscript updates were generated.

## Split Quality Summary

| Field | Value |
|---|---:|
| Rows | 2,959 |
| Groups | 2,958 |
| Folds | 5 |
| Groups crossing folds | 0 |

### Fold Row Counts

| Fold | Rows |
|---:|---:|
| 1 | 592 |
| 2 | 592 |
| 3 | 592 |
| 4 | 592 |
| 5 | 591 |

### Fold Label Counts

| Fold | Negative | Positive |
|---:|---:|---:|
| 1 | 538 | 54 |
| 2 | 538 | 54 |
| 3 | 538 | 54 |
| 4 | 538 | 54 |
| 5 | 538 | 53 |

### Positive Rates

| Fold | Positive rate |
|---:|---:|
| 1 | 0.09121621621621621 |
| 2 | 0.09121621621621621 |
| 3 | 0.09121621621621621 |
| 4 | 0.09121621621621621 |
| 5 | 0.08967851099830795 |

### Group Counts

| Fold | Groups | Largest group size |
|---:|---:|---:|
| 1 | 591 | 2 |
| 2 | 592 | 1 |
| 3 | 592 | 1 |
| 4 | 592 | 1 |
| 5 | 591 | 1 |

## Caveats

- At least one non-singleton group is kept within one fold.
- The upstream combined group assignment retained the `max_pairs=10000` caveat, so grouping may be incomplete.
- The current `source` field remains too coarse for source-aware split control.
- This manifest is a split plan for future reruns, not a performance result.

## Interpretation

The manifest enables a future rerun of the existing baseline models under the `leakage_aware_group_stratified` policy. It does not change current random-stratified metrics, does not provide leakage-aware model evidence, and does not support robust-generalization claims.

Current manuscript metrics remain random-stratified baseline metrics until approved model reruns are completed and interpreted.

## Recommended Next Task

Task 087 - Commit Leakage-Aware Split Manifests
