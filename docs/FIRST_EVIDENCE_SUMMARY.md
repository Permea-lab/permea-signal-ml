# First Evidence Summary

## Title

First BBB Evidence Surface in `permea-signal-ml`

## What was onboarded

The repository now contains a first onboarded legacy BBB evidence surface consisting of:

- imported legacy processed dataset candidate:
  - `legacy_bbb_dataset_with_features.csv`
- imported legacy metrics artifacts:
  - `legacy_baseline_ml_results.csv`
  - `legacy_benchmark_ml_results.csv`
- imported legacy feature-importance artifacts:
  - `legacy_rf_feature_importance.csv`
  - `legacy_rf_feature_importance.png`

These remain imported legacy artifacts, not current benchmark outputs.

## What was regenerated

Using the onboarded dataset surface, the repository produced regenerated benchmark-contract outputs for:

- Dummy most-frequent
- RandomForest
- LogisticRegression

For each rerun, the repository now has:

- metrics JSON
- predictions CSV
- ranking CSV
- summary CSV
- manifest JSON
- score-distribution figure

## Current dataset surface

Current imported dataset size:

- `2959` rows

Current feature set:

- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

For rerun readiness, a derived dataset was created with:

- deterministic `sequence_id`
- conservative `source` value

Dataset version, attribution, and licensing remain pending confirmation.

## Current baseline result snapshot

Regenerated Dummy rerun:

- ROC-AUC: `0.5000`
- PR-AUC: `0.0909`
- Precision: `0.0000`
- Recall: `0.0000`
- F1: `0.0000`
- MCC: `0.0000`

Regenerated RandomForest rerun:

- ROC-AUC: `0.8489`
- PR-AUC: `0.5002`
- Precision: `0.5825`
- Recall: `0.3869`
- F1: `0.4644`
- MCC: `0.4331`

Regenerated LogisticRegression rerun:

- ROC-AUC: `0.8605`
- PR-AUC: `0.4903`
- Precision: `0.2670`
- Recall: `0.7621`
- F1: `0.3949`
- MCC: `0.3618`

## Why this matters

This is the first point where imported legacy BBB evidence and current benchmark-contract execution meet inside one repository.

That matters because the repository can now:

- preserve legacy artifacts transparently
- rerun baseline models under explicit configs
- emit manifest-backed outputs
- support further evidence-building without relying only on opaque historical files

## What this does not prove

This does not prove:

- solved biological delivery
- validated wet-lab performance
- universal permeability prediction
- finalized dataset provenance

The current state is still an early computational evidence surface.

## Next evidence-building steps

- confirm dataset version
- confirm attribution requirements
- confirm licensing status
- compare regenerated outputs against imported legacy artifacts more systematically
- prepare a publication-support package only after provenance gaps are reduced
