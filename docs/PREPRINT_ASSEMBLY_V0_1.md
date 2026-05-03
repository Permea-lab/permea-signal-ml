# Preprint Assembly v0.1

## Purpose

This document assembles the current preprint draft and its supporting assets into a practical package for later submission-oriented refinement. It is intended to clarify what the current manuscript is, which metadata remain placeholders, which figures and tables belong in the main text, and which items are more appropriate for supplementary treatment.

Submission readiness for this package is tracked in [BIORXIV_SUBMISSION_CHECKLIST_V0_1.md](./BIORXIV_SUBMISSION_CHECKLIST_V0_1.md).
Circulation-facing review guidance is documented in [CIRCULATION_GUIDE_V0_1.md](./CIRCULATION_GUIDE_V0_1.md) and [REVIEWER_NOTE_V0_1.md](./REVIEWER_NOTE_V0_1.md).

## Current manuscript status

The repository now contains a v0.1 evidence package, a paper package planning document, a preprint skeleton, a full prose preprint draft, a polished preprint draft, and a bioRxiv submission-readiness checklist. Together, these assets define the current BBB-oriented manuscript surface for internal review and later refinement.

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
- manuscript status: draft v0.1 with first polishing pass completed and front-matter placeholders added
- evidence status: bounded computational evidence package
- validation status: no experimental validation included

## Main-text figure and table plan

- Figure 1 — `dataset_distribution.png` — dataset distribution and class balance
- Figure 2 — `legacy_vs_rerun_metrics.png` — baseline comparison across imported and regenerated benchmark evidence
- Figure 3 — `regenerated_rf_feature_importance.png` — regenerated model-level Random Forest feature importance, not mechanistic evidence
- Figure 4 — `benchmark_workflow_outputs.png` — benchmark workflow / evidence package structure
- Table 1 — `model_comparison_summary.csv` — compact regenerated baseline comparison

## Suggested section-to-asset mapping

- Abstract / Results summary → `results/tables/model_comparison_summary.csv`; regenerated metrics JSON files under `results/metrics/`
- Methods / Dataset surface → `docs/DATASET.md`; run manifests under `results/manifests/`
- Methods / Workflow structure → `figures/benchmark_workflow_outputs.png`
- Results / Dataset and class balance → `figures/dataset_distribution.png`
- Results / Baseline comparison → `figures/legacy_vs_rerun_metrics.png`, `results/tables/model_comparison_summary.csv`
- Results / Model-level feature emphasis → `figures/regenerated_rf_feature_importance.png`, `results/tables/regenerated_rf_feature_importance.csv`
- Discussion / Evidence boundary → `docs/FIRST_EVIDENCE_SUMMARY.md`, `docs/V0_1_EVIDENCE_PACKAGE.md`

## Artifact-to-claim traceability

| Manuscript claim or evidence statement | Supporting artifact or document | Artifact status | Remaining caveat |
| --- | --- | --- | --- |
| Dataset size and feature surface | `docs/DATASET.md`; rerun-ready dataset surface | documented current evidence surface | public dataset version remains `pending_confirmation` |
| Split policy and seed | `docs/DATASET.md`; `results/manifests/*_manifest.json` | recovered benchmark setting | not a duplicate/similarity leakage-control claim |
| Model comparison metrics | `results/tables/model_comparison_summary.csv`; regenerated metrics JSON files under `results/metrics/` | regenerated current-contract artifacts | metric interpretation remains benchmark-level |
| PR-AUC under imbalance | `model_comparison_summary.csv`; preprint evaluation policy text | regenerated metric summary | class imbalance requires class-prior context |
| RF feature importance | `results/tables/regenerated_rf_feature_importance.csv`; `figures/regenerated_rf_feature_importance.png` | regenerated model-level artifact | not mechanistic evidence |
| Imported vs regenerated distinction | `docs/V0_1_EVIDENCE_PACKAGE.md`; summary tables and figures | documented evidence boundary | imported artifacts are continuity material |
| Candidate-prioritization boundary | `docs/PREPRINT_DRAFT_V0_1.md`; ranking outputs under `results/tables/` | current benchmark-output interpretation | not biological validation |

## Submission-gap checklist

- authorship metadata not finalized
- affiliations not finalized
- formal references not yet added
- provenance closure remains incomplete
- label-source criteria and duplicate/similarity leakage status remain unresolved
- supplementary appendix not yet drafted in full prose
- figure set is not yet fully publication-ready
- regenerated-only comparison figure remains optional / pending
- manuscript export format is not yet prepared

## Immediate next assembly steps

- decide what belongs in the appendix versus the main text
- replace metadata placeholders when authorship details are ready
- perform a figure numbering and caption pass
- prepare appendix text for imported versus regenerated artifacts
- prepare export-friendly manuscript formatting
