# Verified Comparator BibTeX Candidate Pack - 2026-05-07

## 1. Purpose and Scope

This report prepares a verified BibTeX candidate pack for direct BBB-penetrating peptide comparators and adjacent compound-level BBB permeability predictors for the Permea first-paper manuscript v0.3.

This report uses only the verified metadata supplied for Task 135 and the current repository state. It does not use web search.

Scope:

- Check which candidate references are already represented in `references.bib`.
- Classify candidate entries as `already present`, `verify existing`, or `add later`.
- Preserve source-to-claim boundaries.
- Define a safe future update sequence for `references.bib`.

This task does **not** modify `references.bib`, manuscript files, data artifacts, result artifacts, figure artifacts, model outputs, split artifacts, or leakage-audit artifacts.

Public bioRxiv remains **Hold / not submission-ready**.

## 2. Existing Keys Already Present in `references.bib`

The following relevant keys are already present:

- `b3pred_2021`
- `bbppredict_2022`
- `augur_2024`
- `deepb3p3_2023`

Related existing keys also present:

- `brainpeps_2012`
- `b3pdb_2021`
- `bbppred_2021`
- `brainpeppass_2024`
- `esm_bbb_pred_2025`
- `b3bpfn_2026`
- `bbb_shuttle_review_2016`
- `saito_rehmsmeier_2015_prauc`
- `chicco_jurman_2020_mcc`
- `scikit_learn_2011`
- `pandas_2010`
- `matplotlib_2007`

No current `references.bib` key was found for:

- `bbb_pep_prediction_2023`
- `deepb3p_2025`
- `deepb3pred_2025`
- `lightbbb_2021`
- `deep_b3_2022`
- `deepred_bbb_2022`
- `deepbbbp_2022`
- `titan_bbb_2026`

## 3. Candidate Entries Already Covered by Existing Keys

### B3Pred

Decision: `verify existing`

Existing likely key:

- `b3pred_2021`

Verified candidate metadata:

```bibtex
@article{kumar2021b3pred,
  title = {{B3Pred}: A Random-Forest-Based Method for Predicting and Designing Blood--Brain Barrier Penetrating Peptides},
  author = {Kumar, Vinod and Patiyal, Sumeet and Dhall, Anjali and Sharma, Neelam and Raghava, Gajendra Pal Singh},
  journal = {Pharmaceutics},
  volume = {13},
  number = {8},
  pages = {1237},
  year = {2021},
  doi = {10.3390/pharmaceutics13081237}
}
```

Recommended future action:

- Update existing `b3pred_2021` metadata rather than adding duplicate `kumar2021b3pred`, unless a later citation-key policy requires renaming.

Source-to-claim boundary:

- Supports B3Pred method, B3Pdb-derived B3PP modeling, RF baseline, B3Pred webserver, and B3Pred article citation.
- Does not prove that the local Permea processed dataset can be redistributed.

### BBPpredict

Decision: `verify existing`

Existing likely key:

- `bbppredict_2022`

Verified candidate metadata:

```bibtex
@article{chen2022bbppredict,
  title = {{BBPpredict}: A Web Service for Identifying Blood-Brain Barrier Penetrating Peptides},
  author = {Chen, Xue and Zhang, Qianyue and Li, Bowen and Lu, Chunying and Yang, Shanshan and Long, Jinjin and He, Bifang and Chen, Heng and Huang, Jian},
  journal = {Frontiers in Genetics},
  volume = {13},
  pages = {845747},
  year = {2022},
  doi = {10.3389/fgene.2022.845747}
}
```

Recommended future action:

- Update existing `bbppredict_2022` metadata rather than adding duplicate `chen2022bbppredict`, unless a later citation-key policy requires renaming.

Source-to-claim boundary:

- Supports BBPpredict as a direct peptide comparator.
- Supports 326/326 training and 99/99 independent testing structure if manuscript discusses it.
- Does not directly support Permea results.

### Augur

Decision: `verify existing`

Existing likely key:

- `augur_2024`

Verified candidate metadata:

