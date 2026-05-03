# Final Artifact Traceability and Export Check v0.1

## Purpose

This report checks artifact traceability and export-readiness after the internal maximum-harsh red-team review and post-red-team roadmap.

This is an internal artifact audit. It does not add new scientific evidence, add new benchmark results, change metric values, rerun models, or make public preprint submission ready by itself.

## Materials inspected

### Planning and review documents

- `docs/POST_RED_TEAM_NEXT_DEVELOPMENT_ROADMAP_V0_1.md`
- `docs/VIRTUAL_EXPERT_RED_TEAM_REVIEW_MAX_HARSH_V0_1.md`
- `docs/HARSH_REVIEW_POST_P1_P2_COUNCIL_CHECK_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_1_P2_PROVENANCE_BENCHMARK_CHANGELOG_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md`
- `docs/REVIEW_OPERATIONS_INDEX_V0_1.md`

### Manuscript and evidence documents

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/INTERNAL_REVIEW_MEMO_V0_1.md`
- `docs/CIRCULATION_GUIDE_V0_1.md`
- `docs/REVIEWER_NOTE_V0_1.md`

### Result artifacts and scripts

- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `results/tables/legacy_bbb_dummy_v01_ranking.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`
- `results/tables/legacy_bbb_dummy_v01_summary.csv`
- `results/tables/legacy_bbb_lr_v01_summary.csv`
- `results/tables/legacy_bbb_rf_v01_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/manifests/legacy_bbb_dummy_v01_manifest.json`
- `results/manifests/legacy_bbb_lr_v01_manifest.json`
- `results/manifests/legacy_bbb_rf_v01_manifest.json`
- `results/predictions/legacy_bbb_dummy_v01_predictions.csv`
- `results/predictions/legacy_bbb_lr_v01_predictions.csv`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`
- `figures/dataset_distribution.png`
- `figures/legacy_vs_rerun_metrics.png`
- `figures/regenerated_rf_feature_importance.png`
- `figures/benchmark_workflow_outputs.png`
- `figures/candidate_ranking_preview.png`
- `scripts/export_metrics.py`
- `scripts/generate_figures.py`
- `scripts/rank_candidates.py`
- `scripts/run_baseline.py`

## Artifact inventory

