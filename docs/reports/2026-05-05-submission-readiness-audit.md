# Permea Submission Readiness Audit - 2026-05-05

## Purpose

This report performs a documentation-only submission-readiness audit for the Permea bioRxiv v0.1 manuscript candidate. It covers SOD restore, current package status, blocker matrix, and recommended next tasks.

This report does not modify manuscript scientific content, rerun models, rerun leakage audit, generate new splits, change metric values, add benchmark results, approve public posting, or make legal conclusions.

## Current Repo State

| Field | Status |
| --- | --- |
| Local path | `/Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml` |
| Branch | `master` |
| Remote | `https://github.com/Permea-lab/permea-signal-ml.git` |
| Working tree before report creation | Clean |
| Latest local commit | `046b2d9 docs: add 2026-05-04 eod and 2026-05-05 sod handoff` |

## Previous Session Summary

The post-sensitivity package now includes:

- leakage-aware grouping utilities
- group assignment outputs
- split manifests
- leakage-aware baseline rerun outputs
- conservative findings investigation
- manuscript candidate and supplement updates with leakage-aware sensitivity findings
- final post-sensitivity claim/citation audit
- post-sensitivity founder/manual decision brief
- EOD/SOD handoff reports and next-session prompt files

## Current Scientific and Readiness Status

- Manuscript candidate: prepared for internal review.
- Supplement draft: prepared with leakage-aware sensitivity materials.
- Citation key consistency: passed.
- Final post-sensitivity claim/citation audit: passed.
- P0/P1 blockers: none for internal continuation.
- Public bioRxiv: **Hold / not submission-ready**.
- Website archive and partner/deck use: Hold pending separate claim-boundary review and approval.

## Current Evidence Summary

Leakage-aware sensitivity did not collapse the baseline signal under the committed group-stratified manifest. Logistic Regression remained broadly similar, and Random Forest was comparable to or higher than the random-stratified baseline under this manifest.

This supports a caveated computational preprint path after operational cleanup. It does not establish leakage-free status, robust generalization, biological validation, wet-lab validation, therapeutic efficacy, or clinical efficacy.

## Submission Blocker Matrix

| Area | Current status | Public submission impact | Next action |
| --- | --- | --- | --- |
| Author metadata | Placeholder / human input required | Blocking | Fill final author list, order, affiliations, corresponding author, email, ORCID decisions, and contribution statement. |
| Disclosures | Human input required | Blocking | Finalize funding, competing interests, acknowledgements, and ethics wording. |
| Dataset legal/licensing | Unresolved | Blocking | Decide source attribution, license, redistribution, public data route, and code/data availability wording. |
| Data/code availability | Draft options only | Blocking | Choose final statement aligned with legal/dataset decision and release policy. |
| `references.bib` cleanup | Draft bibliography; key consistency passed | Blocking | Complete human bibliography cleanup and source-to-claim review. |
| Supplement/export formatting | Draft supplement/checklist exist | Blocking | Finalize captions, file paths, figure/table selection, export manifest, and package format. |
| Final citation/source-claim review | Key-level pass; sentence-level review remains | Blocking | Verify every cited sentence supports only bounded claims. |
| Founder/manual approval | Required | Blocking | Review founder decision brief and approve or hold public path. |
| Public posting decision | Not approved | Blocking | Decide after all blockers close. |
| Claim boundary | Passed with caveats | Not blocking for internal continuation | Preserve computational-only language through final export. |
| Leakage-aware sensitivity | Completed under one grouping strategy | Supports internal continuation | Keep limitations visible; do not overclaim. |

## Submission Readiness Verdict

**Hold / not submission-ready.**

The package is strong enough for internal continuation and for a caveated computational preprint path after cleanup, but public posting remains blocked by metadata, disclosure, dataset legal/licensing, reference cleanup, supplement/export formatting, source-claim review, founder/manual approval, and final public posting decision.

## Recommended Next Tasks

1. Task 101 - Push Permea EOD/SOD Reports to Remote, if not already pushed with the correct GitHub account.
2. Task 102 - Prepare Metadata/Disclosure Completion Draft.
3. Task 103 - Prepare References Cleanup Workplan or Clean `references.bib` after verified metadata.
4. Task 104 - Final Supplement Export Formatting Pass.
5. Task 105 - Final bioRxiv Readiness Review.

## No-Change Confirmation

- Manuscript scientific content was not modified.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- Metric values were not changed.
- No public-preprint-ready, leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
