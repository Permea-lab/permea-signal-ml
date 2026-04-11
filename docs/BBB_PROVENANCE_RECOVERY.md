# BBB Provenance Recovery

## Title

Legacy BBB Analysis Provenance Recovery for `permea-signal-ml`

## Purpose

This report recovers benchmark-relevant provenance from the inspected legacy BBB analysis code under `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis`.

The purpose is to distinguish between:

- imported legacy artifacts
- reproducible regenerated artifacts under the current `permea-signal-ml` benchmark contract

Only findings directly supported by inspected code are included here.

## Files inspected

Primary benchmark-relevant files inspected:

- `baseline_ml.py`
- `benchmark_ml.py`
- `compute_features.py`
- `feature_importance_rf.py`
- `load_data.py`

Additional figure-related files inspected because they appeared to generate legacy result figures:

- `generate_plot.py`
- `plot_analysis.py`

## Dataset construction findings

Findings from `"load_data.py"`:

- input positive file: `raw_data/b3pred_dataset3_positive.txt`
- input negative file: `raw_data/b3pred_dataset3_negative.txt`
- input format: FASTA-like text parsed by header lines beginning with `>`
- positive records are assigned `label = 1`
- negative records are assigned `label = 0`
- output file written by the script: `processed_dataset.csv`
- output columns constructed directly in code: `sequence`, `label`

Findings from `"compute_features.py"`:

- `"compute_features.py"` reads `processed_dataset.csv`
- `"compute_features.py"` writes `dataset_with_features.csv`
- feature generation is applied to the `sequence` column

Findings from `"baseline_ml.py"`, `"benchmark_ml.py"`, `"feature_importance_rf.py"`, and `"plot_analysis.py"`:

- all of these scripts read `dataset_with_features.csv`

What is not recoverable from inspected code:

- dataset version
- original upstream dataset publication metadata
- redistribution or licensing status
- any explicit `sequence_id` construction
- any explicit source column in processed outputs

## Feature construction findings

Findings from `"compute_features.py"`:

- feature computation uses `Bio.SeqUtils.ProtParam.ProteinAnalysis`
- defined feature set:
  - `length`
  - `charge`
  - `gravy`
  - `pI`
  - `aromaticity`
- `charge` is defined explicitly in code as:
  - `count("K") + count("R") - count("D") - count("E")`
- `gravy`, `pI`, and `aromaticity` are computed through `ProteinAnalysis`
- if feature computation fails, the script emits `None` for all feature fields in that row
- the script prints:
  - missing-value counts
  - grouped feature means by `label`

Feature columns used consistently across `"baseline_ml.py"`, `"benchmark_ml.py"`, and `"feature_importance_rf.py"`:

- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

## Model findings

Findings from `"baseline_ml.py"`:

- model families used:
  - `LogisticRegression`
  - `RandomForestClassifier`
- Logistic Regression implementation details:
  - wrapped in a `Pipeline`
  - preprocessing includes `StandardScaler`
  - `class_weight="balanced"`
  - `random_state=42`
  - `max_iter=2000`
- Random Forest implementation details:
  - `n_estimators=300`
  - `max_depth=None`
  - `min_samples_split=5`
  - `min_samples_leaf=2`
  - `class_weight="balanced"`
  - `random_state=42`
  - `n_jobs=-1`

Findings from `"benchmark_ml.py"`:

- model families used:
  - `DummyClassifier(strategy="most_frequent")`
  - `LogisticRegression`
  - `RandomForestClassifier`
- Logistic Regression implementation details:
  - wrapped in a `Pipeline`
  - preprocessing includes `StandardScaler`
  - `class_weight="balanced"`
  - `random_state=42`
  - `max_iter=3000`
- Random Forest implementation details:
  - `n_estimators=300`
  - `min_samples_split=5`
  - `min_samples_leaf=2`
  - `class_weight="balanced"`
  - `random_state=42`
  - `n_jobs=-1`
- `max_depth` is not set explicitly in `"benchmark_ml.py"` and therefore remains default behavior

Findings from `"feature_importance_rf.py"`:

- a Random Forest model is trained on the full dataset for feature-importance output
- parameters used:
  - `n_estimators=300`
  - `min_samples_split=5`
  - `min_samples_leaf=2`
  - `class_weight="balanced"`
  - `random_state=42`
  - `n_jobs=-1`

## Split policy findings

Findings from `"baseline_ml.py"`:

- split method: `train_test_split`
- `test_size=0.2`
- `stratify=y`
- comment in code states the reason as dataset imbalance

Findings from `"benchmark_ml.py"`:

- cross-validation method: `StratifiedKFold`
- `n_splits=5`
- `shuffle=True`
- `random_state=42`

This is the strongest recoverable benchmark-style split policy from inspected code.

What is not recoverable from inspected code:

- any grouped split policy
- any source-aware leakage control beyond label stratification
- whether legacy figure outputs always correspond to the cross-validation workflow

## Random seed findings

Findings from inspected code:

- `"baseline_ml.py"` uses `random_state=42` in:
  - `train_test_split`
  - `LogisticRegression`
  - `RandomForestClassifier`
- `"benchmark_ml.py"` uses `random_state=42` in:
  - `StratifiedKFold`
  - `LogisticRegression`
  - `RandomForestClassifier`
- `"feature_importance_rf.py"` uses `random_state=42` in `RandomForestClassifier`

This random seed is recoverable from inspected code with high confidence.

## Metrics and evaluation findings

Findings from `"baseline_ml.py"`:

- metrics computed:
  - `accuracy`
  - `precision`
  - `recall`
  - `f1`
  - `roc_auc`