| Artifact path | Artifact type | Generated/imported/current status | Source script or source doc | Referenced by | Trusted review status | Public preprint status | Caveat |
|---|---|---|---|---|---|---|---|
| `docs/DATASET.md` | Dataset documentation | Current documentation | Documentation source | Manuscript, evidence package, assembly, checklist | Ready with caveats | Not yet | Dataset version remains `pending_confirmation`; attribution, licensing, label-source criteria, and leakage status remain unresolved. |
| `results/tables/model_comparison_summary.csv` | Model comparison table | Current regenerated summary table | `scripts/export_metrics.py` from metrics JSON files | Manuscript, evidence package, assembly | Ready | Ready with caveats | Supports benchmark-level metric statements only, not biological validation or delivery success probability. |
| `results/metrics/legacy_bbb_dummy_v01_metrics.json` | Dummy baseline metrics JSON | Current regenerated metric artifact | Existing benchmark rerun/export workflow | Assembly, evidence package, summary table | Ready | Ready with caveats | Dataset provenance caveats still apply. |
| `results/metrics/legacy_bbb_lr_v01_metrics.json` | Logistic Regression metrics JSON | Current regenerated metric artifact | Existing benchmark rerun/export workflow | Assembly, evidence package, summary table | Ready | Ready with caveats | Dataset provenance caveats still apply. |
| `results/metrics/legacy_bbb_rf_v01_metrics.json` | Random Forest metrics JSON | Current regenerated metric artifact | Existing benchmark rerun/export workflow | Assembly, evidence package, summary table | Ready | Ready with caveats | Dataset provenance caveats still apply. |
| `results/manifests/legacy_bbb_dummy_v01_manifest.json` | Dummy baseline manifest | Current manifest artifact | Existing benchmark rerun/export workflow | Dataset and assembly traceability | Ready with caveats | Not yet | Useful for traceability but does not close provenance or leakage questions. |
| `results/manifests/legacy_bbb_lr_v01_manifest.json` | Logistic Regression manifest | Current manifest artifact | Existing benchmark rerun/export workflow | Dataset and assembly traceability | Ready with caveats | Not yet | Useful for traceability but does not close provenance or leakage questions. |
| `results/manifests/legacy_bbb_rf_v01_manifest.json` | Random Forest manifest | Current manifest artifact | Existing benchmark rerun/export workflow | Dataset and assembly traceability | Ready with caveats | Not yet | Useful for traceability but does not close provenance or leakage questions. |
| `results/predictions/legacy_bbb_dummy_v01_predictions.csv` | Dummy baseline predictions CSV | Current prediction artifact | Existing benchmark rerun workflow | Evidence package and extended packet context | Ready with caveats | Optional supplement material | Not central to main manuscript metric claims. |
| `results/predictions/legacy_bbb_lr_v01_predictions.csv` | Logistic Regression predictions CSV | Current prediction artifact | Existing benchmark rerun workflow | Evidence package and extended packet context | Ready with caveats | Optional supplement material | Not central to main manuscript metric claims. |
| `results/predictions/legacy_bbb_rf_v01_predictions.csv` | Random Forest predictions CSV | Current prediction artifact | Existing benchmark rerun workflow | Evidence package and extended packet context | Ready with caveats | Optional supplement material | Not central to main manuscript metric claims. |
| `results/tables/legacy_bbb_dummy_v01_ranking.csv` | Dummy ranking table | Current ranking artifact | `scripts/rank_candidates.py` or existing ranking workflow | Candidate-prioritization support context | Ready with caveats | Optional supplement material | Candidate ranking is pre-experimental prioritization only. |
| `results/tables/legacy_bbb_lr_v01_ranking.csv` | Logistic Regression ranking table | Current ranking artifact | `scripts/rank_candidates.py` or existing ranking workflow | Candidate-prioritization support context | Ready with caveats | Optional supplement material | Candidate ranking is pre-experimental prioritization only. |
| `results/tables/legacy_bbb_rf_v01_ranking.csv` | Random Forest ranking table | Current ranking artifact | `scripts/rank_candidates.py` or existing ranking workflow | Candidate-prioritization support context | Ready with caveats | Optional supplement material | Candidate ranking is pre-experimental prioritization only. |
| `results/tables/legacy_bbb_dummy_v01_summary.csv` | Dummy model summary table | Current summary artifact | Existing ranking/summary workflow | Extended packet context | Ready with caveats | Optional supplement material | Secondary to canonical model comparison summary. |
| `results/tables/legacy_bbb_lr_v01_summary.csv` | Logistic Regression summary table | Current summary artifact | Existing ranking/summary workflow | Extended packet context | Ready with caveats | Optional supplement material | Secondary to canonical model comparison summary. |
| `results/tables/legacy_bbb_rf_v01_summary.csv` | Random Forest summary table | Current summary artifact | Existing ranking/summary workflow | Extended packet context | Ready with caveats | Optional supplement material | Secondary to canonical model comparison summary. |
| `results/tables/regenerated_rf_feature_importance.csv` | RF feature importance table | Current regenerated table | `scripts/export_metrics.py` | Manuscript, evidence package, assembly | Ready | Ready with caveats | Model-level feature importance only; not mechanistic proof. |
| `figures/regenerated_rf_feature_importance.png` | RF feature importance figure | Current generated figure | `scripts/generate_figures.py` | Manuscript, assembly, supplementary outline | Ready with caveats | Not yet | Needs final caption/export polish for public supplement. |
| `figures/dataset_distribution.png` | Dataset distribution figure | Current generated figure | `scripts/generate_figures.py` | Manuscript and assembly figure plan | Ready with caveats | Not yet | Needs final caption/export polish and provenance caveat alignment. |
| `figures/legacy_vs_rerun_metrics.png` | Legacy vs rerun metrics figure | Current generated figure | `scripts/generate_figures.py` | Assembly and evidence-package context | Ready with caveats | Not yet | Must keep imported vs regenerated distinction clear. |
| `figures/benchmark_workflow_outputs.png` | Benchmark workflow output figure | Current generated figure | `scripts/generate_figures.py` | Figure/export context | Ready with caveats | Not yet | Needs final export-bundle placement decision. |
| `figures/candidate_ranking_preview.png` | Candidate ranking preview figure | Current generated figure | `scripts/generate_figures.py` | Candidate-prioritization context | Ready with caveats | Hold for public use | Must not imply biological validation. |
| `docs/FIRST_EVIDENCE_SUMMARY.md` | Evidence summary document | Current documentation | Documentation source | Trusted review packet | Ready with caveats | Not final | Summarizes current computational evidence surface. |
| `docs/V0_1_EVIDENCE_PACKAGE.md` | Evidence package document | Current documentation | Documentation source | Trusted review packet | Ready with caveats | Not final | Needs final public supplement/export closure. |
| `docs/PREPRINT_ASSEMBLY_V0_1.md` | Preprint assembly document | Current documentation | Documentation source | Preprint assembly and artifact map | Ready with caveats | Not final | Provides traceability map but is not final submission packaging. |
| `docs/SUPPLEMENTARY_OUTLINE_V0_1.md` | Supplement outline | Current documentation | Documentation source | Preprint support | Ready with caveats | Not yet | Outline only; final supplement/export package still missing. |

