# Harsh Review Round 1 P2 Provenance and Benchmark Changelog v0.1

## Purpose

This changelog records focused P2 provenance and benchmark-clarity revisions made after the Round 1 internal harsh review.

This is an internal revision artifact. It is not external reviewer feedback, does not add new scientific evidence, does not add new benchmark results, and does not resolve all future validation needs. The edits documented here make current uncertainties more explicit and make existing artifacts easier to trace from manuscript and support-doc claims.

## Inputs

- `HARSH_REVIEW_ROUND_1_INTEGRATED_ISSUE_REGISTER_V0_1.md`
- `HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md`
- `HARSH_REVIEW_REVIEWER_A_COMPUTATIONAL_REPRODUCIBILITY_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`

## P2 worklist

| P2 issue ID | Source reviewer | Area | Risk summary | Affected document or artifact | Planned edit type | Status |
| --- | --- | --- | --- | --- | --- | --- |
| I-01 | A | Dataset provenance | Dataset version, attribution, licensing, and source metadata remain unresolved. | `DATASET.md`; metrics/manifests | Make confirmed and unresolved provenance items explicit without claiming closure. | Partially clarified; unresolved items remain |
| I-02 | A | Label definition | Label semantics and source criteria are not fully defined. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Clarify that `label` is the current supervised benchmark target and that original label-source criteria remain partially unresolved. | Partially clarified; unresolved items remain |
| I-03 | A | Leakage risk | Duplicate, near-duplicate, and sequence-similarity leakage risks are not assessed in current docs. | `PREPRINT_DRAFT_V0_1.md`; supplement planning | State that these risks are not documented as audited and avoid leakage-free claims. | Clarified as unresolved |
| I-04 | A | Artifact traceability | Manuscript metrics trace to artifacts, but public-facing artifact-to-claim mapping could be clearer. | `model_comparison_summary.csv`; metrics JSON; `PREPRINT_ASSEMBLY_V0_1.md` | Add explicit artifact-to-claim mapping and source-artifact references. | Clarified |
| I-08 | B/C | Platform ambition | Broader Permea framing could exceed current evidence if separated from limitations. | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Keep program-level context adjacent to current BBB-oriented computational evidence boundary. | Clarified |

## Edits applied

| Change ID | Linked P2 issue ID | Document edited | Section or local heading | Previous clarity gap | New clarity direction | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P2-C01 | I-01, I-02 | `DATASET.md` | Current dataset surface and label field status | Dataset version and label-source status were under-specified for reproducibility review. | Added dataset-surface identifier, `pending_confirmation` version status, label-field status, unresolved label-source criteria, and trusted-review versus preprint status. | Applied |
| P2-C02 | I-03 | `DATASET.md` | Leakage and duplicate-status note | Split policy could be overread as leakage control. | Clarified that `StratifiedKFold(... random_state=42)` is the recovered rerun policy, not a duplicate-removal or sequence-similarity-aware split claim. | Applied |
| P2-C03 | I-01, I-02, I-03 | `PREPRINT_DRAFT_V0_1.md` | Dataset surface, evaluation policy, and limitations | Main manuscript did not state provenance, label-source, and leakage-risk caveats with enough preprint-facing clarity. | Added concise notes that version, attribution/licensing, label-source criteria, and duplicate/similarity leakage status remain unresolved. | Applied |
| P2-C04 | I-04 | `PREPRINT_DRAFT_V0_1.md` | Output artifacts | Artifact-to-claim mapping was present mostly as source anchors. | Mapped manuscript metric claims to `model_comparison_summary.csv`, regenerated metrics JSON files, feature-importance table/figure, and manifests. | Applied |
| P2-C05 | I-04 | `PREPRINT_ASSEMBLY_V0_1.md` | Section-to-asset mapping and artifact-to-claim traceability | Assembly plan did not provide a compact artifact-to-claim table. | Added traceability table for dataset surface, split/seed, model metrics, PR-AUC interpretation, RF feature importance, imported/regenerated distinction, and candidate-prioritization boundary. | Applied |
| P2-C06 | I-01, I-02, I-03, I-04 | `SUPPLEMENTARY_OUTLINE_V0_1.md` | Suggested appendix sections | Supplement outline did not reserve explicit space for label-source, leakage-risk, or artifact-to-claim mapping. | Added appendix and table/note placeholders for provenance, label-source criteria, leakage-risk status, and artifact-to-claim mapping. | Applied |
| P2-C07 | I-01, I-02, I-03 | `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Provenance and benchmark-readiness status | Submission checklist named provenance closure but not the specific benchmark-readiness gaps. | Added current dataset identifier, `pending_confirmation` version status, split/seed, label-source, leakage, attribution/licensing, and artifact traceability notes. | Applied |
| P2-C08 | I-01, I-02, I-03 | `INTERNAL_REVIEW_MEMO_V0_1.md` | What is still unresolved and current recommendation | Internal memo did not spell out label-source and leakage-risk caveats. | Added unresolved label-source and duplicate/similarity leakage notes and reinforced Reviewer A extended-packet context. | Applied |
| P2-C09 | I-08 | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md` | Evidence surface and Permea context | Broader Permea program context could be read without enough current-wedge caveat. | Added language that the current package remains provenance-limited and that broader standard-layer context is architecture, not evidence of generalization. | Applied |
| P2-C10 | I-01 through I-08 | `HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md` | P2 plan | P2 statuses still showed all items as planned. | Marked P2 items as clarified, partially clarified, or still unresolved after this pass. | Applied |

