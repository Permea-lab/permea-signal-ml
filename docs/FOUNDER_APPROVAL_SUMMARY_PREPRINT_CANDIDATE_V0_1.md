# Founder Approval Summary for Preprint Candidate v0.1

## Purpose

This document is a founder/manual approval brief for the bioRxiv v0.1 manuscript candidate.

This is not external expert review, not peer review, not public approval, and not a submission package. It does not add new scientific evidence, does not make the preprint submission-ready, and does not authorize public posting. Founder/manual approval is still required before any public bioRxiv posting, website preview, or partner-facing reuse.

## Current Package Status

- Manuscript candidate prepared: `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`.
- Supplement draft prepared: `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`.
- Draft `references.bib` prepared.
- Citation consistency check passed: `docs/CITATION_CONSISTENCY_CHECK_V0_1.md`.
- Claim-boundary audit passed with caveats: `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`.
- Internal virtual harsh-review council completed; this was internal stress testing only.
- Post-fix review found no P0/P1 blockers for the next internal draft stage.
- P2 blocker closure plan, metadata/disclosure form, dataset legal/availability options, references cleanup checklist, supplement/export checklist, final status report, and leakage-aware sensitivity plan exist.
- Public preprint remains **Hold / not submission-ready**.

## Evidence and Data Status

- A computational evidence package exists.
- Baseline metrics exist for Dummy most-frequent, Logistic Regression, and Random Forest.
- Metrics are random-stratified baseline metrics under `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`.
- Metrics may be optimistic because the leakage audit found same-label duplicate and high-similarity sequence structure crossing reconstructed folds.
- No leakage-aware metrics have been generated.
- Leakage audit completed and found moderate benchmark optimism risk.
- Dataset provenance, attribution, licensing, redistribution, public data availability, and label-source criteria blockers remain.
- No wet-lab validation exists.
- No biological validation exists.

## What the Manuscript Can Claim

- Initial computational evidence for a permeability-related benchmark signal in the current BBB-oriented peptide benchmark.
- Learnable benchmark signal under the current random-stratified split.
- Sequence-derived physicochemical feature baseline using length, charge, GRAVY, pI, and aromaticity.
- Reproducible evidence package with imported-versus-regenerated artifact separation.
- Candidate prioritization as computational hypothesis generation before experimental validation.
- Artifact-to-claim traceability across manuscript, supplement, metrics, figures, tables, audit outputs, and readiness docs.
- Explicit leakage, provenance, label-source, dataset legal, and validation caveats.

## What the Manuscript Cannot Claim

- Validated BBB delivery.
- Biological validation.
- Wet-lab validation.
- Leakage-free benchmark.
- Robust generalization.
- Therapeutic efficacy.
- Clinical efficacy.
- Feature importance as mechanism, causality, or proof that descriptors determine BBB transport.
- Dataset licensing, attribution, redistribution, or provenance closure.
- External expert review.
- Peer review.

## Remaining Blockers Before bioRxiv

- Final author metadata.
- Affiliations, corresponding author email, ORCID, and contribution decisions.
- Funding, competing-interest, acknowledgement, and ethics statements.
- Dataset attribution, licensing, redistribution, and source-chain decisions.
- Data availability and code availability statement decisions.
- `references.bib` founder/manual cleanup and approval.
- Final citation/source-claim review.
- Final supplement and export formatting.
- Decision on whether leakage-aware sensitivity analysis is required before posting.
- Founder/manual approval for public posting.

## Founder Decision Options

### Option A - Fast Caveated bioRxiv Path

Accept explicit leakage and provenance limitations for v0.1, finalize metadata/legal/references/supplement/export, and keep leakage-aware sensitivity as v0.2 work.

This is the fastest path, but it requires strict caveat discipline and cannot support leakage-free, robust-generalization, biological-validation, or delivery-performance claims.

### Option B - Stronger Scientific Package Path

Implement leakage-aware sensitivity analysis first, rerun existing baseline models under stricter split policies, compare random-stratified versus leakage-aware metrics, and update the manuscript before bioRxiv.

This path is slower, but it directly addresses the moderate benchmark optimism risk before public posting.

### Option C - Website Evidence Archive First

Publish a Permea website evidence-release preview only after a separate public-copy claim-boundary review, while deferring bioRxiv until metadata/legal/reference blockers are closed.

This path may help communicate progress, but it still requires no-public-overclaim wording and does not replace bioRxiv readiness work.

## Recommended Decision

Conservative recommendation:

- Do not post to bioRxiv yet.
- Use the current package as an internal manuscript candidate.
- Close metadata, disclosure, dataset legal, data/code availability, reference, supplement/export, and founder/manual approval blockers.
- Decide whether leakage-aware sensitivity analysis is required before public posting.
- If speed matters, choose the Fast caveated bioRxiv path only after metadata/legal/reference cleanup and final claim-boundary review.

## Founder Approval Checklist

- [ ] I reviewed the manuscript candidate.
- [ ] I reviewed the supplement draft.
- [ ] I reviewed leakage caveats.
- [ ] I reviewed dataset legal/availability options.
- [ ] I reviewed the `references.bib` cleanup checklist.
- [ ] I confirmed author metadata.
- [ ] I confirmed disclosure statements.
- [ ] I approved data/code availability language.
- [ ] I decided whether leakage-aware sensitivity is required before bioRxiv.
- [ ] I approve public bioRxiv posting.
- [ ] I do not approve public bioRxiv posting.

## Next Recommended Codex Task

Task 080 - Commit Founder Approval Summary

## No-Change Confirmation

- Manuscript files were not modified by this summary.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Baseline models were not rerun.
- Leakage audit was not rerun.
- Leakage-aware splits were not run.
- Metric values were not changed.
- No references were added.
- No author, funding, conflict, acknowledgement, dataset attribution, licensing, redistribution, permission, or legal certainty was invented.
- No external expert review or peer review is implied.
- No public-preprint-ready, leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
