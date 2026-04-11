# Legacy BBB Rerun Preparation

## Purpose

This document records the schema adaptations applied to the imported legacy BBB processed dataset to make a first benchmark-contract rerun possible in `permea-signal-ml`.

## Schema issues found

Observed in `data/processed/legacy_bbb_dataset_with_features.csv`:

- `sequence_id` column missing
- `source` column missing

The following fields were already present:

- `sequence`
- `label`
- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

## Fields added for rerun readiness

Derived file created:

- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`

Fields added:

- `sequence_id`
  - deterministic format: `legacy_bbb_000001`, `legacy_bbb_000002`, ...
- `source`
  - conservative constant value: `legacy_bbb_import`

Existing columns were preserved.

Label values were not changed.

Feature values were not edited in the imported file during this preparation step.

## Why this does not create new scientific claims

The added fields are operational metadata for repository execution and traceability.

They do not:

- alter labels
- alter sequences
- create new biological evidence
- imply new validation

Their role is only to make the imported dataset compatible with the current benchmark-contract pipeline surface.

## What remains pending

- dataset version confirmation
- attribution confirmation
- licensing confirmation
- verification of whether legacy source should eventually be represented more granularly than `legacy_bbb_import`
