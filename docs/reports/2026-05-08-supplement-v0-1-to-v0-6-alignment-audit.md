# Supplement v0.1 to Manuscript v0.6 Alignment Audit - 2026-05-08

## 1. Purpose and Scope

This report audits `docs/supplement/permea-first-paper-supplement-v0-1.md` against the current internal-preparation manuscript, `docs/paper/permea-first-paper-manuscript-v0-6.md`, and the public-safe artifact boundary documented in `docs/reports/2026-05-07-public-safe-artifact-manifest.md`.

Reviewed materials:

- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/reports/2026-05-07-supplement-export-v0-4-alignment-plan.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `references.bib`

This audit does not modify supplement, manuscript, reference, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, wet-lab validation, clinical claims, or final legal/license conclusions.

## 2. Current Supplement v0.1 Status

Verdict: internal-review safe, but not aligned enough to serve as the current v0.6 companion supplement without revision.

Supplement v0.1 is clearly marked as an internal-review supplement and preserves public bioRxiv **Hold / not submission-ready** status. It states that it does not approve public release of row-level datasets or row-level derived artifacts.

The main version issue is that the status note says the supplement supports manuscript v0.5. Since manuscript v0.6 is now the current internal-preparation manuscript on master, the supplement should be revised as v0.2 rather than treated as current.

## 3. Relationship to Manuscript v0.6

Supplement v0.1 shares the core metric surface and public-safety posture with manuscript v0.6:

- same 2,959-row benchmark surface
- same simple sequence-derived feature set
- same baseline model families
- same random-stratified aggregate metrics
- same leakage-aware sensitivity metrics
- same leakage audit summary counts
- same row-level artifact hold posture
- same dataset/source/license/redistribution unresolved status

However, manuscript v0.6 adds more explicit wording around:

- v0.6 internal-preparation status
- direct BBB-penetrating peptide comparator lineage
- adjacent compound-level BBB predictor separation
- B3Pred/B3Pdb lineage caution
- conservative Option A data/code availability posture
- final bibliography cleanup and source-to-claim blockers

Supplement v0.1 does not yet reflect those v0.6-specific source-to-claim improvements.

## 4. Version / Status Alignment Issues

High-risk version/status issues: none.

Medium-risk version/status issues for broader review:

- Supplement v0.1 states that it supports manuscript v0.5, not manuscript v0.6.
- The available supplement/export alignment plan is v0.4-specific and should be superseded by a v0.6/v0.2 plan or draft.
- Supplement v0.1 has no explicit statement that manuscript v0.6 is now the current internal-preparation manuscript.
- Supplement v0.1 has not incorporated the v0.6 source-to-claim audit conclusions.

Low-risk version/status issues:

- The supplement does not mention manuscript v0.6 filename/path.
- The supplement does not mention that v0.6 replaced v0.5 as the current internal-preparation manuscript.

## 5. Section Alignment Checklist

| Supplement v0.1 area | Alignment with v0.6 | Required v0.2 action |
| --- | --- | --- |
| Status note | Partially aligned; still references v0.5 | Update to v0.2 supporting manuscript v0.6 and keep internal-preparation / Hold language. |
| Scope and claim boundary | Aligned | Preserve no-SOTA, no-validation, no-redistribution, no-peer-review boundaries. |
| Dataset surface | Mostly aligned | Keep row count/fields, add v0.6 dataset caveats and TODOs for source/license/label-source criteria. |
| Feature representation | Aligned | Preserve non-mechanistic baseline framing. |
| Baseline models | Aligned | Preserve exact model families and config traceability. |
| Evaluation metrics | Aligned | Preserve ROC-AUC, PR-AUC, MCC rationale. |
| Random-stratified metrics | Aligned | Preserve values exactly. |
| Leakage audit summary | Aligned | Preserve aggregate counts only; avoid sequence-pair detail. |
| Leakage-aware sensitivity | Aligned | Preserve values exactly and bounded sensitivity wording. |
| Traceability matrix | Mostly aligned | Update release posture wording to match current Option A / candidate-after-review posture. |
| Figure/table inventory | Partially aligned | Add caption readiness requirements and v0.6-specific figure/table mapping. |
| Release allow/hold matrix | Aligned | Preserve and expand to mirror manifest blocklist. |
| Data/code caveats | Partially aligned | Replace with or explicitly align to the conservative Option A availability wording used by v0.6. |
| Limitations/blockers | Mostly aligned | Add bibliography cleanup, final v0.6 source-to-claim approval, and founder/manual public-posting decision blockers. |

