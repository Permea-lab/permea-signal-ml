# Public-Safe Artifact Manifest - 2026-05-07

## 1. Purpose and Scope

This manifest classifies Permea first-paper artifacts by internal-review and public-release risk. It is documentation-only and does not approve public release, dataset redistribution, public bioRxiv posting, or legal conclusions.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Current Repo State

- Repository: `permea-signal-ml`
- Branch: `master`
- Latest task context commit: `4755959 docs: add internal review packet for manuscript v0.4`
- Current working manuscript: `docs/paper/permea-first-paper-manuscript-v0-4.md`
- Manuscript status: internal-review ready
- Dataset redistribution status: unresolved
- Row-level artifact release status: blocked pending explicit permission and manual approval
- Supplement/export status: not public-submission-ready

## 3. Artifact Inventory by Directory

### `docs/`

Documentation, manuscripts, reports, review packets, submission drafts, and historical readiness files.

Release posture:

- Safe to use internally.
- Public-facing release requires final claim-boundary and source-to-claim review.

### `docs/paper/`

Contains manuscript versions v0.1 through v0.4 and review snapshot materials. New v0.5 is prepared separately in this batch.

Release posture:

- Internal review only until blockers are closed.

### `docs/reports/`

Contains audit reports, readiness reports, reference plans, dataset risk audits, and supplement/export plans.

Release posture:

- Safe to expose internally.
- Public-facing release should be filtered for row-level paths, claim boundaries, and legal caveats.

### `docs/submission/`

Contains dataset/license, metadata, data/code availability, founder approval, and blocker decision drafts.

Release posture:

- Internal decision support only until founder/manual approval.

### `docs/review/`

Contains friendly/internal review packets and snapshot notes.

Release posture:

- Internal review only.
- Does not imply external expert review or peer review.

### `data/`

Contains synthetic example data and processed benchmark datasets.

Release posture:

- `data/examples/example_sequences.csv`: likely safe after review because it is documented as synthetic.
- `data/processed/*`: blocked from public redistribution without explicit source/license permission.
- `data/raw/`: no upstream raw dataset is present.

### `results/`

Contains aggregate metrics, run manifests, row-level predictions, rankings, leakage audit outputs, and leakage-aware sensitivity outputs.

Release posture:

- Aggregate summaries are candidates for release after review.
- Row-level predictions, rankings, split manifests, group assignments, and sequence-pair leakage files remain blocked.

### `figures/`

Contains dataset, workflow, metric, feature-importance, score-distribution, and candidate-ranking preview figures.

Release posture:

- Aggregate figures may be considered after review.
- Candidate-ranking preview remains blocked from public-facing export pending source/legal and claim-boundary review.

### `notebooks/`

Contains notebook workflow files for dataset assembly, feature extraction, baseline models, and candidate ranking.

Release posture:

- Internal workflow support.
- Public release requires review for row-level data assumptions, paths, and claims.

## 4. Safe to Expose Internally

- Manuscript drafts under `docs/paper/`
- Review packets under `docs/review/`
- Audit and planning reports under `docs/reports/`
- Submission decision drafts under `docs/submission/`
- Aggregate metric summaries under `results/metrics/`
- Aggregate model comparison tables under `results/tables/`
- Aggregate leakage/sensitivity summaries under `results/audits/` and `results/sensitivity/`
- Summary figures under `figures/`

Internal exposure does not imply public-release approval.

## 5. Likely Safe After Founder / Manual Review

