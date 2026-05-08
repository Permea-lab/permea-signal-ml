# Permea EOD Report - 2026-05-05

## Date

2026-05-05

## Repository State

| Field | Value |
| --- | --- |
| Repo path | `/Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml` |
| Branch | `master` |
| Remote | `https://github.com/Permea-lab/permea-signal-ml.git` |
| Latest confirmed commit | `303caac docs: add submission readiness documentation package` |
| Final status after Task 106 | Clean, `master...origin/master` |

## Tasks Completed Today

- Restored 2026-05-05 SOD context from the EOD/SOD handoff documents.
- Prepared the submission-readiness documentation pass for Steps 1-5.
- Prepared the submission-readiness documentation pass for Steps 6-8.
- Committed and pushed the complete submission-readiness documentation package in Task 106.

## Files Created Today

Task 106 committed the following submission-readiness documentation files:

- `docs/reports/2026-05-05-submission-readiness-audit.md`
- `docs/reports/2026-05-05-reference-audit.md`
- `docs/reports/2026-05-05-export-readiness-check.md`
- `docs/submission/2026-05-05-dataset-license-review-draft.md`
- `docs/submission/2026-05-05-metadata-and-disclosures-draft.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`
- `docs/submission/2026-05-05-founder-approval-packet-v0-1.md`

This EOD package adds:

- `docs/reports/2026-05-05-permea-eod-report.md`
- `docs/reports/2026-05-06-permea-sod-handoff.md`
- `docs/prompts/2026-05-06-permea-operator-planning-sod-prompt.md`
- `docs/prompts/2026-05-06-permea-maintainer-sod-prompt.md`

## Commit Pushed in Task 106

- Commit: `303caac docs: add submission readiness documentation package`
- Push target: `origin/master`
- Push result: local `master` synchronized with `origin/master`.

## Current Scientific Status

- Manuscript candidate prepared.
- Supplement draft prepared.
- Draft `references.bib` prepared.
- Leakage audit completed.
- Leakage-aware sensitivity analysis completed.
- Citation key consistency passed.
- Claim-boundary audit passed.
- P0/P1 blockers: none for internal continuation.

Leakage-aware sensitivity findings remain bounded:

- Dummy ROC-AUC 0.5000, PR-AUC 0.0909, MCC 0.0000.
- Logistic Regression ROC-AUC 0.8587, PR-AUC 0.5024, MCC 0.3747.
- Random Forest ROC-AUC 0.8718, PR-AUC 0.5807, MCC 0.5084.
- Logistic Regression deltas: ROC-AUC -0.0018, PR-AUC +0.0121, MCC +0.0130.
- Random Forest deltas: ROC-AUC +0.0229, PR-AUC +0.0805, MCC +0.0753.

Interpretation: the leakage-aware group-stratified sensitivity rerun did not collapse the baseline signal under this specific grouping strategy. Logistic Regression remained broadly similar, and Random Forest was comparable to or higher than the random-stratified baseline under this manifest.

## Current Submission Status

Public bioRxiv remains **Hold / not submission-ready**.

The package is suitable for internal continuation. Public posting remains blocked until metadata, disclosures, dataset/legal decisions, data/code availability wording, bibliography cleanup, source-claim review, supplement/export formatting, founder/manual approval, and final public posting approval are completed.

## Unresolved Blockers

- Author list, author order, affiliations, corresponding author, email, ORCID, and contributions.
- Funding, competing interests, acknowledgements, and ethics statements.
- Dataset source attribution, licensing, redistribution, and legal review.
- Data and code availability wording.
- `references.bib` human cleanup and source-claim review.
- Supplement/export formatting.
- Founder/manual approval.
- Final public posting decision.

## Next Recommended Tasks

1. Task 108 - Restore 2026-05-06 Permea SOD context.
2. Task 109 - Review metadata/disclosure draft with founder input.
3. Task 110 - Resolve dataset legal and data availability wording.
4. Task 111 - Clean `references.bib` after verified reference metadata.
5. Task 112 - Perform final supplement/export formatting pass.
6. Task 113 - Run final bioRxiv readiness review after blockers close.

## Claim-Boundary Reminder

Do not claim:

- public preprint readiness
- leakage-free status
- robust generalization
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- final dataset licensing or redistribution permission
- external expert review or peer review

Allowed framing remains computational and caveated: the current package supports an internal computational benchmark-signal claim under documented limitations.

## Final Operating State

- Latest pushed commit before this EOD package: `303caac docs: add submission readiness documentation package`.
- Working tree after Task 106: clean.
- This EOD package is documentation-only and should be committed in a later task.
- No manuscript scientific content, `references.bib`, data files, result artifacts, or figure artifacts were modified by this EOD report.