## Claim-to-artifact map

| Claim or evidence statement | Document where claim appears | Supporting artifact/document | Traceability status | Caveat | Required action |
|---|---|---|---|---|---|
| Current dataset surface contains 2,959 rows. | `PREPRINT_DRAFT_V0_1.md`, `DATASET.md` | `docs/DATASET.md`; manifests provide run context | Traceable with caveat | Raw dataset file path and final version remain unresolved in public-facing docs. | Close dataset version/provenance or disclose unresolved status before public preprint. |
| Current feature surface includes `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, `aromaticity`, plus metadata fields. | `PREPRINT_DRAFT_V0_1.md`, `DATASET.md` | `docs/DATASET.md` | Traceable with caveat | Original label-source criteria are partially unresolved. | Harden dataset card and label-source documentation. |
| Evaluation used `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. | `PREPRINT_DRAFT_V0_1.md`, `DATASET.md` | `docs/DATASET.md`; `results/manifests/legacy_bbb_*_manifest.json` | Traceable with caveat | This is split-policy traceability, not leakage-control evidence. | Keep leakage caveat visible; add audit plan or audit output later. |
| Dataset class imbalance makes PR-AUC an important benchmark metric. | `PREPRINT_DRAFT_V0_1.md`, `FIRST_EVIDENCE_SUMMARY.md` | `results/tables/model_comparison_summary.csv`; `figures/dataset_distribution.png`; `docs/DATASET.md` | Traceable with caveat | PR-AUC interpretation remains benchmark-level. | Preserve claim-boundary language in manuscript and captions. |
| Dummy baseline PR-AUC is approximately 0.0909. | `PREPRINT_DRAFT_V0_1.md` | `results/tables/model_comparison_summary.csv`; `results/metrics/legacy_bbb_dummy_v01_metrics.json` | Traceable | None beyond dataset caveats. | No immediate action. |
| Logistic Regression shows ROC-AUC approximately 0.8605, PR-AUC approximately 0.4903, and MCC approximately 0.3618. | `PREPRINT_DRAFT_V0_1.md` | `results/tables/model_comparison_summary.csv`; `results/metrics/legacy_bbb_lr_v01_metrics.json` | Traceable | Metrics do not establish biological validation. | No immediate action. |
| Random Forest shows ROC-AUC approximately 0.8489, PR-AUC approximately 0.5002, and MCC approximately 0.4331. | `PREPRINT_DRAFT_V0_1.md` | `results/tables/model_comparison_summary.csv`; `results/metrics/legacy_bbb_rf_v01_metrics.json` | Traceable | Metrics do not establish delivery success probability. | No immediate action. |
| RF feature importance order is `gravy`, `aromaticity`, `pI`, `length`, `charge`. | `PREPRINT_DRAFT_V0_1.md`, `V0_1_EVIDENCE_PACKAGE.md` | `results/tables/regenerated_rf_feature_importance.csv`; `figures/regenerated_rf_feature_importance.png` | Traceable | Model-level importance only; not mechanistic proof. | Keep figure caption and text non-mechanistic. |
| Imported historical artifacts and current regenerated artifacts are distinct. | `V0_1_EVIDENCE_PACKAGE.md`, `PREPRINT_ASSEMBLY_V0_1.md` | `results/metrics/legacy_*`; `results/tables/model_comparison_summary.csv`; `figures/legacy_vs_rerun_metrics.png` | Traceable with caveat | Distinction is documentation-supported but final export bundle should make it easier to inspect. | Create reviewer-readable artifact inventory/export bundle later. |
| Candidate ranking supports prioritization before experimental validation. | `PREPRINT_DRAFT_V0_1.md`, `PREPRINT_ASSEMBLY_V0_1.md` | `results/tables/legacy_bbb_*_ranking.csv`; `figures/candidate_ranking_preview.png` | Traceable with caveat | Ranking is computational prioritization only, not biological validation. | Keep public-facing text bounded; consider excluding preview from public material until claim-aligned. |
| No wet-lab validation has been performed. | `PREPRINT_DRAFT_V0_1.md`, `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`, review packet docs | Documentation boundary statement | Traceable as documentation boundary | This is a scope statement, not a generated artifact claim. | Preserve boundary in all export and deck materials. |
| Dataset provenance, attribution/licensing, and label-source criteria remain unresolved or partially unresolved. | `DATASET.md`, `PREPRINT_DRAFT_V0_1.md`, `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Documentation boundary statement; manifests provide run context only | Traceable with caveat | The caveat is explicit but not resolved. | Resolve or disclose before public preprint. |
| Duplicate, near-duplicate, and sequence-similarity leakage risks remain unaudited. | `DATASET.md`, `PREPRINT_DRAFT_V0_1.md`, `SUPPLEMENTARY_OUTLINE_V0_1.md` | Documentation caveat | Traceable with caveat | No leakage audit artifact is present. | Draft audit plan before claiming stronger generalization. |

## Export-readiness matrix

| Target | Status | Ready components | Missing components | Caveats | Required next action |
|---|---|---|---|---|---|
| Trusted review circulation | Ready with caveats | Manuscript draft, dataset doc, evidence summary, evidence package, model comparison table, feature importance table/figure, manifests, rankings, review packet docs | None blocking trusted review | Dataset version, attribution/licensing, label-source criteria, and leakage status remain unresolved. | Use current trusted review snapshot and disclose caveats. |
| Public preprint supplement | Not yet | Core tables, metrics JSON, manifests, key figures, supplementary outline | Final supplement/export package, final references and metadata, final dataset/provenance disclosure, leakage audit output or stronger limitation | Current package is computational and pre-experimental; public provenance/licensing closure is incomplete. | Complete provenance/label-source hardening and public supplement export plan. |
| Public website/project page | Hold | Bounded claim language and current artifact set exist | Public-facing page materials, claim-aligned figure captions, public artifact inventory | Public page could overread metrics unless tightly scoped. | Prepare a separate public-page claim-boundary checklist before publishing. |
| Public deck/partner materials | Hold | Current evidence package can inform a deck later | Deck/pitch/presentation materials are absent from `permea-signal-ml`; claim-aligned deck review cannot be performed | No public deck should imply validation, success probability, or solved delivery. | Import or recreate deck materials, then run a dedicated claim-alignment check. |

## Missing or ambiguous links

- The final raw dataset artifact path and final dataset version remain ambiguous in public-facing documentation; `docs/DATASET.md` records the current surface but leaves the version as `pending_confirmation`.
- Attribution and licensing remain unconfirmed; no artifact in the current package closes that issue.
- Original label-source criteria remain partially unresolved; current labels are usable for the recovered benchmark setting but are not independently verified biological truth.
- No duplicate, near-duplicate, or sequence-similarity leakage audit artifact is present.
- No standalone public supplement/export bundle currently packages all tables, figures, manifests, and caveats in one reviewer-readable directory or index.
- Figure/caption polish and final export naming are not complete for public preprint use.
- Deck, pitch, and partner-facing materials are absent from `permea-signal-ml`, so public deck/partner traceability cannot be cleared.

## No-change confirmation

- No result artifacts were modified.
- No metric values were changed.
- No model reruns were performed.
- No new benchmark results were introduced.
- No new biological validation claim was introduced.
- No external reviewer feedback was added.

## Remaining blockers before public preprint

- Close dataset version/provenance or disclose unresolved status in final public-facing language.
- Confirm or disclose attribution and licensing status.
- Clarify original label-source criteria as far as evidence allows.
- Run a leakage audit or preserve a strong limitation around duplicate, near-duplicate, and sequence-similarity leakage.
- Complete final references, metadata, author/affiliation placeholders, and disclosure placeholders.
- Prepare final supplement/export package with artifact inventory, table/figure captions, manifests, and claim-boundary notes.

## Recommended next Codex task

Recommended next task: Task 026 — Commit Final Artifact Traceability Export Check.

