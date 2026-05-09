# Bibliography and Export Readiness Audit - 2026-05-09

## 1. Purpose and Scope

This report audits bibliography cleanup requirements and figure/table/export-readiness requirements for the current Permea first-paper internal draft package.

Reviewed materials:

- `docs/paper/permea-first-paper-manuscript-v0-6.md`
- `docs/supplement/permea-first-paper-supplement-v0-2.md`
- `references.bib`
- `docs/reports/2026-05-08-manuscript-v0-6-source-to-claim-audit.md`
- `docs/reports/2026-05-08-supplement-v0-2-audit.md`
- `docs/submission/2026-05-07-biorxiv-readiness-blocker-checklist.md`
- `docs/submission/2026-05-08-data-code-availability-candidate-wording.md`
- `docs/reports/2026-05-07-public-safe-artifact-manifest.md`
- `docs/reports/2026-05-07-dataset-row-level-provenance-redistribution-risk-audit.md`
- `README.md`

This audit created this report only. It did not modify the manuscript, supplement, `references.bib`, README, data, result, figure, model, split, prediction, ranking, or leakage-audit artifacts. It did not rerun models, regenerate results, create splits, export a PDF, create a DOCX, stage files, commit, or push.

This audit does not approve public bioRxiv submission, dataset redistribution, row-level artifact release, legal/license conclusions, wet-lab validation, biological validation, therapeutic efficacy, or clinical efficacy.

## 2. Current Manuscript / Supplement Status

