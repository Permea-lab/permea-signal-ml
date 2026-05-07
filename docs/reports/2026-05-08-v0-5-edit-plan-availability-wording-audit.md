# v0.5 Edit Plan and Availability Wording Audit - 2026-05-08

## 1. Purpose and Scope

This report audits the v0.5 source-to-claim edit plan and the data/code availability candidate wording before any manuscript edits are applied.

Reviewed files:

- `docs/reports/2026-05-08-manuscript-v0-5-source-to-claim-audit.md`
- `docs/reports/2026-05-08-v0-5-source-to-claim-edit-plan.md`
- `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`
- `docs/paper/permea-first-paper-manuscript-v0-5.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `references.bib`

This audit does not modify the manuscript, supplement, references, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts.

## 2. Current Working Tree State

Current worktree:

- Repository: `permea-signal-ml`
- Branch: `task050_paper_finalization_source_claim`
- Base: `origin/master`
- Current manuscript: `docs/paper/permea-first-paper-manuscript-v0-5.md`
- Current supplement: `docs/supplement/permea-first-paper-supplement-v0-1.md`

Before this report, the working tree contained three untracked documentation files from Tasks 051 and 052:

- `docs/reports/2026-05-08-manuscript-v0-5-source-to-claim-audit.md`
- `docs/reports/2026-05-08-v0-5-source-to-claim-edit-plan.md`
- `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`

This report adds one additional documentation-only audit file.

## 3. Edit Plan Audit

Audit result: pass.

The edit plan is safe to use as the basis for a future v0.6 manuscript draft because it preserves the required source-to-claim boundaries.

Observed safeguards:

- Metrics are explicitly preserved exactly.
- No-SOTA positioning is preserved.
- Direct peptide BBB permeability work is kept separate from adjacent small-molecule or compound BBB predictor work.
- B3Pred/B3Pdb lineage is treated cautiously and does not create a redistribution permission claim.
- Public bioRxiv status remains **Hold / not submission-ready**.
- Row-level processed datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, and sequence-pair leakage artifacts remain blocked from public release.
- Proposed wording narrows claims rather than expanding them.
- Dry-lab benchmark evidence is not described as wet-lab, in vivo, clinical, or externally validated evidence.

The plan is suitable for controlled manuscript editing, but the edits should be applied in a new v0.6 draft rather than by mutating v0.5 without a versioned manuscript update.

## 4. Data/Code Availability Wording Audit

Audit result: pass.

The candidate wording file separates:

- code and reproducibility instructions
- aggregate metrics and aggregate figures
- non-row-level summaries
- restricted row-level datasets and row-level derivatives

Option A is the safest current wording because it does not declare row-level processed data, labels, predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, or upstream dataset mirrors publicly available.

Option A also preserves these required boundaries:

- Dataset redistribution remains unresolved.
- The wording is not a final legal or license determination.
- Any future code or aggregate artifact release remains subject to review.
- Public bioRxiv remains **Hold / not submission-ready**.

Option B and Option C are useful future candidates, but they should not be used in the current manuscript until their stated review gates are complete.

## 5. Recommended Wording Option

Recommended current manuscript wording: Option A, the most conservative option.

Rationale:

- It matches the current unresolved dataset source/license/redistribution status.
- It avoids implying public release approval for processed row-level datasets or row-level derived artifacts.
- It allows future revision after source/license, artifact allowlist, repository tag, and manual approval decisions are documented.

Option B should be considered only after a public-safe code and aggregate artifact allowlist is approved.

Option C should be considered only after source/license and redistribution decisions are resolved and documented.

## 6. High-Risk Issues

None found.

The edit plan and availability wording do not claim public bioRxiv readiness, wet-lab validation, clinical efficacy, universal delivery prediction, dataset redistribution permission, or AlphaFold-level performance, adoption, or standardization.

## 7. Medium-Risk Issues

The following medium-risk blockers remain unresolved before public submission or a public artifact release:

- Exact upstream dataset source files/version remain unconfirmed.
- B3Pred/B3Pdb source terms, license, attribution, and redistribution permission remain unresolved.
- Row-level processed dataset and row-level derivative artifact release decisions remain unresolved.
- Final sentence-level source-to-claim approval remains pending.
- Supplement/export package remains incomplete.
- Bibliography metadata cleanup and final citation formatting remain pending.
- Founder/manual approval remains pending for manuscript, data/code availability, artifact allowlist, and public posting.

These are not failures of the edit plan. They are blockers that the edit plan correctly preserves.

## 8. Low-Risk Issues

- Option B and Option C could become unsafe if copied into the manuscript before their review gates are complete. The candidate wording file marks those gates clearly.
- The edit plan should be treated as a v0.6 drafting guide, not as final approval to alter v0.5 directly.
- Final formatting, figure/table numbering, supplement pointers, and export wording remain editorial cleanup items after claim boundaries are locked.

## 9. Safe-to-Use Decision for v0.6

Decision: safe to use for drafting a future v0.6 manuscript.

Conditions:

- Preserve all existing numeric results and metric values exactly unless a separate verified result update is approved.
- Apply Option A for current data/code availability wording.
- Keep public bioRxiv status as **Hold / not submission-ready**.
- Keep row-level processed datasets and row-level derived artifacts out of any public availability claim.
- Keep dry-lab evidence distinct from biological validation.
- Run a follow-up source-to-claim audit after the v0.6 draft is created.

## 10. Remaining Blockers

Public bioRxiv and public artifact release remain blocked by:

- dataset source/license/redistribution decision
- row-level artifact release decision
- final source-to-claim approval
- supplement/export completion
- bibliography metadata and formatting cleanup
- figure/table/caption public-safe review
- approved data/code availability wording
- founder/manual approval

Current required posture:

- Public bioRxiv remains **Hold / not submission-ready**.
- Dataset redistribution remains unresolved.
- Row-level artifacts remain blocked from public release.
- No wet-lab, in vivo, clinical, or universal delivery prediction claim is supported.

## 11. Recommended Next Task

Recommended next task: commit the Task 051-053 documentation package, then create a separate task to draft manuscript v0.6 from the audited edit plan using Option A data/code availability wording.