## Artifact-to-claim map

| Claim or evidence statement | Supporting artifact or document | Artifact status | Remaining caveat | Preprint readiness status |
| --- | --- | --- | --- | --- |
| Dataset size and feature surface are defined for the current reruns. | `docs/DATASET.md`; rerun-ready processed dataset surface | current evidence surface documented | public dataset version remains `pending_confirmation`; attribution/licensing unresolved | Not yet closed |
| Confirmed feature fields are `sequence`, `label`, `length`, `charge`, `gravy`, `pI`, and `aromaticity`. | `docs/DATASET.md`; feature configs referenced by scripts | documented current benchmark surface | original label-source criteria remain partially unresolved | Needs explicit caveat |
| Split policy and seed are recovered as `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` and `42`. | `docs/DATASET.md`; `results/manifests/*_manifest.json` | recovered benchmark setting | not a duplicate-removal or sequence-similarity-aware split claim | Needs limitation note |
| Model comparison metrics support benchmark-level baseline comparison. | `results/tables/model_comparison_summary.csv`; regenerated metrics JSON files under `results/metrics/` | regenerated current-contract artifacts | no biological validation; metric interpretation remains class-imbalance-aware | Reviewable with caveat |
| PR-AUC interpretation is important under class imbalance. | `model_comparison_summary.csv`; `PREPRINT_DRAFT_V0_1.md` evaluation/results language | documented metric context | class-prior baseline should remain visible | Reviewable |
| RF feature importance is model-level behavior. | `results/tables/regenerated_rf_feature_importance.csv`; `figures/regenerated_rf_feature_importance.png` | regenerated current-contract artifact | not mechanistic proof | Reviewable with cautious caption |
| Imported and regenerated artifacts are distinct. | `docs/V0_1_EVIDENCE_PACKAGE.md`; `PREPRINT_DRAFT_V0_1.md`; legacy and regenerated tables/figures | documented evidence boundary | imported artifacts are continuity material, not current primary evidence unless regenerated | Reviewable |
| Candidate-prioritization outputs are computational filtering aids before experimental validation. | ranking outputs under `results/tables/`; `PREPRINT_DRAFT_V0_1.md` | current benchmark-output interpretation | not biological validation or delivery-performance proof | Reviewable with boundary |

## Remaining P2 work

Resolved as documentation clarity:

- artifact-to-claim mapping is clearer
- imported versus regenerated distinction is reinforced
- split policy, seed, PR-AUC/class-imbalance context, and metric-source mapping are clearer
- platform ambition is more visibly bounded by the current BBB-oriented computational wedge

Partially clarified but still unresolved:

- dataset version remains `pending_confirmation`
- attribution and licensing status remain unconfirmed
- original label-source criteria remain partially unresolved

Deferred to future audit:

- exact duplicate sequence audit
- near-duplicate sequence audit
- sequence-similarity leakage assessment

Deferred to future benchmark expansion:

- stricter sequence-similarity-aware splits, if later required
- new datasets, new model families, additional features, or broader barrier tasks

## Recommended next Codex task

Task 013 — Commit P2 Provenance and Benchmark-Clarity Revisions
