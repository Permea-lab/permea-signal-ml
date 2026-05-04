# Preprint Claim-Boundary Audit v0.1

## Purpose

This audit checks the bioRxiv v0.1 manuscript candidate package for claim-boundary violations.

## Materials inspected

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`
- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`
- `docs/LEAKAGE_AUDIT_REPORT_V0_1.md`
- `docs/LEAKAGE_AUDIT_FINDINGS_INVESTIGATION_V0_1.md`
- `references.bib`

## Audit result

Status: **Pass with caveats**

No major claim-boundary violation was found in the original candidate audit. Task 060 later applied focused wording fixes from the maximum-harsh review to make abstract, metric, leakage, prioritization, and feature-importance boundaries harder to overread.

## Post-Task-060 note

Focused abstract and claim-boundary fixes are documented in `docs/PREPRINT_MANUSCRIPT_CANDIDATE_FIX_CHANGELOG_V0_1.md`.

The fixes strengthened:

- random-stratified baseline wording around metrics
- same-label cross-fold similarity and moderate optimism-risk caveats
- computational/pre-experimental candidate-prioritization language
- non-mechanistic feature-importance framing
- Hold / not submission-ready public preprint status

Remaining caveats still include metadata, disclosure, dataset/legal, reference, supplement/export, human approval, and leakage-aware sensitivity blockers. Public preprint status remains **Hold / not submission-ready**.

## Post-Task-092 note

Leakage-aware sensitivity findings have been added to `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`, `docs/PREPRINT_DRAFT_V0_1.md`, and `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`. The update is documented in `docs/LEAKAGE_AWARE_MANUSCRIPT_UPDATE_CHANGELOG_V0_1.md`.

The added language states that the leakage-aware group-stratified rerun did not collapse the baseline signal under this specific grouping strategy, while preserving explicit boundaries: no leakage-free status, no robust generalization, no biological validation, no wet-lab validation, no therapeutic or clinical efficacy, and no public-posting approval. Public preprint status remains **Hold / not submission-ready**.

## Required boundary checks

| Check | Result | Evidence / note |
| --- | --- | --- |
| No wet-lab validation claim | Pass | Candidate and supplement explicitly state no wet-lab validation. |
| No biological validation claim | Pass | Validation language appears as negation or future need only. |
| No leakage-free claim | Pass | Leakage-free wording appears only as a prohibited/negative boundary. |
| No robust-generalization claim | Pass | Candidate states current metrics may be optimistic and are not leakage-aware generalization estimates. |
| No SOTA predictor claim | Pass | Candidate explicitly excludes SOTA predictor status. |
| No therapeutic/clinical claim | Pass | Therapeutic and clinical terms appear only as excluded claim categories. |
| Feature importance non-mechanistic | Pass | Candidate and draft describe RF feature importance as model-level behavior, not mechanism. |
| Metrics random-stratified and potentially optimistic | Pass | Candidate, draft, supplement, and leakage docs preserve random-stratified baseline caveat. |
| Leakage-aware sensitivity wording bounded | Pass | Candidate, draft, and supplement describe leakage-aware rerun metrics as sensitivity estimates under one committed manifest, not validation or proof of robust generalization. |
| Preprint candidate not submission-ready | Pass | Candidate, draft, supplement, and checklist state not submission-ready / human review required. |
| No fabricated reference claims | Pass | `references.bib` contains draft entries from verified packs only; partial/deferred references are documented outside BibTeX. |

## Caveats retained

- Dataset attribution, licensing, redistribution, source-chain metadata, and original label-source criteria remain incomplete.
- Current metrics are random-stratified baseline metrics and may be optimistic due to measured duplicate and similarity findings.
- The draft bibliography uses supplied lead-author forms plus `and others` for several entries; human reference review remains required.
- The manuscript candidate remains a package for human review, not a public submission.

## No-change confirmation

- No data files were modified.
- No result artifacts were modified.
- No figure artifacts were modified.
- No metric values were changed.
- No baseline models were rerun.
- No new model families or benchmark results were introduced.
