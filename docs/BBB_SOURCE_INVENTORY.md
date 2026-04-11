# BBB Source Inventory

## Title

Legacy BBB Evidence Source Inventory for `permea-signal-ml`

## Source directory status

Source directory inspected:

- `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis`

Status:

- directory exists
- legacy source files are present
- a local virtual environment directory `.venv/` is also present but is not relevant to migration

## Directory summary

Observed non-`.venv` file count: 30

Observed file types:

- `.csv`: 5
- `.md`: 3
- `.png`: 9
- `.py`: 9
- `.txt`: 2
- no extension: 2

Top-level observed structure relevant to migration:

- dataset and processed tables at repository root
- raw sequence text files under `raw_data/`
- result figures at repository root
- modeling and plotting scripts at repository root
- summary markdown documents at repository root

Notebook files:

- none found

## Dataset-related files

Observed dataset-related files:

- `dataset_with_features.csv`
  - classification: inspect further before decision
  - likely target: `data/processed/`
  - notes: contains columns `sequence,label,length,charge,gravy,pI,aromaticity`
- `processed_dataset.csv`
  - classification: inspect further before decision
  - likely target: `data/processed/`
  - notes: contains columns `sequence,label`
- `raw_data/b3pred_dataset3_negative.txt`
  - classification: inspect further before decision
  - likely target: `data/raw/`
  - notes: raw-source style text file
- `raw_data/b3pred_dataset3_positive.txt`
  - classification: inspect further before decision
  - likely target: `data/raw/`
  - notes: raw-source style text file

## Figure files

Observed figure files:

- `candidate_ranking.png`
  - classification: likely import with renamed artifact status
  - likely target: `figures/`
- `charge_distribution.png`
  - classification: likely import with renamed artifact status
  - likely target: `figures/`
- `permea_candidate_ranking.png`
  - classification: likely import with renamed artifact status
  - likely target: `figures/`
- `permea_charge_boxplot.png`
  - classification: likely import with renamed artifact status
  - likely target: `figures/`
- `permea_charge_distribution.png`
  - classification: likely import with renamed artifact status
  - likely target: `figures/`
- `permea_clean_boxplot.png`
  - classification: inspect further before decision
  - likely target: `figures/`
- `permea_feature_plot.png`
  - classification: inspect further before decision
  - likely target: `figures/`
- `permea_final_charge.png`
  - classification: inspect further before decision
  - likely target: `figures/`
- `rf_feature_importance.png`
  - classification: likely direct import
  - likely target: `figures/`

## Notebook files

Observed notebook files:

- none found

## Metrics / prediction / ranking files

Observed result-style tabular files:

- `baseline_ml_results.csv`
  - classification: likely import with renamed artifact status
  - likely target: `results/metrics/`
  - notes: header `model,accuracy,precision,recall,f1,roc_auc`
- `benchmark_ml_results.csv`
  - classification: likely import with renamed artifact status
  - likely target: `results/metrics/`
  - notes: includes mean and std columns for multiple metrics including `roc_auc_mean`, `pr_auc_mean`, `balanced_accuracy_mean`, `mcc_mean`
- `rf_feature_importance.csv`
  - classification: likely import with renamed artifact status
  - likely target: `results/tables/` or `figures/` support artifact
  - notes: header `feature,importance`

Prediction files:

- none found explicitly

Ranking table files:

- none found explicitly as CSV or TSV

Ranking figure files:

- `candidate_ranking.png`
- `permea_candidate_ranking.png`

## Script / code files

Observed script and code files:

- `baseline_ml.py`
  - classification: inspect further before decision
- `benchmark_ml.py`
  - classification: inspect further before decision
- `compute_features.py`
  - classification: inspect further before decision
- `feature_importance_rf.py`
  - classification: inspect further before decision
- `generate_plot.py`
  - classification: not needed for migration as-is
- `load_data.py`
  - classification: inspect further before decision
- `multi_test.py`
  - classification: not needed for migration
- `plot_analysis.py`
  - classification: not needed for migration as-is
- `smoke_test.py`
  - classification: not needed for migration

These files are useful primarily as provenance and regeneration references, not as direct imports into the current result structure.

## Config / metadata files

Observed config-like or metadata-style files:

- `final_prompt_v.0.1.md`
  - classification: inspect further before decision
  - notes: may contain historical workflow context rather than benchmark config
- `permea_ml_validation_summary.md`
  - classification: likely import with renamed artifact status
  - likely target: `docs/` reference or migration notes, not benchmark outputs
- `permea_validation_mou_summary.md`
  - classification: inspect further before decision
  - likely target: supporting documentation only

Explicit YAML, JSON, or stable config files:

- none found outside `.venv/`

## Candidate files for direct import

Most likely direct imports:

- `rf_feature_importance.png`
  - likely target: `figures/`
- `candidate_ranking.png`
  - likely target: `figures/`
- `permea_candidate_ranking.png`
  - likely target: `figures/`
- `baseline_ml_results.csv`
  - likely target: `results/metrics/`
  - import as legacy artifact, not as current benchmark run output
- `benchmark_ml_results.csv`
  - likely target: `results/metrics/`
  - import as legacy artifact, not as current benchmark run output
- `rf_feature_importance.csv`
  - likely target: `results/tables/`
  - import as legacy artifact if still interpretable

## Candidate files requiring regeneration

Most likely regeneration targets:

- manifest files
  - none found
- predictions CSV in current contract format
  - none found
- ranking CSV in current contract format
  - none found
- summary CSV in current contract format
  - not found as a current-contract artifact
- metrics JSON in current contract format
  - not found
- any rerun needed to align split policy, seed, and config references to the current benchmark contract

## Missing expected files

Expected but not found during inspection:

- notebook files (`.ipynb`)
- predictions CSV files
- ranking CSV files
- manifest JSON files
- explicit YAML or JSON config files for model/data/eval

Expected legacy assets checked explicitly:

- `dataset_with_features.csv`
  - found
  - exact path: `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis/dataset_with_features.csv`
  - size: 226609 bytes
  - likely target mapping: `data/processed/`
- `rf_feature_importance.png`
  - found
  - exact path: `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis/rf_feature_importance.png`
  - size: 40365 bytes
  - likely target mapping: `figures/`
- `candidate_ranking.png`
  - found
  - exact path: `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis/candidate_ranking.png`
  - size: 13983 bytes
  - likely target mapping: `figures/`

## Provenance observations

Observed strengths:

- dataset-like files are present
- result figures are present
- metrics summary CSV files are present
- feature importance CSV is present
- raw source text files are present

Observed provenance gaps:

- no manifest files
- no explicit config files
- no notebook-backed audit trail visible from inspection
- no explicit predictions CSV files
- no explicit ranking CSV files
- split policy not visible from filenames alone
- random seed not visible from filenames alone
- dataset versioning not explicit in legacy filenames

## Recommended next migration actions

1. inspect the legacy Python scripts directly to recover:
   - split policy
   - model configuration
   - feature generation details
   - random seed usage
2. treat `dataset_with_features.csv` as a high-priority inspection target for schema and provenance review
3. import result figures only as legacy imported artifacts unless rerun under the current contract
4. import `baseline_ml_results.csv`, `benchmark_ml_results.csv`, and `rf_feature_importance.csv` only with clear imported-artifact labeling
5. regenerate predictions, ranking tables, summary outputs, and manifests under `permea-signal-ml` once the real benchmark dataset and split policy are confirmed
6. document provenance gaps explicitly before any publication-facing use
