# Dataset

## Scope

This document defines the expected dataset shape for Permea Signal ML v0.1. The repository is intentionally generic at this stage and does not assume one fixed public dataset package yet.

The goal is to establish a benchmark-ready schema that can support sequence-level dataset assembly, sequence-derived feature extraction, baseline modeling, and candidate ranking.

## Expected schema

The core dataset should be row-oriented, with one record per sequence-level observation or candidate.

Expected columns:

- `sequence_id`: stable record identifier
- `sequence`: primary sequence string
- `label`: task label for the current benchmark framing
- `source`: source dataset, publication, or collection reference
- `metadata`: structured metadata payload or metadata columns describing context

Additional recommended columns:

- `split`: train, validation, or test assignment when pre-defined
- `sequence_length`: optional cached length field
- `source_license`: source licensing note if redistribution constraints matter
- `notes`: optional curation or filtering notes

## Data handling expectations

- sequence records should be validated before feature extraction
- label semantics should be documented before benchmarking
- source references should remain attached to records or dataset versions
- dataset transformations should be versioned where possible

## Provenance and licensing

Dataset provenance and licensing must be respected throughout the workflow.

This includes:

- documenting where records came from
- preserving citation or attribution requirements
- avoiding redistribution of restricted content when permission is unclear
- recording versioned dataset references in run manifests

## v0.1 posture

The v0.1 repository is designed to support a narrow benchmark-oriented workflow. It should not be interpreted as a complete data platform or as evidence that a single dataset framing fully captures permeability-related biology.
