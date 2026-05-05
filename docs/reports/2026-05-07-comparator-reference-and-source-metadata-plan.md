# Comparator Reference and Source Metadata Plan - 2026-05-07

## 1. Purpose and Scope

This report plans comparator reference and source metadata work for the Permea first-paper manuscript v0.3.

Scope:

- Identify direct BBB-penetrating peptide comparators and adjacent compound-level BBB predictors.
- Check whether each comparator already has a usable citation key in `references.bib`.
- Identify missing or incomplete citation/source metadata.
- Map sources to manuscript claim use.
- Define a safe update sequence for future `references.bib` and manuscript citation work.

This is a planning report only. It does not modify the manuscript, `references.bib`, data files, result artifacts, figure artifacts, model outputs, split artifacts, or leakage-audit artifacts.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Current Manuscript and Reference Status

Current working manuscript:

- `docs/paper/permea-first-paper-manuscript-v0-3.md`

Current manuscript status:

- v0.3 is suitable for internal review.
- v0.3 is the current working manuscript.
- The manuscript separates direct BBB-penetrating peptide comparators from adjacent compound-level BBB predictors.
- The manuscript explicitly does not claim state-of-the-art performance.
- Dataset redistribution remains unresolved.

Current bibliography status:

- `references.bib` contains existing keys for several BBB peptide database/predictor, metric, and software references.
- Existing bibliography metadata remains incomplete in places and still needs human/source verification.
- Several comparator references needed for the expanded BBB landscape are not yet present as verified keys.
- No new keys should be added without verified source metadata.

## 3. Direct Peptide Comparator Table

| Comparator name | Role in manuscript | Existing citation key, if any | Missing citation key, if needed | Metadata completeness status | Source verification needed |
| --- | --- | --- | --- | --- | --- |
| BrainPeps | Earlier BBB peptide database context and source-lineage background. | `brainpeps_2012` | None currently required. | Usable with verification needed; author field abbreviated with `and others`; volume/pages may need verification. | Verify full metadata and source-to-claim use. |
| B3Pdb | Direct BBB-penetrating peptide archive/database lineage. | `b3pdb_2021` | None currently required. | Usable with verification needed; author field abbreviated with `and others`; volume/pages may need verification. | Verify full metadata and whether it is the correct source for any dataset-lineage claim. |
| B3Pred | Direct BBB-penetrating peptide predictor lineage; B3Pdb/B3Pred-like positioning. | `b3pred_2021` | None currently required. | Usable with verification needed; author field abbreviated with `and others`; volume/issue/article fields may need verification. | Verify full metadata and avoid implying Permea is a matched B3Pred benchmark comparison. |
| BBPpred | Direct sequence-based BBB peptide predictor context. | `bbppred_2021` | None currently required. | Usable with verification needed; author field abbreviated with `and others`; volume/pages may need verification. | Verify full metadata and exact naming distinction from BBPpredict. |
| BBPpredict | Direct BBB-penetrating peptide web-service/predictor context. | `bbppredict_2022` | None currently required. | Usable with verification needed; author field abbreviated with `and others`; article metadata may need verification. | Verify full metadata and source-to-claim use. |
| BBB-PEP-prediction | Direct peptide comparator identified in landscape review. | None found in `references.bib`. | Source-required key needed after verification. | Not available. | Identify exact source, title, authors, venue, year, DOI/URL, and whether this is distinct from existing BBP/BBB peptide predictor keys. |
| Augur | Direct/recent BBB-penetrating peptide prediction context. | `augur_2024` | None currently required. | Usable with verification needed; author field abbreviated with `and others`; metadata otherwise directionally present. | Verify full metadata and ensure it is used as related work, not as evidence of Permea superiority. |
| DeepB3P | Direct peptide comparator named in landscape review. | Possibly `deepb3p3_2023`, but name/identity requires verification. | Source-required if distinct from `deepb3p3_2023`. | Existing key may be usable only after identity verification. | Verify whether DeepB3P, DeepB3P3, and DeepB3Pred refer to distinct works or naming variants. |
| DeepB3Pred | Direct peptide comparator named in landscape review. | None found as an explicit `DeepB3Pred` key. | Source-required if distinct from existing keys. | Not available as explicit key. | Verify exact source and whether it is covered by `deepb3p3_2023` or requires a separate entry. |
| BrainPepPass | Related BBB-penetrating peptide predictor context already in bibliography. | `brainpeppass_2024` | None currently required. | Usable with verification needed; author field abbreviated with `and others`. | Verify full metadata and whether manuscript should mention it as related peptide predictor context. |
| ESM-BBB-Pred | Related recent BBB peptide predictor context already in bibliography. | `esm_bbb_pred_2025` | None currently required if retained. | Usable with publication-status verification needed; author field abbreviated with `and others`. | Verify publication status and exact metadata before broader review. |
| B3BPFN | Related recent BBB peptide predictor context already in bibliography. | `b3bpfn_2026` | None currently required if retained. | Usable with publication-status verification needed; author field abbreviated with `and others`. | Verify publication status and exact metadata before broader review. |

