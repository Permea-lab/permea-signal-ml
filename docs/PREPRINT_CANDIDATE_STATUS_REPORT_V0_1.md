# Preprint Candidate Status Report v0.1

## Purpose

This report summarizes the current status of the bioRxiv v0.1 manuscript candidate package.

This is not a submission package, does not approve public posting, does not add new scientific evidence, does not change metric values, and does not close human metadata, legal, bibliography, supplement/export, or approval blockers. Public preprint status remains **Hold / not submission-ready**.

## Current Package Inventory

| Component | Path | Status | Ready for internal review? | Ready for public posting? | Notes |
|---|---|---|---:|---:|---|
| Manuscript candidate | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md` | Prepared candidate | Yes | No | Human review required; metadata/legal/reference/export blockers remain. |
| Supplement draft | `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` | Draft | Yes | No | Not final or export-formatted. |
| Draft bibliography | `references.bib` | Draft bibliography with 18 entries | Yes, with caveats | No | Human cleanup required; several entries use lead-author plus `and others`. |
| Citation consistency check | `docs/CITATION_CONSISTENCY_CHECK_V0_1.md` | Pass | Yes | No | Key consistency passed; sentence-level source support and bibliography cleanup still require human review. |
| Claim-boundary audit | `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md` | Pass with caveats | Yes | No | Confirms current package stays within computational, non-validation boundaries, with remaining blockers. |
| Post-fix harsh review | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_POST_FIX_REVIEW_V0_1.md` | Improved with required follow-up | Yes | No | No remaining P0/P1 blockers for next internal draft stage; P2/P3/P4 blockers remain. |
| Readiness reassessment | `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md` | Candidate package prepared; not submission-ready | Yes | No | Preserves Hold status. |
| Export package draft | `docs/BIORXIV_EXPORT_PACKAGE_DRAFT_V0_1.md` | Draft manifest only | Yes | No | No final PDF, DOCX, submission bundle, website material, or public deployment. |
| Metadata/disclosure input form | `docs/HUMAN_METADATA_AND_DISCLOSURE_INPUT_FORM_V0_1.md` | Form prepared | Yes | No | Requires human completion; Codex must not invent values. |
| Legal/availability options | `docs/DATASET_LEGAL_AND_AVAILABILITY_STATEMENT_OPTIONS_V0_1.md` | Options prepared | Yes | No | Not legal advice and not redistribution approval. |
| References cleanup checklist | `docs/FINAL_REFERENCES_HUMAN_CLEANUP_CHECKLIST_V0_1.md` | Checklist prepared | Yes | No | Does not finalize references or modify `references.bib`. |
| Supplement/export checklist | `docs/SUPPLEMENT_EXPORT_FORMATTING_CHECKLIST_V0_1.md` | Checklist prepared | Yes | No | Defines formatting checks; does not create final export files. |
| Leakage-aware sensitivity plan | `docs/LEAKAGE_AWARE_SENSITIVITY_ANALYSIS_PLAN_V0_1.md` | Plan prepared | Yes | No | No leakage-aware split or metric has been generated. |

## Scientific Readiness Summary

- P0/P1 blockers: none identified for the next internal draft stage.
- Metrics: current values are random-stratified baseline metrics.
- Leakage caveat: first audit found moderate benchmark optimism risk from same-label duplicate and high-similarity sequence structure crossing reconstructed folds.
- Biological validation: absent.
- Wet-lab validation: absent.
- Feature importance: model-level behavior only; not mechanism, causality, or proof that descriptors determine BBB transport.
- Candidate prioritization: computational and pre-experimental only.
- Stronger benchmark or generalization claims require leakage-aware sensitivity follow-up or explicit final caveat language.

## Public Preprint Readiness Summary

Status: **Hold / not submission-ready**.

Reasons:

- human metadata required
- legal and dataset availability decision required
- reference cleanup and bibliography approval required
- final citation/source-claim review required
- supplement/export formatting required
- final human approval required
- human decision required on leakage-aware sensitivity before bioRxiv versus explicit caveat path

## What Is Ready