## 6. Public-Safe Artifact Compliance Check

Verdict: pass for internal-review use; public-facing release remains blocked.

Supplement v0.1 uses aggregate-safe summaries and path-level artifact references. It avoids presenting row-level peptide sequences, labels, predictions, rankings, split manifests, group assignments, or sequence-pair leakage tables.

The supplement's allow/hold matrix is consistent with the public-safe artifact manifest:

- aggregate metrics are candidates only after review
- aggregate leakage/sensitivity summaries are candidates only after review
- summary figures are candidates only after review
- processed row-level datasets are not publicly redistributable without explicit permission
- row-level predictions/rankings remain on Hold
- split manifests/group assignments remain on Hold
- sequence-pair leakage CSVs are not publicly redistributable without explicit permission

Required v0.2 improvement: mirror the manifest's blocklist more completely, including row-level processed datasets, row-level labels, upstream dataset mirrors, row-level derived artifacts linkable to restricted source rows, and candidate-ranking preview artifacts.

## 7. Row-Level Artifact Exposure Check

Verdict: no row-level artifact contents found in supplement v0.1.

Supplement v0.1 includes dataset field names, row count, and internal path-level traceability to processed dataset and result artifacts. It does not include row-level peptide sequences, row-level labels, row-level predictions, ranking tables, split manifests, group assignments, or sequence-pair leakage CSV contents.

Caution: supplement v0.1 names restricted row-level artifact paths for internal traceability. That is acceptable for internal review, but any public-facing supplement/export should either omit those paths or keep them clearly marked as internal traceability only and not publicly redistributed.

## 8. Dataset / Provenance Caveat Check

Verdict: pass with required v0.2 tightening.

Supplement v0.1 states that processed dataset redistribution is not declared available and that dataset availability depends on source terms, attribution, licensing, label-source criteria, and manual review.

Required v0.2 changes:

- Add the v0.6 TODO boundary for original dataset source/citation/license/label-source criteria.
- State that no row-level processed dataset redistribution is declared for the current version.
- State that public reproducibility may remain aggregate-only if row-level dataset redistribution is not approved.
- Preserve that dataset redistribution remains unresolved.

## 9. Result / Metric Traceability Check

Verdict: pass.

The metric values in supplement v0.1 match manuscript v0.6 for both random-stratified and leakage-aware sensitivity summaries:

- Random-stratified Logistic Regression: ROC-AUC 0.8605, PR-AUC 0.4903, MCC 0.3618.
- Random-stratified Random Forest: ROC-AUC 0.8489, PR-AUC 0.5002, MCC 0.4331.
- Leakage-aware Logistic Regression: ROC-AUC 0.8587, PR-AUC 0.5024, MCC 0.3747.
- Leakage-aware Random Forest: ROC-AUC 0.8718, PR-AUC 0.5807, MCC 0.5084.
- Relative deltas match manuscript v0.6.

The supplement correctly treats these as aggregate result references and bounded sensitivity summaries, not proof of leakage-free status or robust generalization.

## 10. Direct Peptide Comparator Context Check

Verdict: incomplete for v0.6 alignment.

Manuscript v0.6 contains a distinct direct BBB-penetrating peptide comparator context, including B3Pdb/B3Pred lineage and related peptide predictor references. Supplement v0.1 does not yet include a direct peptide comparator citation/context section.

Required v0.2 changes:

- Add a direct peptide comparator context section aligned with manuscript v0.6.
- Preserve the boundary that direct peptide predictor citations are lineage/context only.
- Do not imply matched dataset, split, label, or metric comparability.
- Do not imply Permea outperforms prior BBB-penetrating peptide predictors.
- Keep B3Pred/B3Pdb lineage cautious and avoid any dataset redistribution permission claim.

## 11. Adjacent Compound BBB Predictor Context Check

Verdict: incomplete for v0.6 alignment.

Manuscript v0.6 explicitly separates adjacent compound-level BBB predictors from direct peptide comparators. Supplement v0.1 does not include this separation.

Required v0.2 changes:

- Add an adjacent compound BBB predictor context section or table aligned with manuscript v0.6.
- State that LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB are adjacent compound/SMILES BBB contexts, not direct peptide-focused comparators for this benchmark.
- Keep these references out of metric-comparison or leaderboard framing.

## 12. Figure / Table / Caption Readiness Check

Verdict: not export-ready.

