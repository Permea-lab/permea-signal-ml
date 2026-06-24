# P-FIGURE-004 Public-Safe Figure Export

Date: 2026-06-24

Status: public-safe aggregate figure export for review. Do not treat these as final publication figures.

## Purpose

This report documents public-safe export of aggregate-only and metadata-only P-SIGNAL figure assets. The export is intended for review through a public pull request.

## Exported Files

- `figures/p_signal_figures/figure_01_workflow_release_boundary.svg`
- `figures/p_signal_figures/figure_01_workflow_release_boundary.png`
- `figures/p_signal_figures/figure_02_aggregate_performance_comparison.svg`
- `figures/p_signal_figures/figure_02_aggregate_performance_comparison.png`
- `figures/p_signal_figures/figure_03_non_monotonic_classifier_interaction.svg`
- `figures/p_signal_figures/figure_03_non_monotonic_classifier_interaction.png`
- `figures/p_signal_figures/figure_04_calibration_threshold_operating_summary.svg`
- `figures/p_signal_figures/figure_04_calibration_threshold_operating_summary.png`
- `figures/p_signal_figures/figure_05_prioritization_at_k_summary.svg`
- `figures/p_signal_figures/figure_05_prioritization_at_k_summary.png`
- `figures/p_signal_figures/figure_06_source_lineage_overlap_risk.svg`
- `figures/p_signal_figures/figure_06_source_lineage_overlap_risk.png`
- `figures/p_signal_figures/figure_manifest.json`
- `figures/p_signal_figures/README.md`

## Figure Decision Matrix

| Figure | Decision | Basis | Claim boundary |
| --- | --- | --- | --- |
| Figure 1 workflow / release boundary | PUBLIC_EXPORT_READY_AFTER_REDACTION | Aggregate counts and artifact classes only; public-safe filenames and metadata used. | Aggregate-only workflow and release-boundary transparency. |
| Figure 2 aggregate performance comparison | PUBLIC_EXPORT_READY_AFTER_REDACTION | Aggregate model-comparison metrics only. | Aggregate benchmark-label evaluation only. |
| Figure 3 non-monotonic interaction | PUBLIC_EXPORT_READY_AFTER_REDACTION | Aggregate ESM2 35M / 150M classifier metrics only. | No universal model-scale claim. |
| Figure 4 calibration / threshold summary | PUBLIC_EXPORT_READY_AFTER_REDACTION | Aggregate calibration and threshold summaries only. | Probability use remains cautious. |
| Figure 5 prioritization-at-k summary | PUBLIC_EXPORT_READY_AFTER_REDACTION | Aggregate top-k summaries only. | Top-k hits are benchmark-label hits before experimental validation. |
| Figure 6 source lineage map | PUBLIC_EXPORT_READY_AFTER_REDACTION | Metadata-level source-card context only. | No source independence proof and no second-source validation claim. |

## Redactions And Sanitization

- Public filenames remove private draft suffixes.
- Public SVG titles remove private draft wording.
- Public PNG metadata was stripped during export.
- Public SVG text was checked for private paths, private infrastructure terms, row-level field names, and unsupported affirmative claims.

## Boundary Statement

These figures are aggregate-only or metadata-level. They contain no raw sequences, no row-level labels, no row-level predictions, no embeddings, no split manifests, no group assignments, and no sequence-pair leakage files.

No public dataset availability claim is made. No experimental validation claim is made. No independent validation claim is made.

## Claim Discipline

Allowed interpretation:

- Aggregate benchmark-label evaluation.
- Candidate prioritization before experimental validation.
- Metadata-level source context.
- Private/public release boundary.

Not claimed:

- Biological validation.
- Public row-level data release.
- Experimental confirmation.
- Independent validation.
- Operational probability use.
- Final publication readiness.

## Validation

Public validation should include:

- `git diff --check`
- `python3 -m pytest tests/test_p_figure_004_public_figures.py -q`
- Existing P-SIGNAL focused public artifact tests.
- Full public test suite.
