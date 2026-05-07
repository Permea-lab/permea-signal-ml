# Manuscript v0.6 Source-to-Claim Audit - 2026-05-08

## 1. Purpose and Scope

This report audits `docs/paper/permea-first-paper-manuscript-v0-6.md` for source-to-claim boundaries, citation support, data/code availability caution, no-SOTA positioning, row-level artifact restrictions, and internal-preparation readiness before commit.

Reviewed materials:

- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/paper/permea-first-paper-manuscript-v0-5.md`
- `docs/reports/2026-05-08-v0-5-source-to-claim-edit-plan.md`
- `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`
- `docs/reports/2026-05-08-v0-5-edit-plan-availability-wording-audit.md`
- `docs/reports/2026-05-08-manuscript-v0-5-source-to-claim-audit.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `references.bib`

This audit does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, wet-lab validation, clinical claims, or final legal/license conclusions.

## 2. Version and Status Check

Verdict: Pass.

Manuscript v0.6 is clearly marked as an internal-preparation manuscript draft derived from v0.5 using the audited source-to-claim edit plan and conservative data/code availability wording.

The version note and submission-readiness note preserve:

- public bioRxiv **Hold / not submission-ready**
- dataset/source licensing decisions pending
- final data/code availability approval pending
- final source-to-claim review pending
- supplement/export completion pending
- bibliography cleanup pending
- founder/manual approval pending

Manuscript v0.5 remains present and unchanged in this worktree.

## 3. Citation Key Existence Check

Verdict: Pass.

All actual bracketed citation keys used in manuscript v0.6 were found in `references.bib`:

- `arif2025deepb3pred`
- `augur_2024`
- `b3bpfn_2026`
- `b3pdb_2021`
- `b3pred_2021`
- `bbb_shuttle_review_2016`
- `bbppred_2021`
- `bbppredict_2022`
- `brainpeppass_2024`
- `brainpeps_2012`
- `chicco_jurman_2020_mcc`
- `esm_bbb_pred_2025`
- `kumar2022deepredbbb`
- `matplotlib_2007`
- `naseem2023bbbpep`
- `oliveira2026titanbbb`
- `pandas_2010`
- `parakkal2022deepbbbp`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `tang2025deepb3p`

The raw `@...` scan also detects `@permea` inside the corresponding-author email address. This is not a citation key.

## 4. Direct Peptide Comparator Claim Check

Verdict: Pass.

Direct peptide references remain limited to BBB-penetrating peptide comparator context and lineage. The manuscript keeps B3Pdb/B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, BrainPeps, BBPpred, BrainPepPass, ESM-BBB-Pred, and B3BPFN in a context role.

v0.6 strengthens the boundary by stating that direct peptide predictor citations provide lineage and context only and do not establish matched dataset, split, label, or metric comparability for the current benchmark.

The manuscript does not claim Permea outperforms these methods or that the evaluation is a matched leaderboard comparison.

## 5. Adjacent Compound Predictor Claim Check

Verdict: Pass.

Adjacent compound-level BBB predictors remain explicitly adjacent rather than direct comparators. LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB are described as related but different prediction surfaces.

The manuscript keeps the direct peptide predictor context separate from compound/SMILES BBB permeability work.

## 6. B3Pred / B3Pdb Lineage Claim Check

Verdict: Pass with unresolved provenance caveat.

B3Pdb and B3Pred are used for lineage and direct peptide predictor context only. v0.6 does not use B3Pdb/B3Pred citations to claim:

- local processed dataset redistribution permission
- exact provenance closure
- matched B3Pred benchmark comparison
- source/license resolution
- state-of-the-art status

The manuscript keeps exact upstream dataset source files/version, source terms, required attribution, original label-source criteria, and redistribution permission as unresolved items.

## 7. Result Claim Check

Verdict: Pass.

The v0.6 changes are wording-only relative to v0.5. Metric values are unchanged.

The result interpretation remains benchmark-scoped:

- Random-stratified metrics remain baseline benchmark-signal estimates.
- Leakage-aware values remain sensitivity estimates under the committed manifest.
- The sensitivity rerun is not described as proof of full leakage control or robust generalization.
- Feature importance remains model-level behavior, not mechanistic proof.
- No state-of-the-art, leaderboard, direct comparator, biological validation, or clinical performance claim is added.

## 8. Candidate Prioritization Check

