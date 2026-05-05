# Public-Safe Paper Preparation Batch Audit - 2026-05-07

## 1. Purpose and Scope

This report audits the six-file Task 150 public-safe paper preparation batch before commit.

Audited Task 150 files:

- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/reports/2026-05-07-source-to-claim-final-review-draft.md`
- `docs/supplement/permea-first-paper-supplement-v0-1.md`
- `docs/paper/permea-first-paper-manuscript-v0-5.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/reports/2026-05-07-automated-public-safe-paper-prep-batch-summary.md`

This is an internal audit only. It is not a public-readiness approval, legal conclusion, external expert review, or peer review.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. File Creation Scope

Verdict: Pass.

The Task 150 batch created documentation-only files under:

- `docs/reports/`
- `docs/supplement/`
- `docs/paper/`
- `docs/submission/`

No data, result, figure, model, split, prediction, ranking, or leakage-audit artifact was created or modified.

## 3. Existing-File Modification Check

Verdict: Pass.

Observed status before this audit report:

- six untracked documentation files from Task 150
- no tracked-file diff
- no staged files

The v0.5 manuscript is a new file and does not overwrite v0.4, v0.3, v0.2, or v0.1.

## 4. v0.5 Claim-Boundary Check

Verdict: Pass.

Manuscript v0.5 preserves the required claim boundaries:

- in-silico computational study only
- no state-of-the-art claim
- no matched leaderboard claim
- no leakage-free claim
- no robust generalization claim
- no biological, wet-lab, in-vivo, therapeutic, or clinical validation claim
- public bioRxiv remains Hold / not submission-ready

The v0.5 edits are public-safety and clarity edits over v0.4, not new experiments or new scientific claims.

## 5. v0.5 Citation / Source-to-Claim Check

Verdict: Pass for internal preparation.

v0.5 preserves the citation keys already integrated in v0.4 and keeps direct peptide comparators separated from adjacent compound-level BBB predictors.

Direct peptide comparator context remains bounded to:

- `b3pdb_2021`
- `b3pred_2021`
- `bbppredict_2022`
- `naseem2023bbbpep`
- `augur_2024`
- `tang2025deepb3p`
- `arif2025deepb3pred`

Adjacent compound-level context remains bounded to:

- `shaker2021lightbbb`
- `tang2022deepb3`
- `kumar2022deepredbbb`
- `parakkal2022deepbbbp`
- `oliveira2026titanbbb`

Remaining caveat:

- final sentence-level source-to-claim approval is still pending.

## 6. v0.5 Data Availability Caution Check

Verdict: Pass.

v0.5 explicitly states:

- processed dataset redistribution is not declared available
- dataset availability depends on source terms, original attribution, licensing, and manual review
- row-level processed datasets, predictions, rankings, split manifests, group assignments, and sequence-pair leakage artifacts are excluded from the public-facing package unless explicit permission and manual approval are documented
- selected aggregate derived artifacts require founder/legal and claim-boundary review

This is consistent with the dataset redistribution risk audit and dataset availability decision package.

## 7. Supplement v0.1 Row-Level Artifact Exclusion Check

Verdict: Pass.

The supplement v0.1 draft does not include row-level peptide sequences, row-level labels, row-level predictions, ranking tables, split manifests, group assignments, or sequence-pair leakage CSV contents.

The supplement uses aggregate metric tables and path-level traceability only. It explicitly blocks:

- `results/audits/near_duplicate_pairs.csv`
- `results/audits/fold_similarity_leakage_summary.csv`
- `figures/candidate_ranking_preview.png`

## 8. Supplement v0.1 Aggregate-Only Posture Check

Verdict: Pass.

Supplement v0.1 uses aggregate summaries for:

- random-stratified metrics
- leakage-aware metrics
- leakage audit counts
- aggregate result traceability
- figure/table placeholders
- release allow/hold matrix

It remains internal-review only and not public-submission-ready.

## 9. Public-Safe Artifact Manifest Consistency

Verdict: Pass.

The artifact manifest is consistent with the dataset row-level provenance and redistribution risk audit:

- row-level processed datasets remain blocked
- row-level predictions and rankings remain blocked
- split manifests and group assignments remain blocked
- sequence-pair leakage CSVs remain blocked
- aggregate metrics and selected figures are only candidates after review
- dataset redistribution remains unresolved

## 10. Source-to-Claim Review Draft Consistency

Verdict: Pass with low-risk follow-up.

The source-to-claim draft correctly treats itself as a draft and does not declare public readiness. It preserves direct/adjacent comparator boundaries and distinguishes citation support from internal artifact support.

Low-risk follow-up:

- The draft names v0.4 as the primary manuscript source while also covering v0.4/v0.5. A later final source-to-claim pass should explicitly use v0.5 as the primary manuscript if v0.5 becomes the current working manuscript.

## 11. bioRxiv Blocker Checklist Status

Verdict: Pass.

The blocker checklist explicitly states:

- current status: Hold / not submission-ready
- current decision: No-Go for public bioRxiv submission
- final status: Hold / not submission-ready

It correctly keeps dataset/source/license, row-level artifact release, supplement/export, source-to-claim, and founder/manual approval as unresolved blockers.

## 12. No-SOTA / No-Validation / No-Public-Readiness Claim Discipline

Verdict: Pass.

The batch preserves:

- no SOTA claim
- no leakage-free claim
- no robust generalization claim
- no biological/wet-lab/in-vivo validation claim
- no therapeutic or clinical efficacy claim
- no external expert review or peer review implication
- no public bioRxiv readiness claim

Search hits for restricted phrases occur in negated, cautionary, or Hold-status contexts.

## 13. Remaining Blockers

Remaining blockers before broader review or public submission:

- exact upstream dataset files/version
- source terms/license and required attribution wording
- original label-source criteria
- processed dataset redistribution decision
- row-level derived artifact release decision
- final data/code availability wording
- final source-to-claim review
- older bibliography metadata cleanup
- supplement figure/table numbering, captions, and export manifest
- final founder/manual approval
- public posting decision

## 14. Risk Findings

### High-Risk Issues

None found.

### Medium-Risk Issues

- Dataset source/license/redistribution remains unresolved.
- Row-level artifact public release remains blocked.
- Final source-to-claim review remains pending.
- Supplement/export formatting remains incomplete.
- Public bioRxiv remains Hold / not submission-ready.

These are expected blockers and do not prevent committing the documentation batch.

### Low-Risk Issues

- The source-to-claim draft should be updated in a future final pass to make v0.5 the explicit primary manuscript source if v0.5 becomes current.
- Supplement v0.1 is structurally useful for internal review but still lacks final figure/table numbering, captions, and export manifest.
- v0.5 is clearer and safer than v0.4 for internal preparation, but it still requires final source-to-claim and founder/manual review before broader review.

## 15. Commit Readiness

Verdict: safe to commit.

The Task 150 batch is safe to commit as documentation-only preparation because:

- only new markdown files were created
- existing manuscript versions were not modified
- `references.bib` was not modified
- data, result, figure, model, split, prediction, ranking, and leakage-audit artifacts were not modified
- no models, audits, split generation, figures, PDFs, or exports were rerun or generated
- public-readiness and dataset redistribution blockers remain explicit

Recommended commit scope:

- the six Task 150 files
- this audit report

Suggested next commit message:

```text
docs: add public-safe paper preparation batch
```

## Required Conclusion

- Task 150 batch is safe to commit.
- Manuscript v0.5 should become the current working manuscript for internal preparation.
- Supplement v0.1 is safe for internal review only.
- Public bioRxiv remains **Hold / not submission-ready**.
- Dataset redistribution remains unresolved.
- Row-level artifacts remain blocked from public release.