- additional printed evaluation outputs:
  - `confusion_matrix`
  - `classification_report`
- summary CSV written:
  - `baseline_ml_results.csv`

Findings from `"benchmark_ml.py"`:

- evaluation uses `cross_validate`
- metrics computed:
  - `accuracy`
  - `precision`
  - `recall`
  - `f1`
  - `roc_auc`
  - `pr_auc`
  - `balanced_accuracy`
  - `mcc`
- per-model summary stores mean and standard deviation for each metric
- summary CSV written:
  - `benchmark_ml_results.csv`

What is not recoverable from inspected code:

- fold-level prediction outputs
- prediction score export files
- ranking table export files tied directly to the benchmark scripts
- manifest-style provenance outputs

## Figure generation findings

Findings from `"feature_importance_rf.py"`:

- output files written:
  - `rf_feature_importance.csv`
  - `rf_feature_importance.png`
- figure is generated from Random Forest feature importances trained on the full dataset

Findings from `"plot_analysis.py"`:

- reads `dataset_with_features.csv`
- maps `label` to groups:
  - `1 -> BBB`
  - `0 -> Non-BBB`
- generates a charge boxplot by group
- output file written:
  - `permea_clean_boxplot.png`

Findings from `"generate_plot.py"`:

- generates `permea_candidate_ranking.png`
- values are hard-coded:
  - names: `NEW_1`, `NEW_2`, `NEW_3`, `TAT`
  - scores: `4.832`, `4.580`, `4.556`, `4.373`
- this figure is not linked in code to `dataset_with_features.csv`, to a metrics export, or to a reproducible ranking-table generation step

What is not recoverable from inspected code:

- code path for `candidate_ranking.png`
- whether `candidate_ranking.png` and `permea_candidate_ranking.png` originate from the same ranking workflow
- whether any candidate ranking image was generated from a saved CSV ranking artifact

## What can now be mapped confidently

- raw input source files:
  - `raw_data/b3pred_dataset3_positive.txt`
  - `raw_data/b3pred_dataset3_negative.txt`
  - likely mapping: legacy raw-source inputs
- intermediate processed dataset:
  - `processed_dataset.csv`
  - likely mapping: `data/processed/` as legacy intermediate artifact
- feature-augmented dataset:
  - `dataset_with_features.csv`
  - likely mapping: `data/processed/` as legacy processed artifact pending provenance note
- feature set used by legacy baseline modeling:
  - `length`, `charge`, `gravy`, `pI`, `aromaticity`
- baseline metrics exports:
  - `baseline_ml_results.csv`
  - `benchmark_ml_results.csv`
  - likely mapping: `results/metrics/` as imported legacy artifacts
- feature-importance artifacts:
  - `rf_feature_importance.csv`
  - `rf_feature_importance.png`
  - likely mapping: `results/tables/` and `figures/`

## What remains unknown

- dataset version is not recoverable from inspected code
- source licensing is not recoverable from inspected code
- source attribution requirements are not recoverable from inspected code
- presence of stable sequence identifiers is not recoverable from inspected code
- any explicit predictions CSV output is not recoverable from inspected code
- any explicit ranking CSV output is not recoverable from inspected code
- manifest-style run provenance is not recoverable from inspected code
- exact code path for `candidate_ranking.png` is not recoverable from inspected code
- whether the hard-coded ranking in `"generate_plot.py"` reflects model output, manual selection, or presentation-only values is not recoverable from inspected code

## Recommended regeneration targets

Better to regenerate under the current contract:

- predictions CSV artifacts
  - not recoverable from inspected code
- ranking CSV artifacts
  - not recoverable from inspected code
- manifest JSON artifacts
  - not recoverable from inspected code
- summary CSV artifacts in current contract format
  - not produced by inspected legacy scripts
- any current benchmark metrics JSON
  - not produced by inspected legacy scripts
- any candidate ranking artifact intended to be treated as benchmark evidence
  - `"generate_plot.py"` is hard-coded and not sufficient as benchmark provenance
- any rerun intended to represent the first benchmark-contract evidence package
  - should be rerun from onboarded dataset/config paths under `permea-signal-ml`

## Recommended direct-import-only artifacts

### Safe to import as legacy artifact

- `rf_feature_importance.png`
  - directly tied to `"feature_importance_rf.py"`
- `rf_feature_importance.csv`
  - directly tied to `"feature_importance_rf.py"`
- `baseline_ml_results.csv`
  - directly tied to `"baseline_ml.py"`
- `benchmark_ml_results.csv`
  - directly tied to `"benchmark_ml.py"`
- `dataset_with_features.csv`
  - useful as a legacy processed artifact for inspection and schema alignment

### Better to regenerate under current contract

- any fold-level predictions
  - not found and not exported by inspected code
- any ranking CSV
  - not found and not exported by inspected code
- any manifest-like provenance
  - not found and not exported by inspected code
- any benchmark-ready summary artifact using current naming rules
  - not found in legacy outputs
- any candidate-ranking evidence intended for publication-facing benchmark claims
  - code provenance is insufficient

### Still ambiguous / inspect manually

- `candidate_ranking.png`
  - file exists, but generation path is not recoverable from inspected code
- `permea_candidate_ranking.png`
  - generated by `"generate_plot.py"`, but values are hard-coded and should be treated as presentation artifact until manually verified
- `permea_clean_boxplot.png`
  - code provenance is recoverable, but publication use still depends on dataset/provenance review
- any additional figure files not directly tied to the inspected benchmark scripts
  - inspect manually before migration decision