```bibtex
@article{gu2024augur,
  title = {Prediction of Blood--Brain Barrier Penetrating Peptides Based on Data Augmentation with {Augur}},
  author = {Gu, Zhi-Feng and Hao, Yu-Duo and Wang, Tian-Yu and Cai, Pei-Ling and Zhang, Yang and Deng, Ke-Jun and Lin, Hao and Lv, Hao},
  journal = {BMC Biology},
  volume = {22},
  pages = {86},
  year = {2024},
  doi = {10.1186/s12915-024-01883-4}
}
```

Recommended future action:

- Update existing `augur_2024` metadata rather than adding duplicate `gu2024augur`, unless a later citation-key policy requires renaming.

Source-to-claim boundary:

- Supports Augur as a direct peptide comparator.
- Supports data augmentation framing in BBB-penetrating peptide prediction.
- Does not support a claim that Permea outperforms Augur.

### DeepB3P / Existing `deepb3p3_2023` Ambiguity

Decision: `add later` for verified DeepB3P; keep existing `deepb3p3_2023` separate until identity is checked.

Existing possible confusing key:

- `deepb3p3_2023`

Verified DeepB3P candidate metadata:

```bibtex
@article{tang2025deepb3p,
  title = {{DeepB3P}: A Transformer-Based Model for Identifying Blood--Brain Barrier Penetrating Peptides with Data Augmentation Using Feedback {GAN}},
  author = {Tang, Qiang and Chen, Wei},
  journal = {Journal of Advanced Research},
  volume = {73},
  pages = {459--468},
  year = {2025},
  doi = {10.1016/j.jare.2024.08.002}
}
```

Recommended future action:

- Add a new `deepb3p_2025` entry if the manuscript needs DeepB3P specifically.
- Do not overwrite or conflate `deepb3p3_2023` without a deliberate identity check.

Source-to-claim boundary:

- Supports DeepB3P as a direct modern BBBP comparator.
- Supports transformer and feedback GAN augmentation context.
- Does not support direct leaderboard comparison unless dataset/split comparability is established.

## 4. Candidate Entries That Should Be Added Later

### BBB-PEP-prediction

Decision: `add later`

Suggested new key:

- `bbb_pep_prediction_2023`

Verified candidate metadata:

```bibtex
@article{naseem2023bbbpep,
  title = {{BBB-PEP-prediction}: Improved Computational Model for Identification of Blood--Brain Barrier Peptides Using Blending Position Relative Composition Specific Features and Ensemble Modeling},
  author = {Naseem, Ansar and Alturise, Fahad and Alkhalifah, Tamim and Khan, Yaser Daanial},
  journal = {Journal of Cheminformatics},
  volume = {15},
  pages = {110},
  year = {2023},
  doi = {10.1186/s13321-023-00773-1}
}
```

Source-to-claim boundary:

- Supports BBB-PEP-prediction as a direct peptide comparator.
- Supports ensemble/modeling context.
- Does not support Permea model performance.

### DeepB3Pred

Decision: `add later`

Suggested new key:

- `deepb3pred_2025`

Verified candidate metadata:

```bibtex
@article{arif2025deepb3pred,
  title = {{DeepB3Pred}: Blood--Brain Barrier Peptide Predictor Using Stacked {BiGRU} Model with Novel Features},
  author = {Arif, Muhammad and Musleh, Saleh and Alam, Tanvir},
  journal = {BMC Biology},
  volume = {23},
  pages = {325},
  year = {2025},
  doi = {10.1186/s12915-025-02419-0}
}
```

Source-to-claim boundary:

- Supports DeepB3Pred as a direct peptide comparator.
- Because prior landscape notes flagged possible dataset-count inconsistencies, use carefully for related-work context unless exact dataset details are verified.

### LightBBB

Decision: `add later`

Suggested new key:

- `lightbbb_2021`

Verified candidate metadata:

```bibtex
@article{shaker2021lightbbb,
  title = {{LightBBB}: Computational Prediction Model of Blood--Brain-Barrier Penetration Based on {LightGBM}},
  author = {Shaker, Boshra and Yu, Myung-Suk and Song, Jae Seong and Ahn, Sungsoo and Ryu, Jae Yong and Oh, Keun-Soo and Na, Dokyun},
  journal = {Bioinformatics},
  volume = {37},
  number = {8},
  pages = {1135--1139},
  year = {2021},
  doi = {10.1093/bioinformatics/btaa918}
}
```

Source-to-claim boundary:

