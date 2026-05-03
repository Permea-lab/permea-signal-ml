# Dataset

## Purpose

This document defines the current BBB wedge dataset surface used for benchmark-oriented reruns in `permea-signal-ml`. Its purpose is to separate confirmed dataset facts from operational rerun metadata, recovered provenance, and unresolved provenance items that still constrain interpretation.

## Current dataset surface

The current reruns use an imported legacy BBB-oriented processed dataset. The current rerun-ready dataset surface contains `2959` rows and is stored as a processed benchmark input for current-contract reruns.

For this v0.1 evidence package, the practical dataset-surface identifier is `legacy_bbb_dataset_with_features`. The exact public version label remains `pending_confirmation` in current run manifests and should not be treated as a provenance-closed public dataset release name.

## Dataset path status

Current file inspection supports the following path status:

- raw source dataset path in this repo: unresolved; `data/raw/` currently contains no raw source dataset file beyond `.gitkeep`
- imported processed dataset path: `data/processed/legacy_bbb_dataset_with_features.csv`
- rerun-ready processed dataset path: `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- dataset config path: `configs/data/legacy_bbb_dataset_with_features.yaml`

The current dataset config explicitly points current-contract reruns to `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`. The imported processed dataset and the rerun-ready processed dataset each contain `2959` data rows based on file line counts excluding the header row.

The rerun-ready table adds operational metadata needed for current repository execution. It should not be read as a raw source dataset or as a public provenance-closed dataset release.

## Confirmed fields

The currently file-verified benchmark-relevant fields in the imported processed dataset are:

- `sequence`
- `label`
- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

These fields define the present sequence and feature surface used for regenerated baseline comparisons.

The rerun-ready processed dataset additionally includes:

- `sequence_id`
- `source`

These operational metadata fields are file-verified in `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv` and configured in `configs/data/legacy_bbb_dataset_with_features.yaml`.

## Label field status

The `label` field is the current binary benchmark target used by the regenerated baseline reruns. Its values are used as supplied in the imported legacy processed dataset surface.

Current confirmed status:

- `label` is present in the rerun-ready dataset surface
- current scripts treat `label` as the supervised target for benchmark reruns
- current reruns do not alter or relabel the imported values

Current unresolved status:

- original label-source criteria are not yet fully reconstructed
- positive-class and negative-class source criteria are not yet fully reconstructed
- original assay, literature, or benchmark inclusion basis is not yet confirmed in the current repo
- source-level attribution for the original labeling process remains incomplete
- the current package should not treat labels as independently verified biological truth

This label surface is sufficient for trusted review of the current computational benchmark, but it remains a preprint-facing provenance item until the original labeling source and criteria are either confirmed or explicitly documented as unresolved.

## Operational metadata added for reruns

The current rerun-ready dataset also includes the following operational fields:

- `sequence_id`
- `source`

These fields were added for benchmark-contract compatibility only. They support stable row identity and explicit source labeling for reruns, but they do not change labels, sequence values, or feature values.

The current `source` value should be interpreted as an operational source label for imported legacy continuity. It is not a substitute for original upstream dataset attribution or license documentation.

## Provenance status

The current provenance surface is partially recovered and partially unresolved. Enough has been recovered to support benchmark-oriented computational reruns, but not enough to treat the dataset as fully provenance-closed for broader public reuse.

## Confirmed benchmark-relevant details

- the legacy processed dataset path was recovered through legacy-code inspection
- the current feature surface was recovered as `length`, `charge`, `gravy`, `pI`, and `aromaticity`
- the random seed was recovered as `42`
- the strongest recovered benchmark split policy was `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- the rerun-ready dataset adds deterministic `sequence_id` and conservative `source` metadata for current-contract execution

## Unresolved or still-confirming items

- dataset version label for public reference; current manifests use `pending_confirmation`
- final attribution requirements
- redistribution and licensing status
- whether the current processed dataset can be included directly in a public preprint supplement or public dataset release
- exact version naming convention for public reference
- whether additional source-level metadata should be restored later
- original label-source criteria and labeling provenance
- duplicate, near-duplicate, and sequence-similarity leakage status

These unresolved items do not block the current rerun workflow, but they do limit how broadly the dataset surface should be presented or redistributed.

## Leakage and duplicate-status note

The recovered split policy is `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. This documents the current rerun split behavior and seed, but it is not a duplicate-removal or sequence-similarity-aware split claim.

The current package has not documented an audit for:

- exact duplicate sequences
- near-duplicate sequences
- sequence-similarity leakage across folds

These should be treated as unresolved benchmark risks for preprint readiness. The current documentation does not claim that leakage exists, nor does it claim that the benchmark is leakage-free.

## Current use boundary

The current dataset surface supports:

- benchmark-oriented computational reruns
- baseline comparison
- candidate prioritization analysis

The current dataset surface does not by itself support:

- biological validation claims
- clinical relevance claims
- universal delivery claims

It should therefore be treated as a bounded computational benchmark surface rather than as validated biological evidence.

## Trusted-review versus preprint status

Trusted-review status: sufficient for computational/reproducibility review when paired with the extended review packet and current artifacts.

Preprint-readiness status: not fully closed. Dataset version, attribution, licensing, label-source criteria, and duplicate/similarity leakage status require confirmation, explicit documentation, or careful limitation language before public preprint submission.

## Preprint blocker list

Before public preprint submission or public dataset release, the following items require resolution or explicit final disclosure:

- raw source dataset availability or source-reference status
- public dataset version identifier
- source attribution and citation requirements
- license and redistribution rights
- original label-source criteria, including positive and negative class definitions
- duplicate, near-duplicate, and sequence-similarity leakage audit status
- final statement of whether the processed dataset can be redistributed or only referenced

See `DATASET_PROVENANCE_AND_LABEL_SOURCE_CHECKLIST_V0_1.md` for the current checklist.

## Why this dataset documentation matters

This documentation matters because dataset trust depends on explicit provenance boundaries. Clear separation between confirmed facts, rerun metadata, and unresolved items improves trust, supports provenance discipline, makes benchmark reuse easier, and strengthens paper-support readiness without overstating what is currently known.
