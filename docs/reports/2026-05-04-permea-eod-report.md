# Permea EOD Report - 2026-05-04

## Executive Summary

The post-sensitivity manuscript candidate package was prepared on 2026-05-04. Leakage-aware sensitivity analysis was completed, the manuscript candidate and supplement were updated with sensitivity findings, the final post-sensitivity claim/citation audit passed, and the post-sensitivity founder/manual decision brief was prepared.

The GitHub remote was pushed through commit `3f0d982 docs: add post-sensitivity founder decision brief`. Public preprint status remains **Hold / not submission-ready**.

## Completed Work Summary

### A. Evidence and Leakage Work

- Leakage-aware grouping utilities implemented.
- Leakage-aware group assignment outputs generated.
- Leakage-aware split manifests generated.
- Existing baseline models rerun under the committed leakage-aware split manifest.
- Leakage-aware findings investigated before manuscript updates.

### B. Manuscript and Supplement Work

- Manuscript candidate updated with leakage-aware sensitivity findings.
- Preprint draft updated with leakage-aware sensitivity findings.
- Supplement draft updated with leakage-aware manifest description, metrics table, comparison table, and limitations.
- Claim-boundary language tightened to keep the evidence computational and caveated.

### C. Review and Audit Work

- Internal harsh review and post-fix review completed earlier in the package flow.
- Final post-sensitivity claim/citation audit completed.
- Citation key consistency passed: 18 unique citation keys checked and present in `references.bib`.
- P0/P1 status: none for internal continuation.

### D. Readiness and Blocker Work

- Post-sensitivity founder/manual decision brief prepared.
- Human metadata/disclosure input form prepared.
- Dataset legal/availability options prepared.
- Final references cleanup checklist prepared.
- Supplement/export formatting checklist prepared.
- Final candidate status report prepared.

### E. GitHub Sync

- Latest pushed commit: `3f0d982 docs: add post-sensitivity founder decision brief`.
- Remote branch: `origin/master`.
- Remote URL: `https://github.com/Permea-lab/permea-signal-ml.git`.
- Sync status verified on 2026-05-05: remote `master` points to `3f0d982dc293083df47f310ea170cd16a3c3322c`.

## Key Metrics

### Random-Stratified Baseline Metrics

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | approximately 0.0909 | 0.0000 |
| Logistic Regression | approximately 0.8605 | approximately 0.4903 | approximately 0.3618 |
| Random Forest | approximately 0.8489 | approximately 0.5002 | approximately 0.4331 |

### Leakage-Aware Sensitivity Metrics

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

### Random-Stratified Versus Leakage-Aware Deltas

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

## Conservative Interpretation

- Leakage-aware sensitivity did not collapse the baseline signal under this specific group-stratified manifest.
- Logistic Regression remained broadly similar.
- Random Forest was comparable to or higher than its random-stratified baseline under this manifest.
- The sensitivity result strengthens confidence relative to the initial leakage concern.
- This is not leakage-free status.
- This is not robust generalization.
- This is not biological validation or wet-lab validation.

## Current Readiness

| Area | Status |
| --- | --- |
| Internal manuscript candidate | Prepared |
| Internal continuation | Go |
| Public bioRxiv | Hold |
| Website archive | Hold |
| Partner/deck use | Hold |
| External expert review | Not performed |
| Founder/manual approval | Required |

## Remaining Blockers

- Author metadata.
- Disclosures.
- Dataset legal/licensing/redistribution decision.
- Data/code availability wording.
- `references.bib` human cleanup.
- Final source-claim review.
- Supplement/export formatting.
- Founder/manual approval.
- Public posting decision.

## Final Repo State

| Field | Value |
| --- | --- |
| Local path | `/Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml` |
| Remote | `https://github.com/Permea-lab/permea-signal-ml.git` |
| Branch | `master` |
| Latest commit | `3f0d982 docs: add post-sensitivity founder decision brief` |
| Working tree status | Clean at verification before this report was created |
| Remote sync status | Remote `master` verified at `3f0d982dc293083df47f310ea170cd16a3c3322c` on 2026-05-05 |

## Next Recommended Work

The 2026-05-05 SOD should start from:

- `docs/PREPRINT_CANDIDATE_STATUS_REPORT_V0_1.md`
- `docs/POST_SENSITIVITY_FOUNDER_DECISION_BRIEF_V0_1.md`
- `docs/reports/2026-05-05-permea-sod-handoff.md`
- `docs/reports/2026-05-05-permea-operator-planning-sod-prompt.md`
- `docs/reports/2026-05-05-permea-maintainer-sod-prompt.md`

Recommended next tasks:

- Task 100 - Commit EOD/SOD Reports
- Task 101 - Push EOD/SOD Reports
- Task 102 - Prepare Metadata/Disclosure Completion Draft
- Task 103 - Clean `references.bib` after verified metadata
- Task 104 - Final Supplement Export Formatting Pass
- Task 105 - Final bioRxiv Readiness Review

## No-Change Confirmation

- Manuscript scientific content was not modified by this report.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- Metric values were not changed.
- No public-preprint-ready, leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
