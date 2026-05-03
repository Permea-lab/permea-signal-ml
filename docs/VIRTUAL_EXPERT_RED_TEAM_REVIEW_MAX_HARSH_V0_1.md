# Virtual Expert Red-Team Review, Maximum Harsh v0.1

## Purpose

This document records an internal virtual expert red-team review conducted at maximum harshness against the current `permea-signal-ml` manuscript, evidence, and review-operation package.

This is not external expert review, not real peer review, not trusted reviewer feedback, not public validation, and not new scientific evidence. It is an internal simulated stress test designed to identify what a severe technical, biological, narrative, submission, or partner-facing reader could reject or misunderstand.

All findings below are internal virtual red-team findings. They must not be copied into `REVIEW_FEEDBACK_LOG_V0_1.md` as if they came from actual reviewers.

## Materials reviewed

Core manuscript and evidence documents:

- `docs/PREPRINT_DRAFT_V0_1.md`
- `docs/DATASET.md`
- `docs/FIRST_EVIDENCE_SUMMARY.md`
- `docs/V0_1_EVIDENCE_PACKAGE.md`
- `docs/PREPRINT_ASSEMBLY_V0_1.md`
- `docs/SUPPLEMENTARY_OUTLINE_V0_1.md`
- `docs/BIORXIV_SUBMISSION_CHECKLIST_V0_1.md`
- `docs/INTERNAL_REVIEW_MEMO_V0_1.md`
- `docs/CIRCULATION_GUIDE_V0_1.md`
- `docs/REVIEWER_NOTE_V0_1.md`

Review and audit documents:

- `docs/HARSH_REVIEW_COUNCIL_CHARTER_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_0_BASELINE_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_1_INTEGRATED_ISSUE_REGISTER_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_1_REVISION_PLAN_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_1_P1_CLAIM_BOUNDARY_CHANGELOG_V0_1.md`
- `docs/HARSH_REVIEW_ROUND_1_P2_PROVENANCE_BENCHMARK_CHANGELOG_V0_1.md`
- `docs/HARSH_REVIEW_POST_P1_P2_COUNCIL_CHECK_V0_1.md`

Review-operation documents:

- `docs/TRUSTED_REVIEW_CIRCULATION_PACKET_SNAPSHOT_V0_1.md`
- `docs/TRUSTED_REVIEW_FEEDBACK_INTAKE_TEMPLATE_V0_1.md`
- `docs/REVIEW_FEEDBACK_LOG_V0_1.md`
- `docs/REVISION_PRIORITY_FRAMEWORK_V0_1.md`
- `docs/REVIEW_OPERATIONS_INDEX_V0_1.md`

Result and artifact references:

- `results/tables/model_comparison_summary.csv`
- `results/tables/regenerated_rf_feature_importance.csv`
- `results/metrics/legacy_bbb_lr_v01_metrics.json`
- `results/manifests/legacy_bbb_lr_v01_manifest.json`
- `figures/regenerated_rf_feature_importance.png`
- artifact inventory under `results/` and `figures/`

Deck or pitch materials were not reviewed because no deck, pitch, slide, presentation, `.ppt`, or `.pptx` files were found inside `permea-signal-ml`.

## Council composition

- Virtual Reviewer A — Computational Executioner
- Virtual Reviewer B — Biological Skeptic
- Virtual Reviewer C — Narrative Destroyer
- Virtual Reviewer D — Preprint Gatekeeper
- Virtual Reviewer E — Investor/Partner Skeptic

These are internal simulated red-team roles only. They are not real reviewers and do not represent external expert opinions.

## Executive verdict

Verdict: Proceed with required fixes.

The package can proceed to the next internal development phase without waiting for real external reviewer feedback, but it should not proceed to public preprint submission or public deck/partner circulation without resolving or explicitly handling the remaining provenance, leakage, metadata, reference, and public-claim risks.

No P0 fatal contradiction was identified. The strongest problems are not that the current package overclaims in its main manuscript; the strongest problems are that unresolved provenance, label criteria, leakage audit status, and public-facing reuse risk still limit how far the package can be circulated beyond trusted review.

## Virtual Reviewer A — Computational Executioner

Verdict: Pass with severe caveats.

### Top harsh findings