Manuscript v0.6 is the current internal-preparation manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-6.md`

The manuscript is explicitly internal-preparation only and preserves the public bioRxiv **Hold / not submission-ready** posture. It uses conservative claim boundaries, aggregate metric summaries, path-level artifact traceability, direct peptide comparator context, adjacent compound predictor separation, and Option A data/code availability wording.

Supplement v0.2 is the current internal-review supplement:

- `docs/supplement/permea-first-paper-supplement-v0-2.md`

The supplement aligns to manuscript v0.6, uses aggregate summaries and path-level traceability, includes figure/table inventory placeholders, caption requirements, an export manifest placeholder, and an allow/hold matrix. It is not a public supplement export.

## 3. Public-Readiness Status

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved. Row-level processed datasets, row-level labels, row-level predictions, rankings, split manifests, group assignments, sequence-pair leakage artifacts, upstream dataset mirrors, and row-level derived artifacts linkable to restricted source rows remain blocked from public release unless explicit permission and manual approval are documented.

Current public-readiness blockers include:

- dataset source, license, attribution, and redistribution decision
- original label-source criteria
- row-level artifact blocklist or exclusion approval
- data/code availability approval
- bibliography metadata cleanup and final citation formatting/export check
- final sentence-level source-to-claim review
- figure/table numbering, captions, and export manifest
- aggregate artifact allowlist and release-policy approval
- founder/manual approval and final public posting decision

## 4. Citation Key Inventory

### Keys used in manuscript v0.6

The manuscript uses 25 real citation keys:

- `arif2025deepb3pred`
- `augur_2024`
- `b3bpfn_2026`
- `b3pdb_2021`
- `b3pred_2021`
- `bbb_shuttle_review_2016`
- `bbppred_2021`
- `bbppredict_2022`
- `brainpeppass_2024`
- `brainpeps_2012`
- `chicco_jurman_2020_mcc`
- `esm_bbb_pred_2025`
- `kumar2022deepredbbb`
- `matplotlib_2007`
- `naseem2023bbbpep`
- `oliveira2026titanbbb`
- `pandas_2010`
- `parakkal2022deepbbbp`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `tang2025deepb3p`

The corresponding-author email contains `@permea.us`; this is not a citation key.

### Keys used in supplement v0.2

No bracketed citation keys were found in supplement v0.2. The supplement describes comparator and source contexts textually and relies on manuscript v0.6 for formal bibliography integration.

### Keys present in references.bib

`references.bib` contains 26 entries:

- `arif2025deepb3pred`
- `augur_2024`
- `b3bpfn_2026`
- `b3pdb_2021`
- `b3pred_2021`
- `bbb_shuttle_review_2016`
- `bbppred_2021`
- `bbppredict_2022`
- `brainpeppass_2024`
- `brainpeps_2012`
- `chicco_jurman_2020_mcc`
- `deepb3p3_2023`
- `esm_bbb_pred_2025`
- `kumar2022deepredbbb`
- `matplotlib_2007`
- `naseem2023bbbpep`
- `oliveira2026titanbbb`
- `pandas_2010`
- `parakkal2022deepbbbp`
- `perseucpp_2025`
- `practicpp_2024`
- `saito_rehmsmeier_2015_prauc`
- `scikit_learn_2011`
- `shaker2021lightbbb`
- `tang2022deepb3`
- `tang2025deepb3p`

## 5. Missing Citation Keys

No missing citation keys were found for manuscript v0.6.

No supplement v0.2 citation keys were found, so no supplement missing-key issue was found.

## 6. Unused references.bib Entries

One unused `references.bib` entry was found:

- `deepb3p3_2023`

All other `references.bib` entries are used by manuscript v0.6.

## 7. Confusing references.bib Entries

`deepb3p3_2023` remains the main confusing entry. Manuscript v0.6 explicitly says this key is intentionally not used as a DeepB3P or DeepB3Pred citation because its identity and citation role remain unresolved relative to the verified `tang2025deepb3p` and `arif2025deepb3pred` entries.

Cleanup requirement:

- decide whether `deepb3p3_2023` should be removed from `references.bib`, retained as unused background, renamed to a less confusing key, or cited with a clear role distinct from DeepB3P and DeepB3Pred
- do not use it to substitute for `tang2025deepb3p` or `arif2025deepb3pred`
- document the decision before public bibliography export

## 8. Metadata Cleanup Needs

The bibliography is key-complete for the current manuscript but not public-export clean.

Required metadata cleanup:

- replace or approve `and others` author fields after checking target journal/preprint style
- verify full author lists for older entries and newer comparator entries
- preserve title protection for acronyms, model names, and database names, including BBB, B3Pdb, B3Pred, BBPpred, BBPpredict, Augur, DeepB3P, DeepB3Pred, ESM-BBB-Pred, B3BPFN, PractiCPP, PerseuCPP, ROC, PR-AUC, MCC, F1, Python, LightGBM, BiGRU, GAN, SMILES, and TITAN-BBB where applicable
- verify DOI fields and add URLs only where DOI is absent or preprint/source policy requires it
- verify journal, conference, or preprint status for each entry
- verify year/status for 2025 and 2026 entries before public use
- verify volume, issue, pages, and article numbers
- standardize BibTeX field ordering and capitalization style
- confirm whether preprint entries need `note = {Preprint}` or server-specific metadata
- run a final citation rendering check in the intended export tool before public use

## 9. Comparator Citation Readiness

Direct peptide comparator citation coverage is present for:

- BrainPeps: `brainpeps_2012`
- B3Pdb: `b3pdb_2021`
- B3Pred: `b3pred_2021`
- BBPpred: `bbppred_2021`
- BBPpredict: `bbppredict_2022`
- BBB-PEP-prediction: `naseem2023bbbpep`
- Augur: `augur_2024`
- BrainPepPass: `brainpeppass_2024`
- DeepB3P: `tang2025deepb3p`
- DeepB3Pred: `arif2025deepb3pred`
- ESM-BBB-Pred: `esm_bbb_pred_2025`
- B3BPFN: `b3bpfn_2026`

Adjacent compound BBB predictor citation coverage is present for:

- LightBBB: `shaker2021lightbbb`
- Deep-B3: `tang2022deepb3`
- DeePred-BBB: `kumar2022deepredbbb`
- DeepBBBP: `parakkal2022deepbbbp`
- TITAN-BBB: `oliveira2026titanbbb`

Readiness conclusion:

- comparator coverage is sufficient for internal Word review after metadata cleanup
- comparator coverage is not public-ready until final source-to-claim review confirms that no direct benchmark, matched dataset, leaderboard, superiority, state-of-the-art, or redistribution implication is introduced

## 10. Dataset / Source Citation Readiness

Dataset/source citation readiness remains incomplete.

Known source/provenance issues:

- exact upstream dataset files/version remain unresolved
- B3Pred/B3Pdb source terms and license remain unresolved
- required attribution wording remains unresolved
- original positive/negative label-source criteria remain unresolved
- local processed dataset redistribution permission remains unresolved
- raw upstream data files are not present in `data/raw/`
- local processed row-level artifacts are high-risk for public redistribution

The B3Pdb and B3Pred bibliography entries support background, lineage, and direct peptide predictor context. They do not by themselves establish local processed dataset redistribution permission, exact provenance closure, original label-source criteria, or matched dataset comparability.

Before public submission, the package needs a dataset/source citation decision that separates:

- citation of B3Pdb/B3Pred papers as scientific context
- attribution to any downloaded upstream dataset files
- source terms/license and redistribution permission
- label-source criteria and any limitations in label interpretation

## 11. Software / Tool Citation Readiness

Current software/tool citations:

- pandas: `pandas_2010`
- scikit-learn: `scikit_learn_2011`
- matplotlib: `matplotlib_2007`

These cover the tools currently cited in manuscript v0.6. Internal Word draft readiness requires confirming that the software citation policy is acceptable for the intended review format.

Before public export:

- confirm whether any additional tools used in the manuscript/export path require citation
- confirm whether Python, NumPy, SciPy, Biopython, or workflow/export tools are used materially enough to cite
- confirm versions through environment or lockfile review only in a later task if needed
- avoid adding new software citations unless the manuscript text actually uses or needs them

## 12. Figure / Table Inventory Needs

Supplement v0.2 provides placeholders, but the final inventory is incomplete.

Candidate figures requiring review:

- Figure S1: `figures/dataset_distribution.png`
- Figure S2: `figures/legacy_vs_rerun_metrics.png`
- Figure S3: `figures/benchmark_workflow_outputs.png`
- Figure S4: `figures/regenerated_rf_feature_importance.png`
- Hold: `figures/candidate_ranking_preview.png`

Candidate tables requiring review:

- Table S1: dataset surface summary without row-level entries
- Table S2: random-stratified aggregate metrics
- Table S3: leakage-aware aggregate metrics
- Table S4: leakage audit aggregate summary without sequence-pair rows
- Table S5: artifact release allow/hold matrix
- Hold: row-level prediction, ranking, split, group, or leakage-pair tables

Required inventory decisions:

- decide main-text versus supplement placement
- finalize figure/table numbering
- verify each figure/table is aggregate-safe
- confirm no row-level sequence, label, prediction, ranking, split, group, or sequence-pair leakage data are included
- hold candidate-ranking preview unless explicitly approved after source/legal and claim-boundary review

## 13. Caption Requirements

Every figure/table caption should include:

- artifact path or source
- artifact type
- split/evaluation context
- random-stratified, leakage-aware sensitivity, leakage audit, or documentation-only status
- dataset/provenance caveat where relevant
- public-release posture if internal-only

Required caption boundaries:

- in-silico computational benchmark
- bounded sensitivity estimate
- pre-experimental prioritization only if prioritization is discussed
- model-level artifact, not mechanistic proof, for feature importance
- dataset source, licensing, redistribution, and label-source criteria remain unresolved

Forbidden caption implications:

- leakage-free status
- robust generalization
- validated BBB delivery
- biological validation
- wet-lab validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- dataset redistribution permission
- state-of-the-art performance
- AlphaFold-level maturity, adoption, performance, or validation

## 14. Export Manifest Requirements

No public supplement export has been generated for v0.2.

Future export manifest should record:

- manuscript version
- supplement version and date
- bibliography version/status
- citation rendering tool and style
- included figures and tables
- source artifact path for each included figure/table
- excluded row-level artifacts
- aggregate artifact allowlist version
- row-level artifact blocklist version
- data/code availability wording version
- source-to-claim audit version
- figure/table/caption review status
- founder/manual approval status
- final public posting decision

The manifest should explicitly state whether the package is internal-only or approved for public submission. Current export status is blocked / not public-submission-ready.

## 15. Word Internal-Review Draft Readiness

Bibliography readiness for internal Word draft: **not ready yet, but close**.

Reason:

- all manuscript citation keys resolve
- the supplement has no missing citation keys
- one confusing unused entry remains
- metadata cleanup and citation rendering checks remain pending

Minimum required before internal Word draft:

- resolve or document `deepb3p3_2023`
- clean or approve `and others` author fields
- verify titles, DOI, journal/venue, year, volume/issue/page/article fields
- run a local citation rendering/export check in the intended Word-draft path

Supplement/export readiness for internal Word draft: **not ready yet**.

Reason:

- supplement v0.2 is internally safe as a draft
- figure/table numbering is not final
- captions are placeholders/requirements rather than final captions
- export manifest is a placeholder
- public-safe artifact allowlist and row-level blocklist still need final review for the package
- no DOCX or PDF export has been generated or checked

## 16. bioRxiv Public-Submission Blockers

Public bioRxiv remains **Hold / not submission-ready**.

Public-submission blockers:

- dataset source/license/attribution/redistribution decision unresolved
- original label-source criteria unresolved
- row-level artifacts remain blocked from public release
- final data/code availability wording not approved
- repository URL, release tag/commit, software license, and release policy not finalized
- bibliography metadata cleanup and citation formatting/export check incomplete
- final source-to-claim review incomplete
- supplement/export package incomplete
- figure/table numbering and captions incomplete
- public-safe aggregate artifact allowlist not approved
- founder/manual approval missing
- final public posting decision missing

Bibliography readiness for public bioRxiv: **not ready**.

Supplement/export readiness for public submission: **not ready**.

## 17. Recommended Task Sequence

1. Bibliography cleanup draft
   - resolve `deepb3p3_2023`
   - clean metadata fields in `references.bib`
   - keep citation key changes conservative or provide a key-migration note
   - run citation rendering checks without changing manuscript claims

2. Export manifest draft
   - enumerate included/excluded artifacts
   - map each figure/table to source artifact, caption, release posture, and row-level risk
   - include bibliography status, data/code wording version, and approval state

3. Word internal-review draft package
   - export manuscript and supplement only after bibliography and export-manifest draft checks
   - include internal-only status
   - verify figure/table/caption layout and citation rendering

4. Founder/manual approval packet
   - package remaining source/license, data/code availability, artifact allow/hold, bibliography, source-to-claim, and public posting decisions
   - keep public bioRxiv as Hold until explicit approval is documented

## 18. Required Claim-Boundary Reminder

The current evidence package supports only bounded computational benchmark-signal and cautious candidate-prioritization framing before experimental validation.

Do not claim:

- public bioRxiv readiness
- dataset redistribution permission
- row-level artifact public-release permission
- wet-lab validation
- biological validation
- in-vivo validation
- therapeutic efficacy
- clinical efficacy
- robust generalization
- leakage-free status
- matched leaderboard comparison
- state-of-the-art performance
- AlphaFold-level performance, adoption, maturity, or validation

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.

## 19. Required Conclusions

Bibliography is **not ready for internal Word draft** until metadata cleanup, `deepb3p3_2023` resolution/documentation, and citation rendering checks are complete. It is key-complete for manuscript v0.6.

Bibliography is **not ready for public bioRxiv**.

Supplement/export is **not ready for internal Word draft** until figure/table numbering, final captions, export manifest, and internal export checks are complete.

Supplement/export is **not public-submission-ready**.

Public bioRxiv remains **Hold / not submission-ready**.

Dataset redistribution remains unresolved.

Row-level artifacts remain blocked from public release.
