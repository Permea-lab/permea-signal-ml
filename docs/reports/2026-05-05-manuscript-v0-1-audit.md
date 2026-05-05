# Permea Manuscript v0.1 Claim and Structure Audit - 2026-05-05

## Purpose

This audit reviews `docs/paper/permea-first-paper-manuscript-v0-1.md` for claim discipline, structure, internal consistency, and readiness gaps before commit.

This is an audit only. It does not rewrite the manuscript, modify `references.bib`, rerun models, rerun leakage audit, generate new splits, change metric values, or approve public bioRxiv submission.

## Materials Reviewed

- `docs/paper/permea-first-paper-manuscript-v0-1.md`
- `docs/reports/2026-05-05-submission-readiness-audit.md`
- `docs/reports/2026-05-05-reference-audit.md`
- `docs/reports/2026-05-05-export-readiness-check.md`
- `docs/submission/2026-05-05-dataset-license-review-draft.md`
- `docs/submission/2026-05-05-metadata-and-disclosures-draft.md`
- `docs/submission/2026-05-05-data-and-code-availability-draft.md`
- `docs/submission/2026-05-05-founder-approval-packet-v0-1.md`

## Executive Verdict

The manuscript draft may be suitable for internal review. No major claim-boundary issue was found in this audit.

Public bioRxiv status remains **Hold / not submission-ready** until all metadata, disclosure, dataset legal/licensing, data/code availability, reference cleanup, supplement/export formatting, founder/manual approval, and final posting blockers are resolved manually.

## Checklist Findings

### 1. Metadata Consistency

Status: pass for current confirmed metadata.

The draft uses the confirmed values:

- Author: Albert Heekwan Kim
- Affiliation: Permea Research
- Corresponding author email: a.kim@permea.us
- Funding: No funding
- Conflict of interest: N/A
- Acknowledgements: N/A
- Ethics statement: N/A

Remaining gap: ORCID, author contribution wording, bioRxiv category, version date, and final approval status remain unresolved or not included. This is acceptable for an internal v0.1 draft but remains a public-submission blocker.

### 2. Abstract Claim Discipline

Status: pass.

The abstract frames the work as "initial computational evidence" and explicitly states that the results do not establish leakage-free status, robust generalization, biological validation, wet-lab validation, therapeutic efficacy, or clinical efficacy.

Minor future edit: the abstract is long. A future revision could shorten it while preserving the same claim boundaries.

### 3. Introduction Scope Discipline

Status: pass.

The introduction keeps the scope to an in-silico BBB-related peptide classification task and explicitly avoids equating computational permeability language with experimentally validated BBB transport or therapeutic effect.

Low-risk issue: citation keys are listed as notes rather than inserted as normal manuscript citations. This is acceptable for a draft assembly, but a future revision should convert key notes into sentence-level citations after reference cleanup.

### 4. Methods Reproducibility Clarity

Status: pass with minor gaps.

The methods section identifies the dataset surface, feature columns, baseline model families, random-stratified evaluation policy, leakage-aware sensitivity manifest, and major caveats.

Medium-risk issue: the current draft does not include implementation details such as exact scripts, model hyperparameters, software versions, or artifact paths for every metric. These are available elsewhere in the repository but should be summarized or referenced more explicitly before public submission.

### 5. Results Metric Consistency

Status: pass.

The random-stratified metrics match the committed summary values:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8605 | 0.4903 | 0.3618 |
| Random Forest | 0.8489 | 0.5002 | 0.4331 |

The leakage-aware sensitivity metrics match the committed values:

| Model | ROC-AUC | PR-AUC | MCC |
| --- | ---: | ---: | ---: |
| Dummy most-frequent | 0.5000 | 0.0909 | 0.0000 |
| Logistic Regression | 0.8587 | 0.5024 | 0.3747 |
| Random Forest | 0.8718 | 0.5807 | 0.5084 |

The deltas match prior reports:

- Logistic Regression: ROC-AUC -0.0018, PR-AUC +0.0121, MCC +0.0130.
- Random Forest: ROC-AUC +0.0229, PR-AUC +0.0805, MCC +0.0753.

### 6. Leakage-Aware Sensitivity Wording

Status: pass.

