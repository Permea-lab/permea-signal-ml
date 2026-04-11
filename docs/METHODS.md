# Methods

## Title

Permea Signal ML v0.1 Benchmark Contract

## Purpose

This document defines the current benchmark contract for Permea Signal ML v0.1. Its purpose is to make the task framing, feature framing, baseline model set, evaluation policy, and output expectations explicit before broader claims or broader model scope are considered.

The repository is intended as an early-stage, benchmark-oriented computational evidence package. It is not intended to imply solved delivery biology or validated therapeutic performance.

## Current task framing

The current v0.1 task is an early-stage binary classification and candidate-prioritization workflow in a BBB-oriented peptide / permeability-related signal context.

The working question is narrow:

- can permeability-related signal be studied from sequence-derived physicochemical features
- can a simple benchmark workflow support transparent candidate prioritization before experimental validation

This framing is benchmark-first and deliberately limited.

## Input schema

The expected input object is a row-oriented sequence table. At minimum, each record should contain:

- `sequence_id`
- `sequence`
- `label`
- `source`
- `metadata` (optional)

Additional columns may be included for curation, filtering, split assignment, or source-specific audit, but the minimum benchmark surface should remain stable and documented.

## Feature schema

The v0.1 feature schema is intentionally lightweight and sequence-derived. The baseline expectation is that the feature table includes at least:

- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

Additional simple physicochemical summaries may be added later, but v0.1 should remain interpretable and easy to audit.

## Label framing

The current label framing is binary and task-specific. Labels should be interpreted as benchmark labels for the current permeability-related signal or BBB-oriented prioritization task, not as universal biological truth.

Label definitions must be documented alongside the dataset version used for a run.

## Baseline model set

The initial baseline model set is restricted to simple reference models:

- Dummy classifier
- Logistic Regression
- Random Forest

These models are included to establish a transparent baseline for signal detection and candidate ranking. They are not intended to define the final modeling boundary of the project.

## Split and evaluation policy

The default v0.1 evaluation policy is:

- stratified K-fold cross-validation
- fixed random seed
- class imbalance awareness
- no leakage between folds

The exact fold count and seed should be versioned through configuration and tracked in the run manifest. If source-aware or grouped splitting becomes necessary, that change should be documented as a benchmark policy change rather than silently introduced.

## Metrics

The current metric set is:

- ROC-AUC
- PR-AUC
- precision
- recall
- F1
- MCC

These metrics are chosen to support cautious interpretation under a likely imbalanced binary classification setting.

## Output artifacts

Expected v0.1 output artifacts include:

- metrics JSON/CSV
- fold predictions
- candidate ranking CSV
- run summary CSV
- feature importance figure
- score distribution figure
- run manifest JSON

These outputs should be produced in a form suitable for inspection, reruns, and manuscript-support or preprint-support packaging.

## Interpretation boundaries

The benchmark outputs in this repository must not be interpreted as:

- a claim of solved delivery
- a substitute for wet-lab validation
- evidence of universal generalization

The intended interpretation is narrower:

- early-stage computational evidence only
- benchmark-first candidate prioritization support
- transparent comparison of simple baselines under explicit provenance

## Future extensions

Possible future extensions include:

- richer feature sets
- more explicit source-aware splitting policies
- additional ranking diagnostics
- better dataset versioning and curation layers

Any such extension should remain subordinate to the benchmark contract and reproducibility requirements established here.

## Benchmark onboarding note

Real datasets and previously generated evidence packages should be onboarded with explicit provenance, documented label framing, and stable run identifiers before they are treated as benchmark evidence.
