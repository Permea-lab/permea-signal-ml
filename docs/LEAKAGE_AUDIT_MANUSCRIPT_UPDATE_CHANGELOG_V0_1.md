# Leakage Audit Manuscript Update Changelog v0.1

## Purpose

This changelog records manuscript and evidence-documentation updates made after the first leakage audit and findings investigation.

This changelog does not change metric values, does not add biological validation, does not claim leakage-free status, and does not add new benchmark results beyond the already committed leakage audit outputs.

## Inputs

- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
- `results/audits/sequence_duplicate_audit.csv`
- `results/audits/label_conflict_audit.csv`
- `results/audits/near_duplicate_pairs.csv`
- `results/audits/sequence_similarity_summary.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `results/audits/source_group_leakage_summary.csv`
- `results/audits/leakage_audit_summary.json`

## Main findings reflected

- Exact duplicates: 4 exact duplicate sequence groups; all same-label and crossing reconstructed folds.
- Label conflicts: 0 normalized exact-sequence label-conflict groups.
- Near-duplicates: 73 same-label near-duplicate pairs; 56 cross reconstructed folds.
- High similarity: 33 same-label high k-mer Jaccard pairs; 29 cross reconstructed folds.
- Source/group limitation: only one observed source value, `legacy_bbb_import`, spanning all 5 folds; too coarse for group-aware split control.
- Overall interpretation: moderate benchmark optimism risk. Current metrics remain random-stratified baseline metrics and may be optimistic under similarity-aware splitting.

## Documents updated

| Document | Update type | Leakage finding reflected | Claim-boundary effect |
|---|---|---|---|
| `docs/PREPRINT_DRAFT_V0_1.md` | Manuscript wording | Same-label duplicate and high-similarity pairs cross folds; current metrics may be optimistic. | Reframes metrics as random-stratified baseline metrics, not leakage-aware generalization estimates. |
| `docs/FIRST_EVIDENCE_SUMMARY.md` | Evidence summary update | Audit counts and moderate optimism risk. | Keeps current signal claim bounded to baseline evidence under the recovered split. |
| `docs/V0_1_EVIDENCE_PACKAGE.md` | Evidence-boundary update | Audit outputs and investigation memo added as traceability anchors. | States that leakage-aware generalization is not established. |
| `docs/DATASET.md` | Dataset-card update | Exact duplicates, label-conflict result, near-duplicates, high-similarity pairs, and source limitation. | Clarifies that the dataset should not be described as leakage-free or group-controlled. |
| `docs/SUPPLEMENTARY_OUTLINE_V0_1.md` | Supplement planning update | Leakage audit tables added as supplement candidates. | Ensures future supplement includes leakage-audit caveats. |
| `docs/PREPRINT_ASSEMBLY_V0_1.md` | Assembly map update | Leakage report, investigation memo, and summary JSON added to asset map. | Marks leakage caveat as required in limitations. |
| `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Readiness checklist update | First audit completed, but moderate optimism risk remains. | Public preprint remains not submission-ready without conservative leakage reporting and other blocker closure. |
| `docs/INTERNAL_REVIEW_MEMO_V0_1.md` | Internal readiness update | First audit completed with moderate optimism risk. | Trusted review remains possible with caveats; public preprint remains not ready. |
| `docs/FINAL_ARTIFACT_TRACEABILITY_EXPORT_CHECK_V0_1.md` | Artifact inventory and traceability update | Leakage report, investigation memo, and audit summary JSON added. | Keeps audit outputs separate from model metrics and biological validation. |
| `docs/POST_RED_TEAM_NEXT_DEVELOPMENT_ROADMAP_V0_1.md` | Roadmap update | Leakage audit run completed; follow-up planning needed. | Adds leakage-aware split/sensitivity planning as a follow-up before stronger claims. |
| `docs/TRUSTED_REVIEW_CIRCULATION_PACKET_SNAPSHOT_V0_1.md` | Review packet update | Leakage audit docs added as optional Reviewer A context. | Makes optimism-risk caveat visible for computational review. |
| `docs/REVIEW_OPERATIONS_INDEX_V0_1.md` | Operations index update | Changelog and audit summary JSON referenced. | Provides routing for future review-operation use. |

## Remaining follow-up

- Plan leakage-aware or similarity-aware split sensitivity analysis.
- Decide whether manuscript/evidence docs should cite audit counts directly or primarily cite the audit report in public-facing text.
- Use grouped split only if richer source, family, assay, or cluster metadata becomes available.
- Complete final public preprint readiness review after leakage language, references, metadata, provenance/licensing, label-source, supplement, and export blockers are addressed.

## No-change confirmation

- No model metrics were changed.
- No baseline models were rerun.
- No data files were modified.
- No result artifacts were modified.
- No figure artifacts were modified.
- No biological validation claim was added.