The draft uses bounded language: "did not collapse" under the tested group-stratified sensitivity setting. It does not claim leakage-free status or full leakage control.

The draft also preserves the important limitations:

- `max_pairs=10000` caveat
- one non-singleton group
- source field too coarse for source-aware split control
- sensitivity manifest is not proof that all leakage/provenance concerns are controlled

### 7. Discussion Overclaim Risk

Status: pass.

The discussion states that the evidence supports a cautious computational interpretation and candidate-prioritization framing, while explicitly excluding external, wet-lab, biological, in-vivo, therapeutic, and clinical validation.

Low-risk issue: "candidate prioritization" should continue to be paired with "before experimental validation" or "pre-experimental" in future edits.

### 8. Limitations Completeness

Status: pass.

The limitations section includes computational-only status, no biological/wet-lab/in-vivo validation, no therapeutic or clinical efficacy claim, unresolved dataset licensing/provenance, coarse source metadata, grouping caveats, limited features, baseline-only models, random-stratified optimism risk, draft references, and supplement/export blockers.

### 9. Dataset/License Caution

Status: pass.

The draft states that dataset provenance and availability remain unresolved and that redistribution depends on source terms and manual licensing review. It does not conclude that redistribution is permitted.

### 10. Data/Code Availability Caution

Status: pass.

The draft separates code availability from data availability and uses conservative wording aligned with the data/code availability draft. It preserves TODOs for final code release policy and data licensing review.

### 11. References/TODO Completeness

Status: pass with known blocker.

The draft includes reference cleanup TODOs and does not modify or invent `references.bib` metadata.

Medium-risk issue: the manuscript is not citation-formatted for public submission yet. Citation keys are currently discussed in a note rather than integrated throughout the text. This is acceptable for internal review but blocks public submission.

### 12. Supplement/Export Readiness

Status: pass with known blocker.

The draft points to `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` and includes supplement/export TODOs.

Medium-risk issue: figures, tables, captions, numbering, and export manifest remain unresolved for public submission.

### 13. Public Preprint Readiness Status

Status: pass.

The draft explicitly states that public preprint submission remains Hold / not submission-ready.

### 14. Founder/Manual Approval Blockers

Status: pass.

The draft lists founder/manual approval as a remaining blocker and does not imply approval has occurred.

## Risk Summary

### High-Risk Issues

None found.

### Medium-Risk Issues

1. Methods are structurally clear but need more implementation-level detail before public submission, including exact scripts, model settings, software versions, and artifact-path traceability.
2. Citation placement and bibliography cleanup are not public-ready. Citation keys should be integrated into the manuscript after `references.bib` human cleanup.
3. Supplement/export readiness remains incomplete: figures, tables, captions, numbering, and export manifest need a separate formatting pass.

### Low-Risk Issues

1. Abstract could be shortened in a later revision.
2. Candidate-prioritization language should remain paired with pre-experimental or before-experimental-validation qualifiers.
3. The title is accurate but long; a shorter display title may be useful later.
4. The draft uses TODO markers appropriately, but final public export should either resolve or explicitly convert them into approved placeholders.

## Recommended Future Edits

For a future revision task:

1. Add a concise reproducibility table with scripts, input artifacts, output artifacts, and metric sources.
2. Convert reference-key notes into sentence-level citation formatting.
3. Add a compact figure/table plan or public-export table list.
4. Shorten the abstract while preserving exact claim boundaries.
5. Decide whether the title should remain long and descriptive or move to a shorter public-facing variant.
6. Add author contribution and ORCID fields only after founder/manual confirmation.
7. Keep dataset legal and data availability language unresolved until manual review is complete.

## Internal Review Readiness

The manuscript draft can proceed to internal review.

This internal-review readiness does not mean public bioRxiv readiness. Public posting remains blocked by metadata, disclosure, dataset licensing, data/code availability, reference cleanup, supplement/export formatting, founder/manual approval, and final public posting decision.

## No-Change Confirmation

- Manuscript draft was not modified by this audit.
- `references.bib` was not modified.
- Data files were not modified.
- Result artifacts were not modified.
- Figure artifacts were not modified.
- Models were not rerun.
- Leakage audit was not rerun.
- New split generation was not run.
- Metric values were not changed.
- Public bioRxiv remains **Hold / not submission-ready**.
