# Data and Code Availability Candidate Wording - 2026-05-08

## 1. Purpose

This document proposes conservative data/code availability wording candidates for manuscript v0.5 and later drafts. It does not modify the manuscript and does not make final legal, license, or release decisions.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Current Constraints

Current constraints:

- dataset redistribution remains unresolved
- exact upstream dataset files/version remain unresolved
- B3Pred/B3Pdb source terms/license remain unresolved
- required attribution wording remains unresolved
- original label-source criteria remain unresolved
- row-level processed datasets remain blocked from public release
- row-level derived artifacts remain blocked from public release
- supplement/export package remains incomplete
- final founder/manual approval remains pending

## 3. What May Be Released After Review

The following may be considered after founder/manual, source/legal, release-policy, and claim-boundary review:

- code
- environment and reproducibility instructions
- aggregate metrics
- aggregate figures
- non-row-level summaries
- public-safe documentation
- public-safe run manifests or schemas that do not expose restricted row-level information

Release of aggregate artifacts must not imply permission to redistribute the underlying processed dataset.

## 4. What Must Not Be Declared Publicly Available Yet

Do not declare these publicly available unless explicit permission and manual approval are documented:

- processed row-level datasets
- row-level labels
- row-level predictions
- rankings
- split manifests
- group assignments
- sequence-pair leakage artifacts
- upstream dataset mirrors
- row-level derived artifacts that can be linked back to restricted source rows

## 5. Candidate Wording Option A - Most Conservative

> Code and data availability are currently under internal review. Processed row-level datasets and row-level derived artifacts are not publicly redistributed with this draft. The manuscript uses aggregate metric summaries and path-level artifact traceability only. Dataset source, attribution, license, redistribution permission, original label-source criteria, and final data availability wording remain pending manual review. Public posting remains on Hold until these decisions are complete.

Use when:

- dataset/source/license decisions remain unresolved
- no public code release/tag has been approved
- no aggregate artifact allowlist has been approved

## 6. Candidate Wording Option B - Public-Safe Code + Aggregate Artifacts After Review

> Code supporting the benchmark workflow may be released through the Permea repository after final release review, repository URL confirmation, software license confirmation, and release tag/commit selection. Processed row-level datasets, row-level predictions, rankings, split manifests, group assignments, and sequence-pair leakage artifacts are not publicly redistributed. Selected aggregate metrics, aggregate figures, and non-row-level summaries may be released only after founder/manual, source/legal, and claim-boundary review. Dataset redistribution remains unresolved.

Use when:

- code release is approved or nearly approved
- aggregate artifact allowlist is approved or nearly approved
- processed row-level data remain blocked

## 7. Candidate Wording Option C - Future Release Candidate After Source / License Decision

> Code, aggregate benchmark summaries, and approved public-safe artifacts are available at [repository URL / release tag to be inserted after approval]. Dataset availability follows the documented source/license decision and approved data-release posture. Any row-level processed dataset or row-level derived artifact release is limited to artifacts with documented permission, required attribution, and manual approval. Artifacts not explicitly approved for release remain excluded from the public package.

Use only after:

- repository URL and release tag are confirmed
- software license is confirmed
- source/license decision is documented
- row-level release posture is approved
- attribution wording is approved
- founder/manual approval is recorded

Do not use this option in the current draft.

## 8. Notes on B3Pred / B3Pdb Lineage

B3Pred/B3Pdb citations support background, lineage, and direct peptide predictor context. They do not by themselves establish:

- local processed dataset redistribution permission
- exact local dataset provenance closure
- source terms/license for local processed artifacts
- original label-source criteria
- matched dataset or split comparability

Any public data availability statement should keep B3Pred/B3Pdb source and license decisions separate from general citation context.

## 9. Manual Approval Checklist

Before using wording beyond Option A, confirm:

- [ ] exact upstream dataset files/version
- [ ] B3Pred/B3Pdb source terms and license
- [ ] required attribution wording
- [ ] original label-source criteria
- [ ] processed dataset redistribution decision
- [ ] row-level derived artifact release decision
- [ ] code repository URL
- [ ] software license
- [ ] release tag/commit
- [ ] aggregate artifact allowlist
- [ ] row-level artifact blocklist
- [ ] founder/manual approval

## 10. Recommended Wording for Current Manuscript Draft

Recommended current option: **Option A - Most Conservative**.

Rationale:

- dataset redistribution remains unresolved
- row-level artifacts remain blocked
- code release tag/license wording is not final
- aggregate artifact allowlist is not final
- public bioRxiv remains Hold / not submission-ready

Option B can be considered after code release policy, aggregate artifact allowlist, and founder/manual review advance. Option C should be reserved for a later release candidate after source/license decisions are documented.

## 11. Explicit Status Statement

This document is not a final legal or license determination.

Dataset redistribution remains unresolved.

Row-level processed datasets and row-level derived artifacts remain blocked from public release unless explicit permission and manual approval are documented.

Public bioRxiv remains **Hold / not submission-ready**.