- Internal manuscript candidate for human review.
- Supplement draft for internal review.
- Draft bibliography for human cleanup.
- Citation consistency check.
- Claim-boundary audit.
- Post-fix harsh review.
- Leakage audit outputs and conservative interpretation.
- Artifact traceability and export planning materials.
- Human metadata/disclosure input form.
- Dataset legal/availability options.
- Final references cleanup checklist.
- Supplement/export formatting checklist.
- P2 blocker closure plan.
- Leakage-aware sensitivity analysis plan.

## What Is Not Ready

- Public bioRxiv submission.
- Final author metadata, affiliations, correspondence, contributions, funding, competing interests, acknowledgements, and ethics statements.
- Final legal/dataset attribution, licensing, redistribution, public release, and availability decision.
- Final `references.bib` approval.
- Final supplement/export package.
- Website or partner public use.
- Robust generalization claims.
- Leakage-free claims.
- Biological, wet-lab, therapeutic, or clinical claims.

## Human-Required Decisions

- final author list, author order, names, affiliations, corresponding author, email, ORCID, and contribution decisions
- funding, competing interests, acknowledgements, ethics, and disclosure wording
- dataset source attribution, licensing, redistribution, processed-data release, and public data availability decisions
- code repository URL, release tag/archive, software license wording, and public code availability decision
- human cleanup and approval of `references.bib`
- final citation/source-claim approval
- whether to run leakage-aware sensitivity before bioRxiv or proceed with explicit caveats
- whether to publish a Permea website preview before bioRxiv
- final public posting approval

## Codex-Can-Continue Tasks

- prepare a one-page human input summary sheet
- prepare a supplement formatting pass
- prepare a references cleanup prompt for human review
- implement leakage-aware split utilities if explicitly requested
- prepare a website preview claim-boundary checklist
- prepare a final export manifest after human inputs are supplied
- prepare final claim-boundary and citation consistency re-check tasks after blocker closure

## Recommended Next Path Options

### Option A - Fast bioRxiv Candidate Path

1. Fill human metadata and legal inputs.
2. Keep leakage-aware sensitivity as explicitly caveated future work.
3. Finalize references, supplement, captions, and export package.
4. Run final claim-boundary and citation checks.
5. Obtain human approval.

This is faster, but it must preserve current metrics as random-stratified baseline metrics that may be optimistic.

### Option B - Stronger Scientific Package Path

1. Implement leakage-aware grouping and split utilities.
2. Generate leakage-aware split manifests.
3. Rerun existing baseline models under stricter split policies.
4. Compare random-stratified and leakage-aware metrics.
5. Update manuscript and supplement after sensitivity results exist.
6. Proceed to metadata, legal, reference, supplement/export, and human approval closure.

This is stronger scientifically, but it delays public posting and creates new result artifacts in later tasks.

### Option C - Website Evidence Archive First

1. Prepare a Permea website evidence-archive preview after a separate website claim-boundary review.
2. Avoid public language that implies bioRxiv submission readiness, robust generalization, leakage-free status, or validated delivery.
3. Defer bioRxiv until metadata, legal, reference, supplement/export, and leakage-sensitivity decisions are closed.

This may support transparent public communication, but it still requires separate public-copy safety review.

## Recommended Immediate Next Action

The next practical action is for the human operator to complete `docs/HUMAN_METADATA_AND_DISCLOSURE_INPUT_FORM_V0_1.md` and decide whether leakage-aware sensitivity is required before bioRxiv v0.1.

If Codex should continue before human inputs are available, the next useful Codex task is to prepare a one-page human-input summary sheet that condenses metadata, legal, bibliography, supplement/export, and leakage-sensitivity decisions into a shorter decision form.

## Final Status Verdict

**Manuscript candidate prepared; human review and blocker closure required.**

The package is usable for internal manuscript review and trusted-review planning with caveats. It is not cleared for public bioRxiv posting, website archive use, partner/deck use, or stronger benchmark/generalization claims.

## No-Change Confirmation

- Manuscript files were not modified by this report.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Baseline models were not rerun.
- Leakage audit was not rerun.
- Leakage-aware splits were not run.
- Metric values were not changed.
- No references were added.
- No author, disclosure, funding, conflict, acknowledgement, dataset licensing, redistribution, or legal certainty was invented.
- No leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
