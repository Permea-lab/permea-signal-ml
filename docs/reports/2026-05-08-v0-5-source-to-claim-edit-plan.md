# Manuscript v0.5 Source-to-Claim Edit Plan - 2026-05-08

## 1. Purpose and Scope

This plan identifies future manuscript v0.5 edits needed before broader review or public-readiness consideration. It does not modify `docs/paper/permea-first-paper-manuscript-v0-5.md`.

Scope:

- preserve the current conservative manuscript posture
- identify exact manuscript areas needing later source-to-claim edits
- propose wording candidates for future manual application
- preserve dataset, release, and claim-boundary caveats

This is a planning document only. It does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, or final legal/license conclusions.

## 2. Current v0.5 Status

Manuscript v0.5 is suitable for internal preparation and continued source-to-claim review.

Current status:

- internal-preparation only
- not public bioRxiv-ready
- dataset redistribution unresolved
- row-level artifacts blocked from public release
- final source-to-claim approval pending
- supplement/export incomplete
- bibliography metadata cleanup pending

## 3. No-Change Principles

Future edits should preserve:

- all metric values exactly
- no-SOTA positioning
- direct peptide predictor vs adjacent compound predictor distinction
- row-level artifact hold posture
- public bioRxiv **Hold / not submission-ready** status
- no wet-lab, biological, in-vivo, therapeutic, or clinical validation claims
- no leakage-free or robust-generalization claims
- no dataset redistribution permission claim

Future edits should not add new scientific claims unless directly supported by citations, repository artifacts, or explicit limitations.

## 4. Section-by-Section Future Edit Checklist

### Title

Current title is acceptable. Keep the phrase peptide-focused and baseline-oriented.

Future edit candidate:

- No required change unless reviewers prefer replacing "BBB-related permeability signal" with "BBB-related peptide classification signal" for narrower framing.

### Abstract

Keep:

- no-SOTA framing
- leakage-aware sensitivity values exactly as written
- candidate-prioritization-before-validation boundary
- public Hold and data-release caveats

Possible future tightening:

> These results support a bounded computational benchmark-signal claim for internal preparation, not a leakage-free or externally validated generalization claim.

### Introduction

Keep:

- computational BBB-related peptide classification framing
- distinction between prioritization and experimentally demonstrated transport
- direct peptide predictor context

Possible future tightening:

> Throughout this manuscript, permeability language refers to the supervised computational label surface and not to independently validated BBB transport.

### Related Work

Keep:

- direct BBB-penetrating peptide predictor context
- adjacent compound BBB predictor context as adjacent only
- explicit non-use of `deepb3p3_2023`

Possible future tightening:

> Direct peptide predictor citations provide lineage and context only; they do not establish matched dataset, split, label, or metric comparability for the present benchmark.

### Methods

Keep:

- existing dataset surface description
- source/license TODOs
- no-rerun statement
- baseline model scope
- leakage-aware sensitivity limitations

Possible future tightening:

> The supervised target is treated as a benchmark label, not as independently verified biological truth.

### Results

Keep:

- metric tables exactly unchanged
- random-stratified and leakage-aware distinction
- no direct comparator claims

Possible future tightening:

> The leakage-aware sensitivity results are bounded to the committed manifest and should not be interpreted as proof that all sequence, source, or provenance leakage has been eliminated.

### Discussion

Keep:

- learnable computational signal claim
- candidate-prioritization-before-validation framing
- direct peptide context vs adjacent compound context
- no robust generalization claim

Possible future tightening:

> The benchmark signal justifies continued internal prioritization and review, but it does not by itself justify biological, translational, or clinical claims.

### Limitations

Keep all current limitations. Add only if reviewers request stronger visibility.

Possible future addition:

> Public reproducibility may remain aggregate-only if row-level dataset redistribution is not approved.

### Data / Code Availability

This section needs final wording after manual decisions. For the current draft, use the most conservative candidate from `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`.

Do not claim:

- public processed dataset availability
- row-level derived artifact availability
- release tag or archive until created
- final license/legal determination

### Supplement Pointer

Keep the pointer to `docs/supplement/permea-first-paper-supplement-v0-1.md`.

Possible future tightening:

> The current supplement draft is internal-review only and uses aggregate summaries and path-level traceability; it is not a public supplement export.

### Submission-Readiness Note

Keep public bioRxiv **Hold / not submission-ready**. Do not soften the Hold status until all blockers are resolved and approved.

## 5. Exact Claim-Boundary Wording Candidates

Use where future reviewers request stronger boundary wording:

> This manuscript reports an in-silico benchmark-signal analysis only. It does not establish biological validation, wet-lab validation, in-vivo activity, therapeutic efficacy, clinical efficacy, or production readiness.

> The reported metrics are bounded by the current dataset, split policy, feature representation, baseline model families, and committed result artifacts.

> The leakage-aware sensitivity analysis is not a leakage-free guarantee and does not establish robust generalization.

> Direct peptide predictor citations provide context and lineage only; this manuscript does not make matched leaderboard or state-of-the-art claims.

## 6. Dataset / Source Caveat Wording Candidates

> Dataset provenance and availability remain unresolved for public release. The processed dataset is not declared publicly redistributable in this draft.

> Exact upstream source files/version, source terms, required attribution wording, original label-source criteria, and redistribution permission require manual review before public data availability can be finalized.

> Row-level processed datasets and row-level derived artifacts remain excluded from public-facing materials unless explicit permission and manual approval are documented.

## 7. Result Interpretation Wording Candidates

> The result supports a cautious computational benchmark-signal claim under the current artifact surface.

> The result does not establish candidate efficacy, BBB transport, biological mechanism, or external validation.

> Feature importance is treated as model behavior within the current feature representation, not as mechanistic evidence.

## 8. Supplement / Export Caveat Wording Candidates

> Supplement v0.1 is an internal-review supplement draft. It uses aggregate summaries and path-level traceability only.

> Public-facing supplement/export remains blocked until figure/table numbering, captions, export manifest, row-level artifact exclusion, and founder/manual approval are complete.

> Public supplement materials must not include row-level sequences, labels, predictions, rankings, split manifests, group assignments, or sequence-pair leakage tables.

## 9. Remaining Manual Decisions

Manual decisions required before broader/public review:

- exact upstream dataset files/version
- source terms/license and required attribution wording
- original label-source criteria
- processed row-level dataset redistribution posture
- row-level derived artifact release posture
- code repository URL, release tag/commit, license, and archive policy
- final data/code availability wording
- final bibliography metadata cleanup
- final source-to-claim approval
- supplement/export numbering, captions, and manifest
- founder/manual approval for public posting

## 10. Recommended Next Task

Recommended next task: Task 053 - Audit the v0.5 edit plan and data/code availability candidate wording before applying any manuscript edits.