- Supports adjacent compound-level BBB permeability context.
- Do not treat as direct peptide comparator.

### Deep-B3

Decision: `add later`

Suggested new key:

- `deep_b3_2022`

Verified candidate metadata:

```bibtex
@article{tang2022deepb3,
  title = {A Merged Molecular Representation Deep Learning Method for Blood--Brain Barrier Permeability Prediction},
  author = {Tang, Qiang and Nie, Fulei and Zhao, Qi and Chen, Wei},
  journal = {Briefings in Bioinformatics},
  volume = {23},
  number = {5},
  pages = {bbac357},
  year = {2022},
  doi = {10.1093/bib/bbac357}
}
```

Source-to-claim boundary:

- Supports adjacent compound-level BBB permeability context.
- Important because the name may be confused with DeepB3P or DeepB3Pred.
- Do not treat as direct peptide comparator.

### DeePred-BBB

Decision: `add later`

Preferred new key:

- `deepred_bbb_2022`

Verified candidate metadata:

```bibtex
@article{kumar2022deepredbbb,
  title = {{DeePred-BBB}: A Blood Brain Barrier Permeability Prediction Model with Improved Accuracy},
  author = {Kumar, Rajnish and Sharma, Anju and Alexiou, Athanasios and Bilgrami, Anwar L. and Kamal, Mohammad Amjad and Ashraf, Ghulam Md},
  journal = {Frontiers in Neuroscience},
  volume = {16},
  pages = {858126},
  year = {2022},
  doi = {10.3389/fnins.2022.858126}
}
```

Source-to-claim boundary:

- Supports adjacent compound-level BBB permeability context.
- Uses compounds/SMILES-derived representations, not the BBB peptide sequence task.
- Do not treat as direct peptide comparator.

### DeepBBBP

Decision: `add later`

Suggested new key:

- `deepbbbp_2022`

Verified candidate metadata:

```bibtex
@article{parakkal2022deepbbbp,
  title = {{DeepBBBP}: High Accuracy Blood-Brain-Barrier Permeability Prediction with a Mixed Deep Learning Model},
  author = {Parakkal, Sheryl Cherian and Datta, Riya and Das, Dibyendu},
  journal = {Molecular Informatics},
  volume = {41},
  number = {10},
  pages = {2100315},
  year = {2022},
  doi = {10.1002/minf.202100315}
}
```

Source-to-claim boundary:

- Supports adjacent compound-level BBB permeability context.
- Do not treat as direct peptide comparator.

### TITAN-BBB

Decision: `add later`

Suggested new key:

- `titan_bbb_2026`

Verified candidate metadata:

```bibtex
@article{oliveira2026titanbbb,
  title = {{TITAN-BBB}: Predicting {BBB} Permeability Using Multi-Modal Deep-Learning Models},
  author = {de Oliveira, Gabriel Bianchin and Saeed, Fahad},
  journal = {bioRxiv},
  year = {2026},
  doi = {10.64898/2026.02.15.706007},
  note = {Preprint}
}
```

Source-to-claim boundary:

- Supports adjacent compound-level BBB permeability context only.
- It is a SMILES / multimodal compound BBB model, not a peptide sequence BBBP predictor.
- Do not compare Permea metrics directly against TITAN-BBB.

## 5. Candidate Entries That Need Key-Renaming or De-Duplication Decisions

### Existing-Key Update Versus New Verified-Key Addition

Recommended policy:

- Preserve existing repository keys where they are already used or established.
- Update metadata under existing keys when the verified candidate corresponds to the same work.
- Avoid adding duplicate author-year keys unless a later bibliography policy explicitly renames all keys.

Recommended decisions:

| Work | Current key | Verified candidate key | Recommended action |
| --- | --- | --- | --- |
| B3Pred | `b3pred_2021` | `kumar2021b3pred` | Update existing `b3pred_2021`; do not duplicate. |
| BBPpredict | `bbppredict_2022` | `chen2022bbppredict` | Update existing `bbppredict_2022`; do not duplicate. |
| Augur | `augur_2024` | `gu2024augur` | Update existing `augur_2024`; do not duplicate. |
| DeepB3P | possible confusion with `deepb3p3_2023` | `tang2025deepb3p` | Add `deepb3p_2025` if distinct; keep `deepb3p3_2023` until reviewed. |
| DeePred-BBB | none | `kumar2022deepredbbb` | Add preferred repo key `deepred_bbb_2022`, preserving exact title spelling. |

