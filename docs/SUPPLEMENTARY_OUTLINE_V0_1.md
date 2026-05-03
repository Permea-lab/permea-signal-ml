# Supplementary Outline v0.1

## Purpose

This document defines the likely supplementary structure for the current BBB-oriented manuscript draft. It is intended as a compact planning layer for appendix and supplementary materials rather than as the supplement itself.

## Why supplementary structure is needed

The current manuscript depends on provenance clarification, benchmark-structure details, and imported-versus-regenerated distinctions that may be too detailed for the main text but remain important for trust and interpretability. A supplementary structure helps preserve those details without overloading the main manuscript body.

## Suggested appendix sections

- Appendix A — Dataset surface and field definitions
- Appendix B — Benchmark contract summary
- Appendix C — Imported versus regenerated artifact distinctions
- Appendix D — Additional metrics and artifact notes
- Appendix E — Provenance status and unresolved items
- Appendix F — Label-source criteria and leakage-risk status
- Appendix G — Figure-generation and export notes

## Suggested supplementary figures and tables

- supplementary table — full metric set across regenerated baseline outputs
- supplementary table — feature definitions and operational metadata fields
- supplementary figure — imported versus regenerated artifact mapping
- supplementary table — artifact inventory and output schema summary
- supplementary table — run/output schema summary for current-contract artifacts
- supplementary table — artifact-to-claim map for manuscript metrics and feature-importance statements
- supplementary note — unresolved provenance, label-source criteria, and duplicate/similarity leakage status

These items are suggested structure only. They should be treated as pending unless a corresponding asset already exists in the repository.

## Imported vs regenerated appendix note

Any supplementary package should explicitly preserve the distinction between imported historical artifacts and regenerated current-contract benchmark artifacts. Imported materials provide continuity and context, while regenerated artifacts define the present benchmark evidence surface. This distinction should remain visible in any appendix because it is central to how the repository supports present-tense interpretation.

## Provenance and leakage appendix note

The supplement should distinguish confirmed benchmark settings from unresolved provenance items. Confirmed settings include the current feature surface, recovered seed `42`, and recovered `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` evaluation policy. Unresolved items include public dataset version naming, attribution/licensing status, original label-source criteria, and duplicate/near-duplicate or sequence-similarity leakage status.

The current package should not claim that the dataset is fully provenance-closed, that labels are independently biologically validated, or that leakage has been ruled out unless a future audit supports those statements.

## Suggested repository anchors

- `docs/DATASET.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `figures/regenerated_rf_feature_importance.png`
- `results/manifests/`

## Immediate next steps

- decide what remains in the main text versus the supplement
- draft appendix prose for imported versus regenerated artifacts
- prepare a supplementary metric table
- prepare a supplementary provenance note
- prepare a label-source and leakage-risk note
- prepare an artifact-to-claim traceability table