## 4. Adjacent Compound BBB Predictor Table

| Comparator name | Role in manuscript | Existing citation key, if any | Missing citation key, if needed | Metadata completeness status | Source verification needed |
| --- | --- | --- | --- | --- | --- |
| LightBBB | Adjacent compound-level BBB permeability predictor context. | None found. | Source-required key needed after verification. | Not available. | Verify exact source, model/task type, compound/SMILES scope, authors, venue, year, DOI/URL. |
| Deep-B3 | Adjacent compound-level BBB permeability predictor context. | None found. | Source-required key needed after verification. | Not available. | Verify exact source and ensure it is not confused with peptide-focused DeepB3P/DeepB3Pred names. |
| DeePred-BBB | Adjacent compound/SMILES BBB permeability predictor context. | None found. | Source-required key needed after verification. | Not available. | Verify exact source and maintain adjacent-only claim use. |
| DeepBBBP | Adjacent compound-level BBB permeability predictor context. | None found. | Source-required key needed after verification. | Not available. | Verify exact source, task, and metadata before adding. |
| TITAN-BBB | Adjacent compound/SMILES BBB permeability predictor context. | None found. | Source-required key needed after verification. | Not available. | Verify exact source and use only to support adjacent compound-level context. |

## 5. Dataset / Source-Lineage Citation Table

| Source-lineage item | Current repo status | Existing citation key, if any | Metadata completeness status | Manual/source verification needed |
| --- | --- | --- | --- | --- |
| B3Pdb | Existing bibliography key supports archive/database background. | `b3pdb_2021` | Usable with verification needed. | Verify whether this is only background lineage or also the correct upstream source for any Permea dataset rows. Do not assume dataset provenance. |
| B3Pred | Existing bibliography key supports prior predictor/context. | `b3pred_2021` | Usable with verification needed. | Verify whether any Permea dataset surface derives from B3Pred data/downloads or only uses B3Pred as background lineage. |
| B3Pred dataset/download/source terms | Unresolved in repo reports. | None confirmed. | Source-required. | Need exact source page/publication/download terms/license/label-source criteria before any redistribution or strong attribution claim. |
| Imported legacy processed dataset | Repo documents `legacy_bbb_import` as operational source metadata. | None confirmed. | Source-required. | Original source identity, license, redistribution terms, and label-source criteria remain unresolved. |

Important boundary:

Existing B3Pdb/B3Pred keys may support background and lineage after verification, but they do not currently close Permea's dataset provenance, licensing, redistribution, or label-source criteria.

## 6. Source-to-Claim Mapping

| Manuscript claim type | Candidate source support | Safe use | Unsafe use to avoid |
| --- | --- | --- | --- |
| BBB delivery and shuttle background | `bbb_shuttle_review_2016` | General BBB shuttle/delivery motivation. | Do not use as validation of Permea model predictions. |
| BBB peptide database lineage | `brainpeps_2012`, `b3pdb_2021` | Background for peptide databases/archives. | Do not imply exact Permea dataset provenance unless manually verified. |
| Prior BBB peptide predictor lineage | `b3pred_2021`, `bbppred_2021`, `bbppredict_2022`, `augur_2024`, `brainpeppass_2024`, `deepb3p3_2023`, `esm_bbb_pred_2025`, `b3bpfn_2026` | Related work and comparator landscape. | Do not imply Permea is state-of-the-art, validated, or directly benchmarked against these systems. |
| Direct comparator gaps | BBB-PEP-prediction, DeepB3P, DeepB3Pred | Mark as source-required until verified. | Do not add guessed keys or claim direct comparison. |
| Adjacent compound BBB predictor context | LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, TITAN-BBB | Broader BBB prediction context only. | Do not describe as direct peptide comparators or matched benchmark baselines. |
| Metric interpretation | `saito_rehmsmeier_2015_prauc`, `chicco_jurman_2020_mcc` | Explain PR-AUC and MCC relevance under imbalance. | Do not use metric citations to imply biological validation or robust generalization. |
| Tooling | `scikit_learn_2011`, `pandas_2010`, `matplotlib_2007` | Software/method tooling attribution. | Do not use tooling citations as scientific validation. |
| Internal baseline and sensitivity metrics | Repo result paths and audit docs. | Artifact traceability for reported Permea results. | Do not treat as external validation. |
| Dataset availability and redistribution | Dataset decision package plus future verified source/legal records. | Conservative unresolved status. | Do not claim redistribution permission without explicit source/legal approval. |

