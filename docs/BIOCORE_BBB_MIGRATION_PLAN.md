# BIOCORE BBB Migration Plan

## Title

Biocore / BBB Legacy Evidence Migration Plan for `permea-signal-ml`

## Purpose

This document defines a concrete migration plan for bringing the previously generated BBB/Biocore ML evidence package into the current `permea-signal-ml` repository structure.

The goal is not to relabel legacy work as benchmark-complete automatically. The goal is to map what already exists, preserve usable artifacts carefully, and identify which outputs should be regenerated under the current benchmark contract.

## Source project context

Known context for the earlier work:

- prior BBB/Biocore ML work exists in a separate project directory
- the earlier workflow included a public dataset workflow
- the earlier workflow used sequence-derived physicochemical features
- baseline models likely included Logistic Regression and Random Forest
- class imbalance was part of the modeling context
- reported metrics likely included ROC-AUC and PR-AUC
- legacy figures likely included feature importance and candidate ranking outputs

## Known legacy assets

Known or likely legacy assets include:

- `dataset_with_features.csv`
- `rf_feature_importance.png`
- `candidate_ranking.png`
- notebooks or baseline result outputs

These should be treated as candidate import sources pending confirmation, not as already-onboarded benchmark artifacts.

## Expected source directory

Likely earlier working directory:

- `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis`

This path should be confirmed directly before migration work begins.

## Expected source files

Expected or likely files to inspect:

- `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis/dataset_with_features.csv`
- `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis/rf_feature_importance.png`
- `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis/candidate_ranking.png`
- notebooks under the source project
- baseline metrics exports if present
- prediction or ranking CSV outputs if present

Status of many of these files remains unknown pending direct inspection.

## Proposed target mapping into `permea-signal-ml`

Proposed mapping by asset class:

- source dataset exports:
  - likely target: `data/raw/` or `data/processed/`
  - depends on whether the file is raw source material or already feature-augmented benchmark-ready material
- feature-augmented dataset such as `dataset_with_features.csv`:
  - likely target: `data/processed/`
  - may also require regeneration if feature schema or provenance is incomplete
- metrics exports:
  - likely target: `results/metrics/`
  - only if metrics file exists and its provenance is clear
- predictions files:
  - likely target: `results/predictions/`
  - status unknown pending confirmation
- ranking tables:
  - likely target: `results/tables/`
  - image-only ranking outputs likely belong in `figures/`, while CSV rankings should live in `results/tables/`
- manifest files:
  - target: `results/manifests/`
  - likely absent in legacy work and therefore likely requires regeneration
- figure files such as `rf_feature_importance.png`:
  - target: `figures/`
- figure files such as `candidate_ranking.png`:
  - target: `figures/`
- notebooks:
  - likely target: selective reference only
  - import only if useful and if they do not create confusion with the current benchmark contract

## What can likely be copied as-is

Likely candidates for direct import as imported artifacts:

- `rf_feature_importance.png`
- `candidate_ranking.png`
- existing metrics files if they are found and remain interpretable
- existing prediction or ranking CSV files if they are found and remain interpretable

These should still be marked clearly as imported legacy artifacts unless rerun under the current benchmark contract.

## What should be regenerated under the current benchmark contract

Likely regeneration targets:

- run manifests
- summary CSV outputs
- predictions exports in the current contract format
- ranking CSV outputs in the current contract format
- metrics JSON in the current contract format
- any result whose split policy, config, or dataset version cannot be reconstructed clearly

If `dataset_with_features.csv` lacks sufficient provenance, the safer path is to reconstruct the processed dataset through an explicit data onboarding step rather than treating it as final benchmark evidence.

## Likely provenance gaps

Likely provenance gaps include:

- exact dataset version unknown
- exact split policy unknown or only implicit in notebooks
- exact random seed unknown or pending confirmation
- exact model configuration unknown or pending confirmation
- exact feature extraction settings partially known but not yet formalized to current config paths
- manifest files likely absent

These gaps should be documented explicitly rather than inferred casually.

## Recommended migration order

1. inspect the legacy source directory directly
2. inventory actual files that exist versus files only presumed to exist
3. classify each artifact as raw data, processed data, results artifact, figure, or notebook
4. document dataset provenance and label framing before importing benchmark-facing files
5. import image artifacts and static outputs only if they remain interpretable
6. regenerate metrics, predictions, ranking, and manifest outputs where provenance is incomplete
7. align imported or regenerated artifacts with the current naming and directory conventions

## Pre-publication review points

- confirm the true source dataset identity
- confirm whether redistribution is permitted
- confirm label meaning and positive/negative class framing
- confirm split policy and leakage controls
- distinguish imported legacy artifacts from rerun benchmark artifacts
- ensure no legacy figure is presented as current benchmark evidence without supporting provenance

## Open questions / pending checks

- does `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis` still exist in the expected form
- does `dataset_with_features.csv` exist exactly under that path
- are there legacy metrics JSON or CSV files available
- are there legacy prediction CSV files available
- was candidate ranking exported only as a figure or also as a table
- were Logistic Regression and Random Forest both run under saved configs or only through notebooks
- what split policy was actually used in the original work
- what random seed, if any, governed the original training runs
- should some legacy outputs be retained only as historical reference rather than benchmark evidence

Legacy outputs may remain useful, but unless rerun under the current benchmark contract they should be marked clearly as imported artifacts.