Supplement v0.1 includes figure and table inventory placeholders but not final figure/table numbering, captions, path checks, export manifest, or final public-facing artifact allowlist.

Required v0.2 changes:

- Confirm whether figures are main-text or supplement figures.
- Finalize Figure S/Table S numbering.
- Draft captions with artifact path, artifact type, split/evaluation context, dataset/provenance caveat, and claim-boundary wording.
- Keep feature-importance captions explicitly model-level and non-mechanistic.
- Keep leakage-aware captions explicitly bounded to the committed sensitivity manifest.
- Keep candidate-ranking preview blocked unless explicit source/legal and claim-boundary approval is documented.
- Confirm each table excludes row-level sequences, labels, predictions, rankings, split manifests, group assignments, and sequence-pair leakage rows.

## 13. Export-Readiness Check

Verdict: not public-export-ready.

Supplement v0.1 preserves the major export blockers:

- public-safe artifact allowlist not final
- dataset source/license/redistribution decision not final
- figure/table numbering and captions not final
- source-to-claim review not final
- data/code availability wording not final
- founder/manual approval not final
- no export generated

For v0.2, the blocker list should be updated to reference manuscript v0.6, the v0.6 source-to-claim audit, Option A data/code availability wording, and the public-safe artifact manifest.

## 14. Required Supplement v0.2 Changes

Required before v0.2 can replace v0.1 as the current internal-review supplement:

1. Update status note from v0.5 support to v0.6 support.
2. Retitle/version as supplement v0.2 and mark it internal-review / not public-export-ready.
3. Preserve all metrics exactly.
4. Align data/code availability caveats with the conservative Option A posture used in manuscript v0.6.
5. Add direct peptide comparator context and B3Pred/B3Pdb lineage caution.
6. Add adjacent compound BBB predictor context and separation from direct peptide comparators.
7. Expand the public-safe artifact blocklist to match the public-safe artifact manifest.
8. Keep row-level processed datasets, labels, predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and linkable row-level derived artifacts blocked from public release.
9. Update figure/table inventory into a v0.6-aligned numbering/caption plan.
10. Add an export manifest placeholder or checklist.
11. Add bibliography/source-to-claim cleanup blockers from v0.6.
12. Preserve public bioRxiv **Hold / not submission-ready** status.

## 15. Internal-Review Safety Decision

Supplement v0.1 remains internal-review safe.

Reason: it uses aggregate summaries and path-level traceability, does not expose row-level artifact contents, preserves no-SOTA/no-validation boundaries, and clearly states that public bioRxiv remains **Hold / not submission-ready**.

Supplement v0.1 is not aligned enough with manuscript v0.6 to serve as the current companion supplement without revision. A supplement v0.2 should be drafted.

## 16. Risk Findings

### High-Risk Issues

None found.

### Medium-Risk Issues

- Supplement v0.1 references manuscript v0.5, while manuscript v0.6 is now current.
- Supplement v0.1 lacks v0.6-specific direct peptide comparator and adjacent compound predictor boundary sections.
- Supplement v0.1 has not adopted the current v0.6 Option A data/code availability wording.
- Figure/table/caption/export readiness remains incomplete.
- Dataset source/license/redistribution remains unresolved.
- Row-level artifact release decisions remain unresolved.

### Low-Risk Issues

- The supplement/export alignment plan is v0.4-specific and should be superseded.
- Supplement v0.1 uses candidate-after-review release posture correctly, but v0.2 should match the public-safe artifact manifest blocklist more completely.
- Supplement v0.1 contains path-level references to restricted artifacts; acceptable internally, but public-facing export should keep or omit them according to the final release policy.

## 17. Remaining Blockers

Public-facing supplement/export remains blocked by:

- dataset source, attribution, license, redistribution, and label-source criteria decisions
- row-level artifact release decision
- final data/code availability approval
- final source-to-claim approval
- supplement v0.2 drafting and audit
- figure/table numbering and caption review
- export manifest creation
- bibliography cleanup
- founder/manual approval
- final public posting decision

Public bioRxiv remains **Hold / not submission-ready**. Dataset redistribution remains unresolved. Row-level artifacts remain blocked from public release.

## 18. Recommended Next Task

Recommended next task: draft `docs/supplement/permea-first-paper-supplement-v0-2.md` from supplement v0.1 using this audit, manuscript v0.6, the v0.6 source-to-claim audit, the conservative Option A data/code availability posture, and the public-safe artifact manifest. Do not modify supplement v0.1.
