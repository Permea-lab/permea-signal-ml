# Supplement and Export Formatting Checklist v0.1

## Purpose

This checklist defines supplement and export formatting requirements before any bioRxiv v0.1 public posting decision.

This is not the final export package. It does not create PDF, DOCX, submission-bundle, website, or public archive files. It does not submit to bioRxiv, does not modify scientific content, does not change artifacts, and does not make the public preprint ready. Public preprint status remains **Hold / not submission-ready** until metadata, legal, reference, supplement/export, and human approval blockers are closed.

## Current Materials Inventory

| Item | Path | Current status | Ready for internal review? | Ready for public export? | Notes |
|---|---|---|---:|---:|---|
| Manuscript candidate | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` | Candidate prepared for human review | Yes | No | Metadata, disclosure, dataset/legal, reference, formatting, and approval blockers remain. |
| Supplement draft | `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` | Draft only | Yes | No | Needs final section, caption, path, and export-format review. |
| Supplement outline | `docs/SUPPLEMENTARY_OUTLINE_V0_1.md` | Planning outline | Yes | No | Useful for checking coverage against the prose supplement draft. |
| Draft bibliography | `references.bib` | Draft bibliography | Yes, with caveats | No | Human cleanup and final reference approval remain required. |
| Figures | `figures/` | Figure artifacts exist | Yes, with caveats | No | Caption, numbering, resolution, inclusion, and claim-boundary checks remain pending. |
| Result tables | `results/tables/` | Table artifacts exist | Yes, with caveats | No | Public table selection, captions, and formatting remain pending. |
| Leakage audit outputs | `results/audits/` | Audit outputs exist | Yes, with caveats | No | Appendix formatting and conservative leakage caveats remain required. |
| Metadata/disclosure input form | `docs/HUMAN_METADATA_AND_DISCLOSURE_INPUT_FORM_V0_1.md` | Human input form exists | Yes | No | Requires human completion; Codex must not fill final values. |
| Export package draft | `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md` | Draft manifest only | Yes | No | Not a final export bundle. |
| Readiness reassessment | `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md` | Current readiness status | Yes | No | States package is not submission-ready. |
| Artifact traceability report | `docs/FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md` | Internal traceability check | Yes | No | Useful source for artifact-to-claim review before public export. |

## Required Supplement Sections

- [ ] Dataset surface.
- [ ] Field definitions.
- [ ] Feature definitions.
- [ ] Model and evaluation setup.
- [ ] Metrics table.
- [ ] Leakage audit summary.
- [ ] Leakage audit output file list.
- [ ] Artifact inventory.
- [ ] Provenance caveats.
- [ ] Label-source caveats.
- [ ] Reproducibility command anchors.
- [ ] No-wet-lab boundary.
- [ ] Candidate-prioritization boundary.
- [ ] Limitations.

## Figure, Table, and Caption Checklist

| Figure/table class | Figure/table exists | Path documented | Caption exists | Caption overclaim check | Metric values match artifact | Leakage caveat included if relevant | Feature importance non-mechanistic if relevant | Public export filename stable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Model comparison table | Yes | `results/tables/model_comparison_summary.csv` | Draft references only | Pending | Must verify before export | Required | Not applicable | Pending |
| Random Forest feature-importance table | Yes | `results/tables/regenerated_rf_feature_importance.csv` | Draft references only | Pending | Must verify before export | If discussed with metrics | Required | Pending |
| Random Forest feature-importance figure | Yes | `figures/regenerated_rf_feature_importance.png` | Draft references only | Pending | Must verify against table | If discussed with metrics | Required | Pending |
| Dataset distribution figure | Yes | `figures/dataset_distribution.png` | Draft references only | Pending | Must verify against dataset docs | Class-imbalance caveat required | Not applicable | Pending |
| Legacy versus rerun metrics figure | Yes | `figures/legacy_vs_rerun_metrics.png` | Draft references only | Pending | Must verify against metric/table artifacts | Required | Not applicable | Pending |
| Benchmark workflow figure | Yes | `figures/benchmark_workflow_outputs.png` | Draft references only | Pending | Not metric-bearing unless caption states metrics | If benchmark status discussed | Not applicable | Pending |
| Candidate ranking preview figure | Yes | `figures/candidate_ranking_preview.png` | Draft references only | Hold for public use | Required to avoid biological validation implication | If metric-linked | Not applicable | Pending |
| Leakage audit tables | Yes | `results/audits/*.csv`; `results/audits/leakage_audit_summary.json` | Draft references only | Pending | Must verify against audit docs | Required | Not applicable | Pending |
| Score-distribution figures | Yes | `figures/legacy_bbb_*_score_distribution.png`; `figures/smoke_test_rf_score_distribution.png` | Not selected for current public package | Pending if used | Must verify if included | Required if used | Not applicable | Pending |
| Legacy feature-importance artifacts | Yes | `figures/legacy_rf_feature_importance*.png`; `results/tables/legacy_rf_feature_importance.csv` | Not selected for current public package | Pending if used | Must verify if included | If metric-linked | Required if used | Pending |

## Export Package Checklist

- [ ] Manuscript candidate file included or converted from `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`.
- [ ] Supplementary materials draft included or converted from `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`.
- [ ] `references.bib` included after human bibliography cleanup.
- [ ] Figure files selected, named, captioned, and checked.
- [ ] Result tables selected, named, captioned, and checked.
- [ ] Leakage audit outputs included or referenced with conservative interpretation.
- [ ] Data availability placeholders replaced with human-approved final text.
- [ ] Code availability placeholders replaced with human-approved final text.
- [ ] Metadata/disclosure placeholders replaced with human-approved final text.
- [ ] Claim-boundary audit included in internal export review packet.
- [ ] Citation consistency check included in internal export review packet.
- [ ] Readiness reassessment included in internal export review packet.
- [ ] Human approval checklist completed before public posting.

## Formatting Checklist

- [ ] Title and headings are consistent across manuscript, supplement, and export manifest.
- [ ] Citation placeholders are consistent with `references.bib`.
- [ ] `references.bib` is linked or included according to the final export route.
- [ ] Tables are named consistently.
- [ ] Figures are named consistently.
- [ ] File paths are relative and repo-valid.
- [ ] Internal links are not broken.
- [ ] Placeholder blocks remain clearly marked until human-completed.
- [ ] Public preprint status remains clearly **Hold / not ready** until final approval.
- [ ] No caption or heading implies biological validation, validated delivery, leakage-free status, robust generalization, therapeutic efficacy, clinical efficacy, or SOTA predictor status.

## Not-Yet-Ready Blockers

- Final author metadata.
- Disclosure statements.
- Dataset legal/licensing decision.
- Human bibliography cleanup.
- Final reference review.
- Final figure/table captions.
- Final supplement export formatting.
- Human approval.
- Optional leakage-aware sensitivity follow-up before any stronger benchmark claims.

## Minimal Export Readiness Path

1. Complete the human metadata and disclosure input form.
2. Complete dataset legal and availability wording.
3. Complete human reference cleanup for `references.bib`.
4. Complete supplement formatting pass.
5. Complete figure/table caption pass.
6. Rerun final claim-boundary and citation consistency checks.
7. Package manuscript, supplement, references, selected figures, selected tables, and audit outputs.
8. Obtain explicit human approval for public posting.

## Recommended Next Codex Task

Recommended next task: Task 069 - Commit Supplement and Export Formatting Checklist.

## No-Change Confirmation

- No final PDF, DOCX, submission bundle, website export, or public archive was created.
- Manuscript scientific content was not modified.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Metric values were not changed.
- Public preprint status remains **Hold / not submission-ready**.