- The benchmark is reviewable, but still not audit-grade because dataset version, attribution, licensing, and original label-source criteria remain unresolved.
- `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` is documented, but the current package cannot claim duplicate-aware or sequence-similarity-aware evaluation.
- The metrics are traceable to artifacts, but a hostile reproducibility reader can still ask whether all artifact-generating scripts, manifests, and final export tables align without a final traceability check.
- Class imbalance is acknowledged, but PR-AUC interpretation will remain fragile unless reviewers can see the class prior and label semantics clearly.

### Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before next development? | Required before public preprint? | Required before public deck/partner use? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VRT-A01 | P2 | Dataset provenance | Dataset surface is usable for trusted review but not provenance-closed. | `DATASET.md` states dataset version is `pending_confirmation`, attribution/licensing remain unresolved. | `DATASET.md`; manifests | Close version/attribution/licensing or preserve explicit unresolved status before public preprint. | No | Yes | Yes |
| VRT-A02 | P2 | Label definition | Labels are benchmark targets, not independently verified biological truth. | `DATASET.md` says original label-source criteria remain partially unresolved. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Add final label-source disclosure or unresolved-status language in any preprint package. | No | Yes | Yes |
| VRT-A03 | P2 | Leakage risk | The current split policy is not a leakage-control guarantee. | `DATASET.md` and `PREPRINT_DRAFT_V0_1.md` state duplicate/similarity leakage has not been audited. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md`; future supplement | Run an audit or keep a prominent limitation before preprint. | No | Yes | Yes |
| VRT-A04 | P2 | Artifact traceability | Artifact mapping is improved but should be checked before export. | `PREPRINT_ASSEMBLY_V0_1.md` has artifact-to-claim table; post-P1/P2 council still calls final traceability/export check useful. | `PREPRINT_ASSEMBLY_V0_1.md`; `results/metrics/`; `results/manifests/` | Run final artifact traceability/export check before preprint. | No | Yes | No |
| VRT-A05 | P3 | Metric interpretation | PR-AUC is responsibly framed but still needs class-prior context wherever excerpted. | `model_comparison_summary.csv` shows Dummy PR-AUC near 0.0909; draft explains imbalance. | `PREPRINT_DRAFT_V0_1.md`; future captions/excerpts | Keep class-prior baseline adjacent to PR-AUC claims. | No | Yes | Yes |

### Killer questions

- Can every manuscript metric be regenerated or traced from current artifacts without manual inference?
- What exactly generated the `label` field, and under what source criteria?
- How many exact or near-duplicate sequences exist across folds?
- Would a sequence-similarity-aware split materially reduce reported ROC-AUC or PR-AUC?
- What is the dataset license and redistribution status?

### What would change the verdict

The verdict would improve to "Pass for preprint preparation" if dataset version/attribution/licensing are closed or explicitly unresolved in final submission materials, label-source criteria are disclosed as far as possible, leakage risk is audited or prominently caveated, and a final artifact-to-claim traceability check is completed.

## Virtual Reviewer B — Biological Skeptic

Verdict: Pass with severe caveats.

### Top harsh findings

- The main text is cautious, but "BBB-oriented" and "permeability-related signal" remain phrases that can be overread when removed from their qualifiers.
- The package has no wet-lab validation, no biological mechanism, and no proof of delivery performance; any public excerpt that forgets this will become misleading quickly.
- Feature importance is currently described as model-level behavior, but figures and captions are the highest-risk place for accidental mechanism language.
- The dataset labels are not independently validated biological truth, which weakens biological interpretation more than a casual reader may realize.

### Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before next development? | Required before public preprint? | Required before public deck/partner use? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VRT-B01 | P1 | Biological overread | Public excerpts could turn "permeability-related signal" into an implied biological claim. | `PREPRINT_DRAFT_V0_1.md` is cautious; post-P1/P2 check says isolated phrases can still be overread. | Future abstracts, excerpts, deck text | Keep computational and benchmark-surface qualifiers adjacent to the phrase. | No | Yes | Yes |
| VRT-B02 | P1 | Validation boundary | Candidate prioritization must not read as biological validation. | Draft repeatedly says candidate prioritization before experimental validation. | `PREPRINT_DRAFT_V0_1.md`; outreach text | Preserve "before experimental validation" language in all public material. | No | Yes | Yes |
| VRT-B03 | P1 | Feature importance | Model-level feature importance could be reused as mechanism if caption context is lost. | Draft says not mechanistic proof; assembly says Figure 3 is not mechanistic evidence. | `PREPRINT_DRAFT_V0_1.md`; `figures/regenerated_rf_feature_importance.png`; captions | Lock captions to "model-level feature importance, not mechanistic evidence." | No | Yes | Yes |
| VRT-B04 | P2 | Label biology | Label-source uncertainty limits biological interpretation. | `DATASET.md` says labels are not independently verified biological truth. | `DATASET.md`; `PREPRINT_DRAFT_V0_1.md` | Make label-source limitation prominent in preprint methods and limitations. | No | Yes | Yes |
| VRT-B05 | P4 | Biological validation | The package ultimately needs wet-lab validation to move beyond candidate prioritization. | All current docs state no experimental validation is included. | Future roadmap | Keep as future work; do not backfill into current claims. | No | No | No |

### Killer questions

- Could a biologist read the abstract and believe BBB delivery has been validated?
- Are the labels sufficiently biologically meaningful to support even a bounded permeability signal claim?
- Is feature importance ever shown without the "not mechanism" caveat?
- Does candidate prioritization imply any real-world delivery performance?
- What experimental validation would be minimally required to advance the evidence level?

### What would change the verdict

The verdict would improve if public-facing phrasing is locked to computational, benchmark-surface language; feature-importance captions are made non-mechanistic everywhere; and label-source limitations are impossible to miss.

## Virtual Reviewer C — Narrative Destroyer

Verdict: Pass with severe caveats.

### Top harsh findings

- The project is now well structured, but the document stack is large enough to exhaust a first-time reader.
- The main claim is bounded, but it takes too many documents to understand why the package is trusted-review ready but not preprint-ready.
- The strongest narrative risk is "platform ambition leakage": broader Permea language can make a narrow BBB wedge sound more mature than it is.
- The package is operationally impressive, but public readers may mistake review infrastructure for scientific validation unless the distinction is preserved.

### Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before next development? | Required before public preprint? | Required before public deck/partner use? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VRT-C01 | P3 | Document complexity | Review-operation stack is too heavy for clarity-only readers. | `REVIEW_OPERATIONS_INDEX_V0_1.md` lists many review and council docs. | Review-operation docs | Keep Reviewer C packet minimal and avoid sending internal audit docs by default. | No | No | Yes |
| VRT-C02 | P3 | Readiness state | Trusted-review, preprint, and deck readiness are spread across multiple docs. | Snapshot and council check state Go with caveats / Not yet / Hold. | `TRUSTED_REVIEW_CIRCULATION_PACKET_SNAPSHOT_V0_1.md`; `HARSH_REVIEW_POST_P1_P2_COUNCIL_CHECK_V0_1.md` | Preserve a single current-readiness source for operators. | No | Yes | Yes |
| VRT-C03 | P1 | Platform ambition | Broader standard-layer context could be misread as evidence of generalization. | `FIRST_EVIDENCE_SUMMARY.md` and `V0_1_EVIDENCE_PACKAGE.md` link broader Permea core docs while caveating current wedge. | `FIRST_EVIDENCE_SUMMARY.md`; `V0_1_EVIDENCE_PACKAGE.md`; future public text | Keep broader Permea framing subordinate to current BBB computational wedge. | No | Yes | Yes |
| VRT-C04 | P3 | Abstract density | The abstract is accurate but dense and may bury the claim boundary. | Round 1 register flags abstract density as P3; draft abstract is long and caveat-rich. | `PREPRINT_DRAFT_V0_1.md` | Tighten for readability after P0-P2 checks are stable. | No | Yes | Yes |
| VRT-C05 | P3 | Figures and captions | Figure polish remains below final-public standard. | Submission checklist says figure polish and publication formatting remain pending. | Figures; `PREPRINT_ASSEMBLY_V0_1.md` | Perform figure/caption polish before preprint or partner deck reuse. | No | Yes | Yes |

### Killer questions

- Can a first-time reader explain the current claim in one sentence after only the minimum packet?
- Does the package feel like evidence, or like a platform narrative with evidence attached?
- Can a public reader distinguish review infrastructure from scientific validation?
- Which document is the single source of truth for current readiness?
- Would a deck writer accidentally omit the caveats because they are too distributed?

### What would change the verdict

The verdict would improve if readiness is kept in one current snapshot, the abstract is tightened without weakening claim boundaries, and public-facing materials keep broader Permea ambition separate from the current evidence surface.

## Virtual Reviewer D — Preprint Gatekeeper

Verdict: Hold pending fixes.

### Top harsh findings

- The manuscript is not preprint-ready because formal references, final authorship/affiliation metadata, disclosure statements, and a full supplement are not complete.
- Provenance, attribution, licensing, label-source criteria, and leakage status are still blockers or explicit-deferral items for public preprint.
- The package is a credible internal candidate, but a preprint upload would currently force the authors either to overstate closure or to submit with unresolved basic provenance questions.
- Final export, figure numbering, captions, and artifact traceability have not yet been through a last preprint assembly gate.

### Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before next development? | Required before public preprint? | Required before public deck/partner use? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VRT-D01 | P2 | Metadata | Authors, affiliations, correspondence, disclosures, funding, conflicts, and availability statements remain placeholders. | `PREPRINT_DRAFT_V0_1.md`; `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` | Replace placeholders before submission. | No | Yes | No |
| VRT-D02 | P2 | References | Formal references are not yet added. | `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` says formal references pending. | `PREPRINT_DRAFT_V0_1.md`; submission package | Add verified references before preprint submission. | No | Yes | No |
| VRT-D03 | P2 | Supplement | Supplement exists as outline, not full prose. | `SUPPLEMENTARY_OUTLINE_V0_1.md`; checklist says full supplement pending. | `SUPPLEMENTARY_OUTLINE_V0_1.md`; future supplement | Draft supplement or explicitly decide what is included at submission. | No | Yes | No |
| VRT-D04 | P2 | Provenance blockers | Public preprint needs provenance closure or explicit unresolved-status disclosure. | `BIORXIV_SUBMISSION_CHECKLIST_V0_1.md` lists provenance, attribution/licensing, label-source, leakage as blockers. | Submission package | Resolve or disclose each item before preprint. | No | Yes | Yes |
| VRT-D05 | P3 | Export readiness | Figure polish, manuscript export, and final formatting remain pending. | `PREPRINT_ASSEMBLY_V0_1.md`; checklist remaining blockers. | Figures; manuscript export | Run final formatting/export pass after content stabilization. | No | Yes | Yes |

### Killer questions

- Who are the final authors, affiliations, and corresponding author?
- What references support dataset provenance, BBB framing, and benchmark context?
- What exactly will be in the supplement at submission?
- Are data/code availability statements truthful given licensing uncertainty?
- Is every public figure caption claim-bounded?

### What would change the verdict

The verdict would improve to "Proceed to preprint preparation" after metadata, references, supplement decisions, provenance/label/leakage disclosure, and final artifact/figure/export checks are complete.

## Virtual Reviewer E — Investor/Partner Skeptic

Verdict: Pass with severe caveats.

### Top harsh findings

- The technical package increases credibility because it is unusually explicit about limitations, but those same limitations can backfire if public materials imply more maturity than the evidence supports.
- Partner-facing claims must not use the benchmark metrics as success probabilities, delivery rates, or proof of biological performance.
- Public deck or website language is currently not reviewable because no deck materials are present in the repo.
- The package is best used to show discipline, reproducibility posture, and a narrow computational wedge; it is not yet evidence of a de-risked delivery platform.

### Issue table

| Issue ID | Priority | Area | Finding | Evidence from repo | Affected document or artifact | Recommended action | Required before next development? | Required before public preprint? | Required before public deck/partner use? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VRT-E01 | P1 | Partner overclaim | Metrics could be misused as delivery success probabilities in public materials. | `model_comparison_summary.csv` has ROC-AUC/PR-AUC/MCC; docs frame them as benchmark metrics. | Future deck, website, partner memo | Forbid success-probability language unless experimentally supported. | No | Yes | Yes |
| VRT-E02 | P1 | Public validation risk | Review readiness could be misrepresented as external validation. | Review docs repeatedly distinguish internal and trusted review. | Public comms | State review infrastructure is internal/operational, not endorsement. | No | Yes | Yes |
| VRT-E03 | P2 | Public caveat handling | Caveats strengthen trust only if visible; hidden caveats create reputational risk. | Snapshot lists dataset version, licensing, label-source, leakage, and no wet-lab caveats. | `TRUSTED_REVIEW_CIRCULATION_PACKET_SNAPSHOT_V0_1.md`; public materials | Include caveat block in public or partner-facing technical appendix. | No | Yes | Yes |
| VRT-E04 | P4 | Partner evidence path | Partners will eventually ask for experimental validation and broader benchmarks. | Current docs identify wet-lab validation and benchmark expansion as future work. | Future roadmap | Prepare future evidence roadmap without converting it into current claims. | No | No | Yes |
| VRT-E05 | P4 | Deck review | Deck cannot be cleared until materials exist in repo. | No deck/pitch/presentation files found in `permea-signal-ml`. | Future deck materials | Review deck separately before circulation. | No | No | Yes |

### Killer questions

- Could a partner mistake PR-AUC or ROC-AUC for probability of successful delivery?
- Does any public copy imply the platform is validated beyond this computational wedge?
- Are unresolved licensing and label issues acceptable for the intended audience?
- What evidence milestone comes next after computational prioritization?
- Is the caveat discipline a strength in the deck, or hidden in technical appendices?

### What would change the verdict

The verdict would improve if any deck, website, or partner memo is reviewed against the same evidence boundary before use, metrics are never presented as delivery success probabilities, and unresolved provenance/licensing caveats are disclosed in the appropriate technical appendix.

## Integrated P0-P4 distribution

- P0 count: 0
- P1 count: 6
- P2 count: 11
- P3 count: 6
- P4 count: 4

## Top 10 non-negotiable issues

1. Dataset version remains `pending_confirmation`.
2. Attribution and licensing remain unconfirmed.
3. Original label-source criteria remain partially unresolved.
4. Duplicate, near-duplicate, and sequence-similarity leakage status remains unaudited.
5. Public claims must never convert benchmark metrics into biological validation or delivery success probabilities.
6. Feature importance must remain model-level behavior, not mechanism.
7. Broader Permea platform ambition must remain separate from this BBB-oriented computational wedge.
8. Formal references and final metadata are required before public preprint submission.
9. Supplement, figure/caption polish, and final artifact traceability/export check remain incomplete.
10. Deck or partner materials cannot be cleared because no deck materials are present in the repo.

## Go/no-go verdicts

| Path | Verdict | Rationale |
| --- | --- | --- |
| Next internal development | Go with caveats | No P0 or fatal blocker was found; required next work is scoped and already known. |
| Trusted review circulation | Go with caveats | Existing snapshot routes Reviewer A to extended packet and caveats are explicit. |
| Public preprint submission | Hold | Metadata, references, supplement, provenance/label/leakage handling, and final export checks remain incomplete. |
| Public deck/partner circulation | Hold | Deck materials were not present in repo and public-claim misuse risk remains high. |
| Wet-lab planning | Go with caveats | Planning can proceed as future validation design, but it must not be represented as current evidence. |
| Website/public project page | Hold | Public copy must be claim-aligned and caveat-aware before launch. |

## Required fixes before next development

None that block next internal development.

The next internal development phase should keep unresolved provenance, label-source, leakage, and public-facing caveat handling visible. It should not broaden claims or add model/biology work without a scoped task.

## Required fixes before public preprint

- Confirm dataset version or keep explicit `pending_confirmation` disclosure.
- Confirm attribution and licensing, or disclose unresolved status and constrain distribution language.
- Clarify original label-source criteria as far as recoverable.
- Run duplicate, near-duplicate, and sequence-similarity leakage audit, or preserve a prominent limitation.
- Perform final artifact-to-claim traceability and export check.
- Add formal references.
- Replace author, affiliation, correspondence, funding, conflict, contribution, and availability placeholders.
- Draft or explicitly scope the supplement.
- Run final figure numbering, caption, and formatting pass.

## Required fixes before public deck/partner use

- Review deck or partner materials after they exist in `permea-signal-ml`.
- Remove or soften any metric-as-success-probability language.
- Align all deck metrics with canonical regenerated metrics in `model_comparison_summary.csv`.
- Keep platform ambition separate from current BBB-oriented computational evidence.
- Preserve no-wet-lab, no-solved-delivery, no-biological-validation, and no-mechanism boundaries.
- Include provenance/licensing/label-source/leakage caveats in technical appendix or notes.

Deck not reviewed because no deck materials were present in `permea-signal-ml`.

## Decision

Yes, proceed to next development with caveats.

The virtual council does not require waiting for real external reviewer feedback before continuing internal development. It does require that the next development task respect the unresolved P1/P2 public-readiness risks and avoid public submission or partner-facing circulation until the listed preprint and deck gates are handled.

## Recommended next Codex task

Task 022 — Commit Maximum-Harsh Virtual Red-Team Review

Rationale: this task creates an internal virtual red-team report and stages it with the review-operations index. The next step should close that artifact before applying any fixes or roadmapping.

