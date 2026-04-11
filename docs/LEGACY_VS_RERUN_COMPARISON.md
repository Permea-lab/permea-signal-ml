# Legacy vs Rerun Comparison

## Title

Imported Legacy BBB Evidence vs Regenerated Benchmark-Contract Rerun

## Purpose

This document compares:

- imported legacy BBB artifacts brought into `permea-signal-ml` for reference
- regenerated benchmark-contract rerun outputs produced inside the current repository

The purpose is to show what is consistent, what differs, and what remains provisional.

## Imported legacy evidence summary

Imported legacy artifacts currently onboarded:

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `figures/legacy_rf_feature_importance.png`
- `results/tables/legacy_rf_feature_importance.csv`
- `results/metrics/legacy_baseline_ml_results.csv`
- `results/metrics/legacy_benchmark_ml_results.csv`

Imported legacy metric surfaces available directly from files:

- holdout-style results from `legacy_baseline_ml_results.csv`
- 5-fold benchmark summary metrics from `legacy_benchmark_ml_results.csv`

These remain legacy imports rather than current benchmark-contract outputs.

## Regenerated rerun evidence summary

Current regenerated outputs available:

- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/tables/legacy_bbb_dummy_v01_summary.csv`
- `results/manifests/legacy_bbb_dummy_v01_manifest.json`
- `results/predictions/legacy_bbb_dummy_v01_predictions.csv`
- `results/tables/legacy_bbb_dummy_v01_ranking.csv`
- `figures/legacy_bbb_dummy_v01_score_distribution.png`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/tables/legacy_bbb_rf_v01_summary.csv`
- `results/manifests/legacy_bbb_rf_v01_manifest.json`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`
- `figures/legacy_bbb_rf_v01_score_distribution.png`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/tables/legacy_bbb_lr_v01_summary.csv`
- `results/manifests/legacy_bbb_lr_v01_manifest.json`
- `results/predictions/legacy_bbb_lr_v01_predictions.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `figures/legacy_bbb_lr_v01_score_distribution.png`

These are regenerated benchmark-contract outputs, but the dataset version, attribution, and licensing fields remain pending confirmation.

## Dataset comparison

Imported legacy side:

- dataset file: `legacy_bbb_dataset_with_features.csv`
- row count: `2959`
- columns:
  - `sequence`
  - `label`
  - `length`
  - `charge`
  - `gravy`
  - `pI`
  - `aromaticity`
- `sequence_id` absent
- `source` absent

Regenerated rerun side:

- rerun used derived file: `legacy_bbb_dataset_with_features_rerun_ready.csv`
- same imported legacy content retained
- added fields:
  - `sequence_id`
  - `source`

The rerun dataset is therefore a schema-adapted derivative of the imported legacy processed dataset, not a different scientific dataset.

## Feature comparison

Imported legacy side:

- recovered feature set from legacy code:
  - `length`
  - `charge`
  - `gravy`
  - `pI`
  - `aromaticity`

Regenerated rerun side:

- same feature set used by current rerun config and pipeline:
  - `length`
  - `charge`
  - `gravy`
  - `pI`
  - `aromaticity`

Feature surface is consistent across the imported and regenerated sides.

## Split/eval comparison

Imported legacy side:

- strongest benchmark policy recoverable from legacy code:
  - `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- legacy holdout script also existed separately:
  - `train_test_split(test_size=0.2, stratify=y, random_state=42)`

Regenerated rerun side:

- current rerun used:
  - `stratified_kfold`
  - `cv_folds = 5`
  - `random_seed = 42`

The regenerated rerun is aligned with the strongest recovered benchmark-style policy from legacy code.

## Model comparison

Imported legacy side:

- holdout script models:
  - Logistic Regression
  - Random Forest
- benchmark script models:
  - Dummy most-frequent
  - Logistic Regression
  - Random Forest

Regenerated rerun side:

- executed models:
  - Dummy most-frequent
  - Logistic Regression
  - Random Forest

## Metrics comparison table

Legacy benchmark metrics below come from imported `legacy_benchmark_ml_results.csv`.

Regenerated metrics below come from current rerun metrics JSON outputs.

| Model | Evidence type | ROC-AUC | PR-AUC | Precision | Recall | F1 | MCC |
|---|---|---:|---:|---:|---:|---:|---:|
| Dummy_MostFrequent | Legacy imported benchmark mean | 0.5000 | 0.0909 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Dummy most-frequent | Regenerated rerun mean | 0.5000 | 0.0909 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| LogisticRegression | Legacy imported benchmark mean | 0.8590 | 0.4965 | 0.2774 | 0.7695 | 0.4069 | 0.3755 |
| LogisticRegression | Regenerated rerun mean | 0.8605 | 0.4903 | 0.2670 | 0.7621 | 0.3949 | 0.3618 |
| RandomForest | Legacy imported benchmark mean | 0.8863 | 0.5943 | 0.6034 | 0.5057 | 0.5481 | 0.5112 |
| RandomForest | Regenerated rerun mean | 0.8489 | 0.5002 | 0.5825 | 0.3869 | 0.4644 | 0.4331 |

Legacy imported holdout metrics from `legacy_baseline_ml_results.csv` for reference:

| Model | Evidence type | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|
| LogisticRegression | Legacy imported holdout | 0.7872 | 0.2662 | 0.7593 | 0.3942 | 0.8698 |
| RandomForest | Legacy imported holdout | 0.9307 | 0.6585 | 0.5000 | 0.5684 | 0.8827 |

## Key consistencies

- same legacy processed dataset family used as the starting point
- same core feature set used
- same benchmark-style split policy family used for the rerun
- same random seed value `42`
- same baseline model families reused for rerun
- regenerated Dummy baseline exactly matches the imported legacy benchmark Dummy metrics
- regenerated Logistic Regression metrics are close to imported legacy benchmark values

## Key differences

- rerun used a schema-adapted dataset with added `sequence_id` and `source`
- regenerated outputs include manifest, predictions, ranking, summary, and figure files under the current contract
- regenerated Random Forest metrics are lower than imported legacy benchmark metrics across ROC-AUC, PR-AUC, recall, F1, and MCC
- imported holdout metrics and imported benchmark metrics are different evaluation surfaces and should not be conflated

## What remains provisional

- dataset version remains `pending_confirmation`
- attribution remains pending
- licensing remains pending
- imported dataset lineage beyond the inspected legacy directory remains provisional
- imported legacy figures remain legacy artifacts unless explicitly regenerated under the current contract

## Interpretation note

The current rerun establishes a real benchmark-contract execution surface on top of the imported legacy BBB processed dataset candidate.

It does not prove solved delivery, universal permeability prediction, or validated biology.

The correct interpretation is narrower:

- legacy results have now been connected to a current reproducible pipeline
- some benchmark behavior appears directionally consistent, especially for Logistic Regression
- final evidence status still depends on dataset versioning, attribution, licensing confirmation, and continued rerun discipline
