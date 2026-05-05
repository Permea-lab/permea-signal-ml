# Permea Manuscript v0.3 BBB Landscape Positioning Audit - 2026-05-07

## Purpose

This report audits `docs/paper/permea-first-paper-manuscript-v0-3.md` for BBB landscape positioning, direct-versus-adjacent comparator classification, claim boundaries, citation/source TODO visibility, and internal-review readiness.

This is an internal audit only. It is not external expert review, peer review, public approval, or a public preprint readiness decision.

## Materials Reviewed

- `docs/paper/permea-first-paper-manuscript-v0-3.md`
- `docs/reports/2026-05-07-bbb-landscape-based-manuscript-change-plan.md`
- `docs/paper/permea-first-paper-manuscript-v0-2.md`
- `docs/paper/permea-first-paper-review-snapshot-v0-2.md`
- `docs/reports/2026-05-06-reference-cleanup-and-citation-plan.md`
- `docs/reports/2026-05-06-reference-cleanup-post-audit.md`
- `docs/submission/2026-05-06-dataset-attribution-and-availability-decision-package.md`
- `docs/reports/2026-05-06-supplement-export-formatting-plan.md`
- `references.bib`

No manuscript, bibliography, data, result, figure, model, split, or leakage-audit artifact was modified for this audit.

## Audit Checklist

### 1. Metadata Consistency

Verdict: Pass.

The manuscript preserves the confirmed metadata:

- Author: Albert Heekwan Kim
- Affiliation: Permea Research
- Corresponding author email: `a.kim@permea.us`
- Funding: No funding
- Conflict of Interest: N/A
- Acknowledgements: N/A
- Ethics Statement: N/A

No missing or invented metadata was detected.

### 2. Title and Abstract Positioning

Verdict: Pass with minor polish caveat.

The title frames the work as a reproducible peptide-focused baseline rather than a state-of-the-art BBB predictor. The abstract explicitly positions the study as an in-silico computational baseline/evidence package and states that the work does not present a new state-of-the-art BBB permeability predictor.

The abstract preserves the leakage-aware sensitivity metrics and does not reframe them as leaderboard performance.

Low-risk polish issue: the title is still relatively long and could be shortened during a later editorial pass without changing the claim boundary.

### 3. Introduction Scope Discipline

Verdict: Pass.

The introduction correctly narrows the landscape from generic BBB permeability prediction to BBB-penetrating peptide prediction. It states that compound-level BBB models are adjacent context and not the direct comparator class for this peptide-focused study.

The introduction maintains conservative language around:

- initial computational evidence
- peptide-focused BBB-related classification
- sequence-derived physicochemical features
- candidate prioritization before experimental validation

### 4. Related Work Completeness

Verdict: Pass for internal review, with source-required TODOs.

The new Related Work section materially improves the manuscript by separating:

- direct BBB-penetrating peptide predictor context
- adjacent compound-level BBB predictor context
- Permea's positioning relative to both groups

This is sufficient for internal review. It is not yet final for public submission because several comparator references still require source verification and bibliography integration.

### 5. Direct Peptide Comparator Classification

Verdict: Pass.

The manuscript correctly identifies direct peptide-focused comparators:

- B3Pdb / B3Pred
- BBPpredict
- BBB-PEP-prediction
- Augur
- DeepB3P
- DeepB3Pred

The manuscript appropriately states that Permea is positioned as a conservative, reproducible, peptide-focused baseline/evidence package in the B3Pdb/B3Pred lineage rather than as a state-of-the-art replacement for these systems.

### 6. Adjacent Compound BBB Predictor Classification

Verdict: Pass.

The manuscript correctly classifies the following as adjacent compound-level BBB predictor context:

- LightBBB
- Deep-B3
- DeePred-BBB
- DeepBBBP
- TITAN-BBB

The manuscript explicitly states that TITAN-BBB and DeePred-BBB are compound/SMILES BBB permeability work, not direct peptide predictors for this manuscript's sequence-derived peptide task.

### 7. No-SOTA Wording

Verdict: Pass.

The manuscript includes explicit no-SOTA language in the abstract, Related Work, Results interpretation, Discussion, and limitations. It does not claim state-of-the-art performance, does not present a matched leaderboard comparison, and does not imply superiority over B3Pred, BBPpredict, BBB-PEP-prediction, Augur, DeepB3P, DeepB3Pred, or compound-level BBB predictors.

### 8. Dataset Lineage Wording

Verdict: Pass with medium-risk unresolved blocker.

The manuscript strengthens dataset-lineage caution by stating that task comparability, source-label criteria, redistribution terms, and cross-paper dataset alignment remain unresolved.

Medium-risk blocker: original dataset source/citation/license/label-source criteria still require manual resolution before public submission.

### 9. Results Interpretation Discipline

Verdict: Pass.

The random-stratified and leakage-aware metric values are preserved and are interpreted as evidence of learnable signal within the internal benchmark surface. The manuscript does not convert these values into claims of validated BBB delivery, robust generalization, biological validation, clinical utility, or state-of-the-art performance.

The metrics remain:

| Setting | Model | ROC-AUC | PR-AUC | MCC |
| --- | --- | ---: | ---: | ---: |
| Random-stratified | Dummy | 0.5000 | 0.0909 | 0.0000 |
| Random-stratified | Logistic Regression | 0.8605 | 0.4903 | 0.3618 |
| Random-stratified | Random Forest | 0.8489 | 0.5002 | 0.4331 |
| Leakage-aware | Dummy | 0.5000 | 0.0909 | 0.0000 |
| Leakage-aware | Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Leakage-aware | Random Forest | 0.8718 | 0.5807 | 0.5084 |

Deltas are preserved:

- Logistic Regression: ROC-AUC -0.0018, PR-AUC +0.0121, MCC +0.0130
- Random Forest: ROC-AUC +0.0229, PR-AUC +0.0805, MCC +0.0753

### 10. Leakage-Aware Wording Discipline

Verdict: Pass.

The manuscript says the leakage-aware sensitivity analysis did not collapse under the tested group-stratified sensitivity setting. It does not describe the benchmark as leakage-free, fully controlled for leakage, or validated for robust generalization.

The remaining grouping caveats are visible, including the coarse grouping field, limited non-singleton grouping, and unresolved provenance questions.

### 11. Candidate-Prioritization Qualifier Discipline

Verdict: Pass.

Candidate-prioritization language remains qualified as pre-experimental and computational. The manuscript does not imply experimentally validated candidates, in-vivo activity, therapeutic effect, or clinical relevance.

### 12. Discussion and Limitations Discipline

Verdict: Pass.

The discussion emphasizes reproducibility, traceability, conservative baseline framing, and internal benchmark signal. The limitations appropriately state that:

- no wet-lab validation was performed
- no external validation was performed
- no robust generalization claim is made
- no matched cross-paper leaderboard comparison was performed
- dataset lineage and source comparability remain unresolved
- adjacent compound-level predictors target related but different prediction surfaces

### 13. Data/Code Availability Caution

Verdict: Pass.

The Data and Code Availability section remains conservative. It separates intended code availability from unresolved data availability and states that row-level processed dataset redistribution is not currently declared available.

The manuscript does not claim redistribution permission, does not make final legal conclusions, and preserves the requirement for founder/legal and claim-boundary review before any public data release.

### 14. Citation/Source TODO Visibility

Verdict: Pass for internal review, not complete for public submission.

The manuscript visibly marks source-required TODOs for unresolved reference needs:

- original dataset source/citation/license/label-source criteria
- BBB-PEP-prediction
- DeepB3P and DeepB3Pred if distinct from existing keys
- LightBBB
- Deep-B3
- DeePred-BBB
- DeepBBBP
- TITAN-BBB

Existing keys are used conservatively where already present, but final citation integration and source-to-claim review remain pending.

### 15. Public-Readiness Status

Verdict: Pass.

The manuscript preserves public bioRxiv status as Hold / not submission-ready. It states that public submission remains blocked by:

- source/citation verification
- dataset licensing and availability decisions
- supplement/export formatting
- final source-to-claim review
- founder/manual approval

Low-risk issue: the final submission-readiness note still refers to "internal first-paper v0.2 assembly" even though this file is v0.3. This is a version-label typo and should be fixed in the next revision or commit-prep task.

## Risk Summary

### High-Risk Issues

None found.

No leakage-free, robust-generalization, biological validation, wet-lab validation, in-vivo validation, therapeutic efficacy, clinical efficacy, public-readiness, external expert review, peer-review, or state-of-the-art claim was introduced.

### Medium-Risk Issues

1. Citation/source metadata remains unresolved for several landscape comparators, including BBB-PEP-prediction, potentially distinct DeepB3P/DeepB3Pred references, LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, and TITAN-BBB.
2. Original dataset source, citation, license, label-source criteria, and redistribution posture remain unresolved.
3. Supplement/export formatting remains incomplete and not public-submission-ready.
4. Final source-to-claim review is still required after any future bibliography additions.

### Low-Risk Issues

1. The v0.3 manuscript has one final status sentence that still references "v0.2 assembly"; this should be corrected before commit or in the next cleanup task.
2. The title is conservative and accurate but may still be long for final submission.
3. Related Work uses source-required TODO markers that are appropriate for internal review but should be resolved before broader review or public posting.

## Internal Review Readiness

Verdict: v0.3 is suitable for internal review.

Manuscript v0.3 improves over v0.2 by aligning the paper with the BBB-penetrating peptide predictor landscape, separating direct peptide comparators from adjacent compound-level BBB predictors, adding explicit no-SOTA wording, and strengthening dataset-lineage and cross-paper comparability limitations.

## Current Working Manuscript Recommendation

Verdict: v0.3 should replace v0.2 as the current working manuscript.

Rationale:

- v0.3 keeps the scientific metrics unchanged.
- v0.3 preserves conservative leakage-aware interpretation.
- v0.3 corrects the broader landscape positioning risk identified after v0.2.
- v0.3 makes the direct/adjacent comparator distinction visible to internal reviewers.

v0.2 should remain as a historical internal-review draft and review snapshot, but v0.3 should be the base for future manuscript edits.

## Dataset Availability Status

Dataset redistribution remains unresolved.

Current safe posture:

- Code availability may be prepared subject to final release review.
- Processed row-level dataset redistribution is not declared available.
- Dataset availability depends on source terms, original attribution, and manual licensing review.
- Selected aggregate derived artifacts may be considered only after founder/legal and claim-boundary review.

## Public Submission Status

Public bioRxiv remains Hold / not submission-ready.

No public-readiness decision should be inferred from this audit. Manuscript v0.3 is an internal working draft, not a public preprint.

## Recommended Next Task

Task 132 - Fix v0.3 Version Label and Commit BBB Landscape Package

Recommended scope:

- Correct the low-risk "v0.2 assembly" version-label typo in `docs/paper/permea-first-paper-manuscript-v0-3.md`.
- Stage and commit only:
  - `docs/reports/2026-05-07-bbb-landscape-based-manuscript-change-plan.md`
  - `docs/paper/permea-first-paper-manuscript-v0-3.md`
  - `docs/reports/2026-05-07-manuscript-v0-3-landscape-positioning-audit.md`
- Do not modify references, data, result, figure, model, split, or leakage-audit artifacts.

