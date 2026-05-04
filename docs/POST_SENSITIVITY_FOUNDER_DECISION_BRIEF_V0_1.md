# Post-Sensitivity Founder Decision Brief v0.1

## Purpose

This brief summarizes the post-sensitivity decision state for the founder/manual approval process for the bioRxiv v0.1 manuscript candidate.

Internal virtual review and internal audits are complete for the current package. External expert review has not occurred. Peer review has not occurred. Public posting is not approved. This brief does not make the preprint submission-ready and does not authorize public posting.

## Current Status

- Manuscript candidate prepared: `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`.
- Supplement draft prepared: `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md`.
- Draft `references.bib` prepared; human bibliography cleanup remains required.
- Leakage-aware sensitivity rerun completed under the committed group-stratified split manifest.
- Final post-sensitivity claim/citation audit passed: `docs/FINAL_POST_SENSITIVITY_CLAIM_AND_CITATION_AUDIT_V0_1.md`.
- P0/P1 blockers: none identified for internal continuation.
- Public preprint status: **Hold / not submission-ready**.

## Evidence Upgrade Since Previous Founder Summary

The previous founder/manual approval summary preserved a moderate benchmark-optimism concern from the leakage audit. That concern came from same-label duplicate and high-similarity sequence structure crossing reconstructed random-stratified folds.

Since then, a leakage-aware group-stratified split manifest was generated and the same baseline model families were rerun under that manifest. The baseline signal did not collapse under this specific grouping strategy. Logistic Regression remained broadly similar to the random-stratified baseline, and Random Forest was comparable to or higher than its random-stratified baseline under this manifest. The post-sensitivity claim-boundary and citation audit still passes.

## Evidence and Data Summary

### Random-Stratified Baseline Metrics

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 |
| Random Forest | 0.8489 | 0.5002 | 0.4331 |

### Leakage-Aware Sensitivity Metrics

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

### Random-Stratified Versus Leakage-Aware Deltas

| Model | ROC-AUC delta | PR-AUC delta | MCC delta |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.0000 | 0.0000 | 0.0000 |
| Logistic Regression | -0.0018 | +0.0121 | +0.0130 |
| Random Forest | +0.0229 | +0.0805 | +0.0753 |

Interpretation: the post-sensitivity package supports continued use of the computational benchmark-signal claim and strengthens confidence relative to the initial leakage concern. It does not prove robust generalization, does not establish leakage-free status, and does not validate biology.

## What Can Now Be Claimed

- Initial computational evidence for a permeability-related benchmark signal.
- Learnable permeability-related benchmark signal under the documented benchmark surfaces.
- Reproducible baseline and leakage-aware sensitivity evidence package.
- Leakage-aware sensitivity did not collapse the baseline signal under this specific grouping strategy.
- Computational and pre-experimental candidate-prioritization hypothesis generation.
- Artifact-to-claim traceability across manuscript, supplement, metrics, audit, and status documents.
- Explicit limitations and caveats around leakage, provenance, dataset legal status, label-source criteria, and validation.

## What Still Cannot Be Claimed

- Validated BBB delivery.
- Biological validation.
- Wet-lab validation.
- Leakage-free benchmark.
- Robust generalization.
- True BBB performance.
- Therapeutic efficacy.
- Clinical efficacy.
- Feature importance as mechanism, causality, or proof that descriptors determine BBB transport.
- Dataset licensing, attribution, redistribution, or provenance closure.
- External expert review.
- Peer review.

## Remaining Blockers Before bioRxiv

- Author metadata and affiliations.
- Funding, competing-interest, acknowledgement, and ethics statements.
- Dataset legal, licensing, attribution, redistribution, and source-chain decision.
- Data/code availability wording.
- `references.bib` human cleanup and approval.
- Final source-claim review.
- Supplement/export formatting.
- Founder/manual approval.
- Final public posting decision.

## Decision Paths

### Option A - Proceed Toward Caveated bioRxiv v0.1 After Cleanup

Recommended if speed matters. This path requires metadata, legal, reference, supplement, export, and final founder/manual approval closure before public posting. The leakage-aware sensitivity rerun is now available as supporting computational evidence, but it remains bounded and caveated.

### Option B - Perform Further Scientific Strengthening Before bioRxiv

Possible additions include alternative grouping thresholds, expanded baseline comparisons, and deeper source-chain reconstruction. These are not necessary for a caveated v0.1 package, but they may be useful for a v0.2 package or for reducing remaining uncertainty before broader public use.

### Option C - Website Evidence Archive First

A website evidence archive could be prepared before bioRxiv only after a separate website claim-boundary review. It must not imply bioRxiv posting, external expert review, peer review, validated delivery, robust generalization, or public-preprint approval.

## Recommended Decision

Proceed toward a caveated bioRxiv v0.1 package after metadata, legal, reference, supplement, and export cleanup.

Do not claim the package is submission-ready yet. Prepare a website evidence archive after the bioRxiv package is finalized, or in parallel only with strict claim-boundary review.

## Founder/Manual Approval Checklist

- [ ] I accept the current computational-only claim scope.
- [ ] I accept the leakage-aware sensitivity interpretation.
- [ ] I accept that no biological or wet-lab validation claim is made.
- [ ] I have completed metadata/disclosure fields.
- [ ] I have approved dataset legal/availability wording.
- [ ] I have approved `references.bib` cleanup.
- [ ] I have approved the supplement/export package.
- [ ] I approve moving toward bioRxiv v0.1 after remaining cleanup.
- [ ] I approve website evidence archive planning.

## Recommended Next Codex Task

Task 097 - Commit Post-Sensitivity Founder Decision Brief

## No-Change Confirmation

- Manuscript scientific content was not modified by this brief.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- Metric values were not changed.
- No references were added.
- No author, funding, conflict, acknowledgement, dataset attribution, licensing, redistribution, permission, or legal certainty was invented.
- No external expert review or peer review is implied.
- No public-preprint-ready, leakage-free, robust-generalization, biological-validation, wet-lab-validation, therapeutic, or clinical claim is made.
