# Preprint Manuscript Candidate Fix Changelog v0.1

## Purpose

This changelog records focused abstract and claim-boundary wording fixes applied after the internal maximum-harsh manuscript candidate review.

Source review:

- `docs/PREPRINT_MANUSCRIPT_CANDIDATE_MAX_HARSH_REVIEW_V0_1.md`

This changelog does not add new benchmark results, change metric values, rerun models, rerun leakage audits, add references, or claim public preprint readiness.

## Fixes Applied

| Fix area | Documents updated | Claim-boundary effect |
|---|---|---|
| Abstract caveats | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`; `docs/PREPRINT_DRAFT_V0_1.md` | Metric values are now introduced as random-stratified baseline metrics and not leakage-aware generalization estimates. |
| Metric and leakage interpretation | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`; `docs/PREPRINT_DRAFT_V0_1.md`; `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` | Metric interpretation is tied to `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`, same-label cross-fold similarity findings, and moderate optimism risk. |
| Biological and prioritization language | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`; `docs/PREPRINT_DRAFT_V0_1.md` | Candidate prioritization is bounded as computational hypothesis generation before experimental validation, not delivery performance or biological actionability. |
| Feature-importance framing | `docs/PREPRINT_MANUSCRIPT_CANDIDATE_V0_1.md`; `docs/PREPRINT_DRAFT_V0_1.md`; `docs/SUPPLEMENTARY_MATERIALS_DRAFT_V0_1.md` | Feature importance is stated as model-level behavior only, not mechanism, causality, or biological explanation. |
| Public preprint status | `docs/PREPRINT_DRAFT_V0_1.md`; `docs/PREPRINT_CLAIM_BOUNDARY_AUDIT_V0_1.md`; `docs/BIORXIV_V0_1_READINESS_REASSESSMENT_V0_1.md`; `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Public preprint remains Hold / not submission-ready after the fixes. |

## Metric Values

No metric values were changed.

The manuscript still reports the existing regenerated baseline values:

- Dummy PR-AUC approximately 0.0909
- Logistic Regression ROC-AUC approximately 0.8605
- Logistic Regression PR-AUC approximately 0.4903
- Logistic Regression MCC approximately 0.3618
- Random Forest ROC-AUC approximately 0.8489
- Random Forest PR-AUC approximately 0.5002
- Random Forest MCC approximately 0.4331

## Remaining Blockers

Public preprint status remains: **Hold / not submission-ready**.

Remaining blockers include:

- final author metadata, author order, affiliations, corresponding author, and email
- funding, competing interests, acknowledgements, author contributions, ethics, data availability, and code availability wording
- dataset attribution, licensing, redistribution, source-chain, and label-source criteria
- final human bibliography review and deferred-reference decisions
- final supplement/export formatting and human approval
- leakage-aware or similarity-aware sensitivity follow-up before stronger benchmark claims

## Safety Confirmation

- No leakage-free claim was added.
- No robust-generalization claim was added.
- No biological or wet-lab validation claim was added.
- No therapeutic or clinical efficacy claim was added.
- No data files were modified.
- No result artifacts were modified.
- No figure artifacts were modified.
- No metric values were changed.
- `references.bib` was not modified.
