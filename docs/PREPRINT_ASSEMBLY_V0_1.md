# Preprint Assembly v0.1

## Purpose

This document assembles the current preprint draft and its supporting assets into a practical package for later submission-oriented refinement. It is intended to clarify what the current manuscript is, which metadata remain placeholders, which figures and tables belong in the main text, and which items are more appropriate for supplementary treatment.

## Current manuscript status

The repository now contains a v0.1 evidence package, a paper package planning document, a preprint skeleton, a first full prose preprint draft, and a polished preprint draft. Together, these assets define the current BBB-oriented manuscript surface for internal review and later refinement.

## Provisional title

Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark

## Author and affiliation placeholders

- Author 1 — placeholder
- Author 2 — placeholder
- Affiliation 1 — placeholder
- Affiliation 2 — placeholder
- Corresponding author — placeholder

## Suggested manuscript metadata

- title: `Initial Computational Evidence for Permeability-Related Signal in a BBB-Oriented Peptide Benchmark`
- short title / running title: `BBB-Oriented Permeability Signal Benchmark`
- keywords:
  - blood-brain barrier
  - peptide benchmark
  - permeability-related signal
  - sequence-derived physicochemical features
  - candidate prioritization
  - benchmark-first evaluation
  - reproducible evidence package
- abstract status: draft prose available
- manuscript status: draft v0.1 with first polishing pass completed
- evidence status: bounded computational evidence package
- validation status: no experimental validation included

## Main-text figure and table plan

- Figure 1 — `dataset_distribution.png` — dataset distribution and class balance
- Figure 2 — `legacy_vs_rerun_metrics.png` — baseline comparison across imported and regenerated benchmark evidence
- Figure 3 — `regenerated_rf_feature_importance.png` — regenerated Random Forest feature importance
- Figure 4 — `benchmark_workflow_outputs.png` — benchmark workflow / evidence package structure
- Table 1 — `model_comparison_summary.csv` — compact regenerated baseline comparison

## Suggested section-to-asset mapping

- Abstract / Results summary → `results/tables/model_comparison_summary.csv`
- Methods / Dataset surface → `docs/DATASET.md`
- Methods / Workflow structure → `figures/benchmark_workflow_outputs.png`
- Results / Dataset and class balance → `figures/dataset_distribution.png`
- Results / Baseline comparison → `figures/legacy_vs_rerun_metrics.png`, `results/tables/model_comparison_summary.csv`
- Results / Feature emphasis → `figures/regenerated_rf_feature_importance.png`, `results/tables/regenerated_rf_feature_importance.csv`
- Discussion / Evidence boundary → `docs/FIRST_EVIDENCE_SUMMARY.md`, `docs/V0_1_EVIDENCE_PACKAGE.md`

## Submission-gap checklist

- authorship metadata not finalized
- affiliations not finalized
- formal references not yet added
- provenance closure remains incomplete
- supplementary appendix not yet drafted in full prose
- figure set is not yet fully publication-ready
- regenerated-only comparison figure remains optional / pending
- manuscript export format is not yet prepared

## Immediate next assembly steps

- add a supplementary outline and decide what belongs in the appendix
- add structured running-title and metadata fields to the manuscript draft if needed
- perform a figure numbering and caption pass
- prepare appendix text for imported versus regenerated artifacts
- prepare export-friendly manuscript formatting