## 6. Source-to-Claim Boundary Table

| Entry or group | Safe claim support | Unsafe claim use |
| --- | --- | --- |
| B3Pred | B3Pred method, B3Pdb-derived B3PP modeling, RF baseline context, B3Pred webserver/article citation. | Does not establish Permea dataset redistribution rights or prove Permea performance. |
| BBPpredict | Direct peptide comparator and possible train/test structure if explicitly discussed. | Does not support Permea results. |
| BBB-PEP-prediction | Direct peptide comparator and ensemble/modeling context. | Do not use as Permea performance evidence. |
| Augur | Direct peptide comparator and data augmentation context. | Do not claim Permea outperforms Augur. |
| DeepB3P | Modern direct BBBP comparator, transformer and feedback GAN augmentation context. | Do not use for direct leaderboard claims without matched data/splits. |
| DeepB3Pred | Direct peptide comparator with stacked BiGRU context. | Use carefully until dataset-count and source details are checked. |
| LightBBB, Deep-B3, DeePred-BBB, DeepBBBP, TITAN-BBB | Adjacent compound-level BBB permeability context. | Do not treat as direct peptide comparators. Do not compare Permea metrics directly against them. |
| B3Pred dataset/download/source terms | May guide future dataset/source attribution after source terms are reviewed. | CC BY article status does not automatically approve local processed dataset redistribution. |

## 7. Recommended `references.bib` Update Order

1. Back up or inspect current `references.bib` state.
2. Update existing direct peptide comparator metadata first:
   - `b3pred_2021`
   - `bbppredict_2022`
   - `augur_2024`
3. Add missing direct peptide comparator entries:
   - `bbb_pep_prediction_2023`
   - `deepb3p_2025`
   - `deepb3pred_2025`
4. Resolve the `deepb3p3_2023` versus `deepb3p_2025` identity/naming issue without deleting anything unless confirmed.
5. Add adjacent compound-level BBB predictor entries clearly marked by key/name:
   - `lightbbb_2021`
   - `deep_b3_2022`
   - `deepred_bbb_2022`
   - `deepbbbp_2022`
   - `titan_bbb_2026`
6. Do not add dataset/source/license terms until source provenance and redistribution permissions are manually documented.
7. Run citation-key audit after bibliography update.
8. Only then update manuscript citations/source-to-claim wording.

## 8. Entries That Must Remain TODO Until Source / License / Provenance Is Resolved

Dataset/source-lineage TODOs:

- B3Pred dataset/download/source terms.
- Original Permea processed dataset source identity.
- Original upstream source page or publication if distinct from B3Pdb/B3Pred.
- Original label-source criteria.
- Dataset license and redistribution terms.
- Whether row-level processed data may be redistributed.
- Whether derived row-level artifacts, split manifests, group assignments, or predictions may be public.
- Final code/repository archive citation.

Boundary note:

- The B3Pred article states that datasets are available at the B3Pred download page.
- The article being CC BY does not automatically settle row-level redistribution terms for local processed datasets.
- Dataset redistribution remains unresolved unless explicit source terms are documented separately.

## 9. Recommended Codex Task for Applying Safe `references.bib` Updates

Recommended next task:

**Task 136 - Apply Verified Comparator BibTeX Updates to references.bib**

Suggested scope:

- Modify only `references.bib`.
- Preserve existing keys for B3Pred, BBPpredict, and Augur while updating verified metadata.
- Add verified direct peptide comparator entries.
- Add adjacent compound-level BBB predictor entries with clear key names.
- Do not add dataset/source/license entries.
- Do not modify manuscript text yet.
- Do not declare public bioRxiv readiness.

## Required Conclusion

- `references.bib` was not modified in this task.
- `references.bib` can be updated in a later task using this candidate pack.
- Direct peptide comparator references should be prioritized first.
- Adjacent compound BBB predictor references should be clearly marked as adjacent in future manuscript/source-to-claim work.
- Dataset redistribution remains unresolved.
- Public bioRxiv remains **Hold / not submission-ready**.