Candidates for possible public package inclusion after founder/manual, source/legal, and claim-boundary review:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_dummy_v01_metrics.json`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/metrics/legacy_bbb_rf_v01_metrics.json`
- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/combined_group_stratified_split_summary.json`
- `results/sensitivity/grouping_summary_combined.json`
- `results/audits/leakage_audit_summary.json`
- selected aggregate figures such as `figures/dataset_distribution.png`, `figures/legacy_vs_rerun_metrics.png`, and `figures/regenerated_rf_feature_importance.png`

Required caveat: release of aggregate artifacts does not grant permission to redistribute the underlying processed dataset.

## 6. Hold Until Source / License Decision

- processed dataset path disclosures beyond documentation summaries
- row-level prediction and ranking derivatives
- row-level split and grouping derivatives
- any table or figure that can reveal row-level prioritization
- notebooks or scripts that assume public access to restricted row-level data
- data availability wording that implies public processed dataset release

## 7. Do Not Redistribute Publicly Without Explicit Permission

The following classes should not be redistributed publicly unless explicit source/license permission and founder/manual approval are documented:

- processed row-level peptide datasets
- rerun-ready processed row-level datasets
- row-level prediction files
- row-level ranking files
- split manifests containing row identifiers, labels, folds, or groups
- group assignment files containing normalized sequences or sequence IDs
- sequence-pair leakage audit files
- candidate-ranking preview artifacts

## 8. Row-Level Artifact Blocklist

Current blocklist:

- `data/processed/legacy_bbb_dataset_with_features.csv`
- `data/processed/legacy_bbb_dataset_with_features_rerun_ready.csv`
- `results/predictions/legacy_bbb_dummy_v01_predictions.csv`
- `results/predictions/legacy_bbb_lr_v01_predictions.csv`
- `results/predictions/legacy_bbb_rf_v01_predictions.csv`
- `results/sensitivity/leakage_aware_predictions.csv`
- `results/tables/legacy_bbb_dummy_v01_ranking.csv`
- `results/tables/legacy_bbb_lr_v01_ranking.csv`
- `results/tables/legacy_bbb_rf_v01_ranking.csv`
- `results/tables/smoke_test_rf_ranking.csv`
- `results/sensitivity/combined_group_stratified_split_manifest.csv`
- `results/sensitivity/group_assignments_combined.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `figures/candidate_ranking_preview.png`

## 9. Aggregate Artifact Allowlist Candidates

Candidate allowlist after review:

- `results/tables/model_comparison_summary.csv`
- `results/metrics/legacy_bbb_*_metrics.json`
- `results/sensitivity/leakage_aware_metrics_summary.json`
- `results/sensitivity/leakage_aware_model_comparison_summary.csv`
- `results/sensitivity/leakage_aware_model_comparison_per_fold.csv`
- `results/sensitivity/combined_group_stratified_split_summary.json`
- `results/sensitivity/grouping_summary_combined.json`
- `results/audits/leakage_audit_summary.json`
- `results/tables/regenerated_rf_feature_importance.csv`
- selected summary figures under `figures/`

These are candidates only. They require final review before public release.

## 10. Code Release Caveats

Code availability is separate from data availability.

Code may be released only after:

- repository URL and release tag/commit are confirmed
- software license is approved
- scripts are reviewed for restricted path assumptions
- examples avoid requiring row-level restricted data
- documentation avoids claiming public dataset redistribution

## 11. Public Package Recommendation

Recommended safest current posture:

- Do not release row-level processed datasets.
- Do not release row-level predictions, rankings, split manifests, group assignments, or sequence-pair leakage artifacts.
- Consider a code plus selected aggregate-artifact package only after founder/manual, legal/source, and claim-boundary review.
- Keep manuscript and supplement public submission on Hold until blockers close.

## 12. Manual Decision Checklist

- [ ] Confirm exact upstream dataset source files/version.
- [ ] Confirm B3Pred/B3Pdb source terms and license.
- [ ] Confirm required attribution wording.
- [ ] Confirm original label-source criteria.
- [ ] Decide whether any processed row-level data may be redistributed.
- [ ] Decide whether row-level derived artifacts may be redistributed.
- [ ] Approve aggregate artifact allowlist.
- [ ] Approve code release policy, license, tag, and archive.
- [ ] Approve final data/code availability wording.
- [ ] Approve final public package boundary.

## Required Posture

Row-level processed datasets, row-level predictions, rankings, split manifests, group assignments, and sequence-pair leakage CSVs remain blocked from public release. Dataset redistribution remains unresolved. Public bioRxiv remains **Hold / not submission-ready**.
