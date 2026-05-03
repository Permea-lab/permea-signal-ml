# Citation Placeholder Map for bioRxiv v0.1

## Purpose

This map shows where verified reference placeholders should later be inserted.

No manuscript text is modified in this task. No citation insertion happens here. This is a planning artifact for later bibliography and manuscript-editing work.

## Placeholder-to-section table

| Placeholder key | Proposed manuscript section | Target sentence/claim type | Reference role | Insertion priority | Caveat |
| --- | --- | --- | --- | --- | --- |
| `REF_BRAINPEPS_DATABASE` | Introduction / Related Work / Dataset lineage | BBB peptide database and heterogeneous BBB transport evidence | Database-lineage and background support | Priority 1 | Do not use to claim Permea validation or dataset licensing closure. |
| `REF_B3PDB_DATABASE` | Related Work / Dataset lineage | B3Pdb as BBB-penetrating peptide archive | Dataset/database-lineage support | Priority 1 | Do not imply current processed dataset redistribution rights are resolved. |
| `REF_B3PRED` | Related Work / Dataset lineage / comparator | Random-forest BBB peptide predictor and B3Pdb-derived benchmark lineage | Direct comparator and likely dataset-lineage support | Priority 1 | Do not overuse to claim Permea dataset novelty. |
| `REF_BBPPRED` | Related Work | Early sequence-based BBB peptide classifier | Predictor-lineage and logistic-regression comparator | Priority 2 | Comparator context only. |
| `REF_BBPPREDICT` | Related Work / Evaluation | Nested-CV and independent-test comparator | Evaluation comparator | Priority 2 | Do not imply Permea used the same evaluation design. |
| `REF_PRAUC_IMBALANCE` | Methods / Evaluation metrics | PR-AUC under class imbalance | Metric-interpretation support | Priority 1 | Does not validate model generalization. |
| `REF_MCC_BINARY_CLASSIFICATION` | Methods / Evaluation metrics | MCC as useful binary-classification metric | Metric-interpretation support | Priority 1 | Does not strengthen biological interpretation. |
| `REF_SCIKIT_LEARN` | Methods / Software | scikit-learn implementation | Software citation for Logistic Regression, Random Forest, StratifiedKFold, and metrics | Priority 1 | Software support only. |
| `REF_PANDAS` | Methods / Software | data processing | Software citation for dataframe/CSV processing | Priority 2 | Software support only. |
| `REF_MATPLOTLIB` | Methods / Software | figure generation | Software citation for figure generation | Priority 2 | Software support only. |
| `REF_DATASETS_FOR_DATASETS` | Dataset / Limitations / Data availability | dataset documentation/provenance discipline | Documentation framework support | Priority 2 | Needs final metadata completion; does not resolve dataset licensing. |
| `REF_PROTPARAM_FEATURES` | Methods / Features | pI/GRAVY/physicochemical descriptor support | Feature/tool support | Priority 3 | Canonical citation still needs final verification. |
| `REF_PRACTICPP_IMBALANCE` | Related Work / Benchmark hygiene | adjacent CPP benchmark imbalance/dedup/negative-label caution | Adjacent benchmark-hygiene support | Priority 3 | Adjacent CPP context only, not direct BBB validation. |

## Citation insertion priority

### Priority 1

- `REF_BRAINPEPS_DATABASE`
- `REF_B3PDB_DATABASE`
- `REF_B3PRED`
- `REF_PRAUC_IMBALANCE`
- `REF_MCC_BINARY_CLASSIFICATION`
- `REF_SCIKIT_LEARN`

### Priority 2

- `REF_BBPPRED`
- `REF_BBPPREDICT`
- `REF_PANDAS`
- `REF_MATPLOTLIB`
- `REF_DATASETS_FOR_DATASETS`

### Priority 3

- `REF_PRACTICPP_IMBALANCE`
- `REF_PROTPARAM_FEATURES`
- extended related-work references needing one more verification pass

## Do-not-cite-yet list

- `REF_PEPBENCHMARK_KMER_HOMOLOGY`
- `REF_PERSEUCPP`
- `REF_AUGUR`
- `REF_BRAINPEPPASS`
- `REF_ESM_BBB_PRED`
- `REF_B3BPFN`
- `REF_DEEPB3P3`
- `REF_BBB_SHUTTLE_REVIEW`
- `REF_CPP_CLINICAL_REVIEW`

## Next insertion task

Recommended next task: Task 045 — Create Draft references.bib from Verified Reference Pack.

Alternative: Task 045 — Insert Citation Placeholders into `PREPRINT_DRAFT_V0_1.md` after references.bib preparation.