Verdict: Pass.

Candidate prioritization remains explicitly pre-experimental. v0.6 states that the benchmark signal supports continued internal prioritization and review, but does not by itself justify biological, translational, or clinical claims.

The manuscript does not imply wet-lab validation, in-vivo validation, biological validation, therapeutic efficacy, clinical efficacy, external validation, expert review, or peer review.

## 9. Data / Code Availability Check

Verdict: Pass.

v0.6 applies the conservative Option A posture from `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`.

The Data and Code Availability section states:

- code and data availability are currently under internal review
- processed row-level datasets and row-level derived artifacts are not publicly redistributed with this draft
- manuscript traceability uses aggregate metric summaries and path-level artifact traceability only
- dataset source, attribution, license, redistribution permission, original label-source criteria, and final data availability wording remain pending manual review
- public posting remains on Hold until decisions are complete

The manuscript does not declare publicly available:

- row-level processed datasets
- row-level labels
- row-level predictions
- rankings
- split manifests
- group assignments
- sequence-pair leakage artifacts
- upstream dataset mirrors
- row-level derived artifacts linkable to restricted source rows

Aggregate metrics, aggregate figures, non-row-level summaries, and reproducibility instructions remain conditional on founder/manual, source/legal, release-policy, and claim-boundary review.

## 10. Supplement / Export Check

Verdict: Pass for internal preparation; public export remains blocked.

v0.6 keeps the supplement pointer and adds that the current supplement draft is internal-review only, uses aggregate summaries and path-level traceability, and is not a public supplement export.

Remaining supplement/export blockers remain visible:

- supplement section order and numbering
- figure and table captions
- file-path checks and export manifest
- final claim-boundary and citation checks after formatting
- confirmation that public-facing supplement materials exclude row-level sequences, labels, predictions, rankings, split manifests, group assignments, and sequence-pair leakage tables

## 11. Public-Readiness Check

Verdict: Pass.

v0.6 does not declare public bioRxiv readiness. Public preprint submission remains **Hold / not submission-ready**.

Remaining public-readiness blockers are explicit:

- dataset legal/licensing and redistribution decision
- data/code availability wording approval
- final dataset/source citation
- final `references.bib` cleanup and source-to-claim review
- final citation/source-claim review
- supplement/export formatting
- founder/manual approval
- final public posting decision

## 12. Unsupported or Weakly Supported Claims

No high-risk unsupported claim was found.

Bounded claims that remain suitable for internal preparation:

- learnable benchmark signal under the current artifact surface
- no collapse under the tested leakage-aware sensitivity manifest
- cautious candidate prioritization before experimental validation
- direct peptide predictor lineage and context

These remain bounded by dataset provenance, source/license, split, leakage, comparator, supplement/export, and public-release limitations.

## 13. Required Edits Before Broader Review

No blocking source-to-claim edit is required before committing v0.6 as the current internal-preparation manuscript.

Recommended later edits before broader/public review:

- complete final sentence-level source-to-claim review
- resolve dataset source/license/attribution/redistribution posture
- complete bibliography metadata cleanup
- align supplement numbering, captions, and export manifest
- finalize data/code availability wording after manual decisions
- complete founder/manual approval before any public posting

## 14. Risk Findings

### High-Risk Issues

None found.

### Medium-Risk Issues

The following unresolved blockers remain medium-risk for broader review or public submission:

- dataset source/license/redistribution remains unresolved
- row-level processed dataset and row-level derived artifact release decisions remain unresolved
- final source-to-claim approval remains pending
- supplement/export remains incomplete
- bibliography cleanup remains pending
- founder/manual approval remains pending

These are not v0.6 drafting defects. They are correctly preserved as blockers.

### Low-Risk Issues

- v0.6 is currently untracked and should be committed only with the audit report after review.
- Supplement v0.1 has not yet been revised to explicitly align with v0.6; this is expected because supplement editing was out of scope.
- Final editorial polishing may still be useful after blocker decisions are resolved.

## 15. Required Conclusion

v0.6 is suitable for internal preparation.

v0.6 should replace v0.5 as the current internal-preparation manuscript after commit.

v0.6 is not public bioRxiv-ready.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.

No high-risk claim issues were found.

## 16. Recommended Next Task

Recommended next task: commit manuscript v0.6 and this source-to-claim audit report, then open a documentation-only PR for review.
