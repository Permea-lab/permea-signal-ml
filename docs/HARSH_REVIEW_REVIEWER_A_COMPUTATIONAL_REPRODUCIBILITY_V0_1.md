# Harsh Review — Reviewer A Computational/Reproducibility v0.1

## Purpose

This is an internal harsh review from the computational/reproducibility perspective. It is not external reviewer feedback.

Reviewer A evaluates whether the current BBB-oriented manuscript package is benchmark-aware, artifact-traceable, and reproducibility-oriented enough for trusted review without expanding the current evidence boundary.

## Materials reviewed

- `PREPRINT_DRAFT_V0_1.md`
- `CIRCULATION_GUIDE_V0_1.md`
- `REVIEWER_NOTE_V0_1.md`
- `REVIEWER_PACKET_V0_1.md`
- `FIRST_REVIEW_WAVE_OUTREACH_PACKET_V0_1.md`
- `DATASET.md`
- `FIRST_EVIDENCE_SUMMARY.md`
- `V0_1_EVIDENCE_PACKAGE.md`
- `PREPRINT_ASSEMBLY_V0_1.md`
- `SUPPLEMENTARY_OUTLINE_V0_1.md`
- `REVISION_PRIORITY_FRAMEWORK_V0_1.md`
- `REVIEW_FEEDBACK_LOG_V0_1.md`
- `HARSH_REVIEW_COUNCIL_CHARTER_V0_1.md`
- `HARSH_REVIEW_ROUND_0_BASELINE_V0_1.md`
- `REVIEW_OPERATIONS_INDEX_V0_1.md`
- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/manifests/legacy_bbb_rf_v01_manifest.json`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`
- `results/metrics/smoke_test_rf_metrics.json`
- `results/manifests/smoke_test_rf_manifest.json`

## Reviewer A verdict

Verdict: Pass with major caveats.

The package is strong enough for trusted review, especially with Reviewer A receiving the extended packet by default. It is not yet strong enough for public preprint submission because provenance closure, label/source definition, leakage-risk discussion, and artifact traceability need sharper treatment before broader public scrutiny.

## Main computational concerns

- Dataset provenance is clear enough for trusted review but remains unresolved for public submission. `DATASET.md` and metrics manifests use `pending_confirmation` for dataset version.
- Label definition is not explained deeply enough for a harsh reproducibility reader. The current docs identify `label` as a field but do not fully define labeling source, criteria, or original construction.
- Split policy and seed are visible: `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` and seed `42` appear in manuscript and support artifacts.
- Class imbalance is acknowledged, and the Dummy PR-AUC of approximately `0.0909` is traceable to the summary table and metrics JSON.
- Metric selection is reasonable for trusted review, but PR-AUC and MCC should remain framed as benchmark summaries, not biological validity.
- Baselines are appropriate for a first bounded package, but the package should resist turning "baseline signal" into "model maturity."
- Leakage risk is not proven from inspected docs, but duplicate sequence, near-duplicate sequence, and sequence-similarity leakage risks are not explicitly ruled out. These are unresolved questions.
- Imported versus regenerated artifact distinction is consistently documented.
- Manuscript-level metrics are traceable to `results/tables/model_comparison_summary.csv` and the relevant metrics JSON files.
- Figure/table traceability exists but should be stress-tested before public submission.

## Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before trusted review? | Required before preprint? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-01 | P2 | Dataset provenance | Dataset version, attribution, and licensing remain unresolved. | `DATASET.md`; metrics/manifests show `dataset_version` as `pending_confirmation`. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md`; manifests | Keep limitation visible for trusted review; resolve or explicitly document before public preprint. | No | Yes |
| A-02 | P2 | Label definition | Label semantics and original labeling criteria are not sufficiently defined for reproducibility scrutiny. | `DATASET.md` lists `label` but does not define source criteria in detail. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Add a label-definition/provenance clarification before preprint if recoverable; otherwise state unresolved status. | No | Yes |
| A-03 | P2 | Leakage risk | Duplicate, near-duplicate, or sequence-similarity leakage risk is not assessed in current docs. | Split policy is documented, but no duplicate/similarity leakage audit was found. | `PREPRINT_DRAFT_V0_1.md`; future supplement | Treat as unresolved risk; do not claim leakage exists unless audited. | No | Yes |
| A-04 | P2 | Metric traceability | Manuscript metrics are traceable to result tables, but public readers may need explicit artifact path mapping. | `model_comparison_summary.csv`; metrics JSON files; manuscript source anchors. | `PREPRINT_DRAFT_V0_1.md`; `PREPRINT_ASSEMBLY_V0_1.md` | Add a compact artifact-to-claim mapping before public preprint. | No | Yes |
| A-05 | P2 | PR-AUC/MCC interpretation | Metrics are currently cautious, but should remain benchmark-level and class-imbalance-aware. | Manuscript discusses strong imbalance and Dummy baseline. | `PREPRINT_DRAFT_V0_1.md` | Preserve cautious metric language; avoid threshold or validation claims. | No | Yes |
| A-06 | P3 | Figure/table traceability | Figure and table plan exists but is not publication-polished. | `PREPRINT_ASSEMBLY_V0_1.md`; figures present in repo. | Figure captions; `PREPRINT_ASSEMBLY_V0_1.md` | Defer polish until after trusted review. | No | No |
| A-07 | P4 | Expanded modeling | New model families or additional features may be useful later but are outside this review-operation phase. | `REVISION_PRIORITY_FRAMEWORK_V0_1.md` classifies scope-expanding work as future work. | Future roadmap | Log as future work, not current fix. | No | No |

## Harsh questions for the authors

- Can all reported metrics be regenerated from current scripts, configs, and artifacts without undocumented steps?
- Is the recovered split policy sufficient to reduce leakage, or does sequence similarity require a stricter future split?
- Are labels and source provenance sufficiently defined for public preprint scrutiny?
- Does PR-AUC interpretation adequately account for class imbalance and class-prior behavior?
- Are feature importances interpreted only as model-level signals?
- Are imported artifacts visually and textually separated from regenerated current-contract artifacts everywhere a reviewer might look?
- Are smoke-test artifacts clearly separated from current evidence artifacts?

## Reviewer A recommended next actions

Must fix before wider circulation:

- None blocking trusted review circulation.

Should fix before preprint:

- Clarify label definition and provenance status.
- Add or reference a duplicate/near-duplicate leakage-risk note if an audit is available; otherwise mark it as unresolved.
- Strengthen artifact-to-claim mapping from manuscript metrics to result files.
- Keep PR-AUC and MCC language tied to benchmark-level interpretation.

Can defer to future work:

- New model families.
- Sequence-similarity split redesign.
- Additional datasets or external benchmarks.
- Wet-lab validation linkage.