## 7. `references.bib` Update Candidates

### Existing Keys to Verify and Retain

Highest-priority existing keys for v0.3 source-to-claim review:

- `brainpeps_2012`
- `b3pdb_2021`
- `b3pred_2021`
- `bbppred_2021`
- `bbppredict_2022`
- `augur_2024`
- `deepb3p3_2023`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `bbb_shuttle_review_2016`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`

Verification needed before broader review or public posting:

- full author lists or approved abbreviated-author policy
- exact titles and protected capitalization
- journal/venue names
- DOI/URL
- volume, issue, page, or article-number fields
- publication status for recent/future-dated entries
- exact source-to-claim fit

### New Keys That May Be Needed After Verification

Candidate new keys to add only after source metadata is verified:

- `bbb_pep_prediction_[year]` or another verified key for BBB-PEP-prediction
- `deepb3p_[year]` if distinct from `deepb3p3_2023`
- `deepb3pred_[year]` if distinct from `deepb3p3_2023`
- `lightbbb_[year]`
- `deep_b3_[year]`
- `deepred_bbb_[year]` or exact verified DeePred-BBB key spelling
- `deepbbbp_[year]`
- `titan_bbb_[year]`
- verified dataset/source/download/terms key if a citable source exists

Do not use these placeholder key names in manuscript citations until exact metadata is verified and a deliberate naming convention is chosen.

## 8. What Not to Add Yet Due to Insufficient Verification

Do not add the following yet:

- BBB-PEP-prediction reference metadata
- DeepB3P reference metadata if not confirmed distinct from `deepb3p3_2023`
- DeepB3Pred reference metadata if not confirmed distinct from `deepb3p3_2023`
- LightBBB reference metadata
- Deep-B3 reference metadata
- DeePred-BBB reference metadata
- DeepBBBP reference metadata
- TITAN-BBB reference metadata
- original Permea dataset source/download/license metadata
- source terms or redistribution-permission citations
- repository release/archive citation

Reason:

- The repo currently identifies these as landscape or source-required items, but exact source metadata has not been verified in the repository materials reviewed for this task.
- Adding guessed fields would make the bibliography appear more complete than it is.

## 9. Recommended Safe Reference-Update Sequence

1. Freeze the v0.3 claim surface before editing references.
2. Verify direct peptide comparator sources first:
   - B3Pdb / B3Pred
   - BBPpred / BBPpredict
   - BBB-PEP-prediction
   - Augur
   - DeepB3P / DeepB3Pred identity and naming
3. Verify adjacent compound predictor sources second:
   - LightBBB
   - Deep-B3
   - DeePred-BBB
   - DeepBBBP
   - TITAN-BBB
4. Verify existing `references.bib` metadata for all keys used by v0.3.
5. Add only verified new entries, preserving a consistent key naming convention.
6. Do not add dataset/source/license entries until source terms and provenance are manually confirmed.
7. Update manuscript citations only after `references.bib` has verified keys.
8. Run a key-level citation audit.
9. Run a sentence-level source-to-claim audit.
10. Keep public bioRxiv status on Hold until citation, dataset, supplement/export, founder/manual, and public-posting blockers are resolved.

## 10. Recommended Next Task

Recommended next task:

**Task 134 - Verify Comparator Sources and Prepare Safe references.bib Update Draft**

Suggested scope:

- Use manually verified source metadata or explicitly approved source documents.
- Add only verified comparator bibliography entries.
- Do not change manuscript claims or metrics.
- Keep dataset/source/legal decisions unresolved unless founder/legal review provides explicit documentation.

Alternative if source metadata is not yet available:

**Task 134 - Commit Comparator Reference and Source Metadata Plan**

## Required Conclusion

- Manuscript v0.3 remains internal-review ready.
- `references.bib` still needs comparator/source metadata work before broader review.
- Dataset redistribution remains unresolved.
- Public bioRxiv remains **Hold / not submission-ready**.

## No-Change Confirmation

This planning task did not modify:

- manuscript v0.3
- manuscript v0.2
- `references.bib`
- data files
- result artifacts
- figure artifacts
- model artifacts
- split artifacts
- leakage-audit artifacts

