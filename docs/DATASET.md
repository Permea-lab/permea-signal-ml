# Dataset

## Purpose

This document defines the current BBB wedge dataset surface used for benchmark-oriented reruns in `permea-signal-ml`. Its purpose is to separate confirmed dataset facts from operational rerun metadata, recovered provenance, and unresolved provenance items that still constrain interpretation.

## Current dataset surface

The current reruns use an imported legacy BBB-oriented processed dataset. The current rerun-ready dataset surface contains `2959` rows and is stored as a processed benchmark input for current-contract reruns.

## Confirmed fields

The currently confirmed benchmark-relevant fields are:

- `sequence`
- `label`
- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

These fields define the present sequence and feature surface used for regenerated baseline comparisons.

## Operational metadata added for reruns

The current rerun-ready dataset also includes the following operational fields:

- `sequence_id`
- `source`

These fields were added for benchmark-contract compatibility only. They support stable row identity and explicit source labeling for reruns, but they do not change labels, sequence values, or feature values.

## Provenance status

The current provenance surface is partially recovered and partially unresolved. Enough has been recovered to support benchmark-oriented computational reruns, but not enough to treat the dataset as fully provenance-closed for broader public reuse.

## Confirmed benchmark-relevant details

- the legacy processed dataset path was recovered through legacy-code inspection
- the current feature surface was recovered as `length`, `charge`, `gravy`, `pI`, and `aromaticity`
- the random seed was recovered as `42`
- the strongest recovered benchmark split policy was `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- the rerun-ready dataset adds deterministic `sequence_id` and conservative `source` metadata for current-contract execution

## Unresolved or still-confirming items

- final attribution requirements
- redistribution and licensing status
- exact version naming convention for public reference
- whether additional source-level metadata should be restored later

These unresolved items do not block the current rerun workflow, but they do limit how broadly the dataset surface should be presented or redistributed.

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

## Why this dataset documentation matters

This documentation matters because dataset trust depends on explicit provenance boundaries. Clear separation between confirmed facts, rerun metadata, and unresolved items improves trust, supports provenance discipline, makes benchmark reuse easier, and strengthens paper-support readiness without overstating what is currently known.
