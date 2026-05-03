# Verified Reference Pack for bioRxiv v0.1

## Purpose

This pack records the first set of externally verified reference candidates for the bioRxiv v0.1 preprint.

This is not the final bibliography, does not insert citations into the manuscript, and does not create `references.bib`. References are ready for structured bibliography preparation only where metadata is sufficiently verified. References with incomplete metadata remain marked as "Partially verified / needs final metadata completion" or "Partially verified / needs canonical citation verification."

## Verification status legend

- Metadata verified
- Partially verified / needs final metadata completion
- Partially verified / needs canonical citation verification
- Claim relevance verified
- Ready for bibliography preparation
- Keep in queue

## Verified reference table

| Placeholder key | Reference | Year | Venue | DOI/identifier | Verification status | Supported manuscript role | Claim-boundary caveat | Bibliography readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REF_BRAINPEPS_DATABASE` | Van Dorpe et al.; "Brainpeps: the blood-brain barrier peptide database" | 2012 | Brain Structure & Function | DOI: `10.1007/s00429-011-0375-0` | Metadata verified; claim relevance verified | BBB peptide database lineage; heterogeneous BBB transport evidence; positive/negative BBB transport information | Supports source/context only; does not validate Permea predictions or dataset licensing. | Ready for bibliography preparation |
| `REF_B3PDB_DATABASE` | Kumar et al.; "B3Pdb: an archive of blood-brain barrier-penetrating peptides" | 2021 | Brain Structure and Function | DOI: `10.1007/s00429-021-02341-5` | Metadata verified; claim relevance verified | B3Pdb lineage and BBB-penetrating peptide database context | Supports database lineage only; does not resolve current processed dataset redistribution status. | Ready for bibliography preparation |
| `REF_B3PRED` | Kumar et al.; "B3Pred: A Random-Forest-Based Method for Predicting and Designing Blood-Brain Barrier Penetrating Peptides" | 2021 | Pharmaceutics | DOI: `10.3390/pharmaceutics13081237` | Metadata verified; claim relevance verified | Direct comparator and likely dataset-lineage reference | Do not overuse to claim Permea dataset novelty; note B3Pred dataset construction includes B3Pdb positives and multiple negative sets. | Ready for bibliography preparation |
| `REF_BBPPRED` | Dai et al.; "BBPpred: Sequence-Based Prediction of Blood-Brain Barrier Peptides with Feature Representation Learning and Logistic Regression" | 2021 | Journal of Chemical Information and Modeling | DOI: `10.1021/acs.jcim.0c01115` | Metadata verified; claim relevance verified | Early BBB peptide classifier / logistic-regression comparator | Comparator context only; not evidence of Permea performance superiority. | Ready for bibliography preparation |
| `REF_BBPPREDICT` | Chen et al.; "BBPpredict: A Web Service for Identifying Blood-Brain Barrier Penetrating Peptides" | 2022 | Frontiers in Genetics | DOI: `10.3389/fgene.2022.845747` | Metadata verified; claim relevance verified | Evaluation comparator; nested-CV and independent-test framing | Comparator context only; do not imply Permea reproduces its evaluation design. | Ready for bibliography preparation |
| `REF_PRAUC_IMBALANCE` | Saito & Rehmsmeier; "The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets" | 2015 | PLOS ONE | DOI: `10.1371/journal.pone.0118432` | Metadata verified; claim relevance verified | Justifies PR-AUC emphasis under imbalanced labels | Supports metric interpretation only; does not validate benchmark generalization. | Ready for bibliography preparation |
| `REF_MCC_BINARY_CLASSIFICATION` | Chicco & Jurman; "The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation" | 2020 | BMC Genomics | DOI: `10.1186/s12864-019-6413-7` | Metadata verified; claim relevance verified | Justifies MCC reporting alongside ROC-AUC/PR-AUC | Supports metric interpretation only; does not strengthen biological claims. | Ready for bibliography preparation |
| `REF_SCIKIT_LEARN` | Pedregosa et al.; "Scikit-learn: Machine Learning in Python" | 2011 | Journal of Machine Learning Research, 12:2825-2830 | Not provided in task context | Metadata verified; claim relevance verified | Software citation for Logistic Regression, Random Forest, StratifiedKFold, and metrics | Software support only; not model-result validation. | Ready for bibliography preparation |
| `REF_PANDAS` | McKinney; "Data Structures for Statistical Computing in Python" | 2010 | SciPy Proceedings | DOI: `10.25080/Majora-92bf1922-00a` | Metadata verified; claim relevance verified | Software citation for dataframe/CSV processing | Software support only. | Ready for bibliography preparation |
| `REF_MATPLOTLIB` | Hunter; "Matplotlib: A 2D Graphics Environment" | 2007 | Computing in Science & Engineering | DOI: `10.1109/MCSE.2007.55` | Metadata verified; claim relevance verified | Software citation for figure generation | Software support only. | Ready for bibliography preparation |
| `REF_DATASETS_FOR_DATASETS` | Gebru et al.; "Datasheets for Datasets" | 2021 | Communications of the ACM | DOI not provided in current verified pack | Partially verified / needs final metadata completion; claim relevance verified | Dataset documentation/provenance discipline | Supports documentation discipline only; does not resolve dataset attribution/licensing. | Keep in queue until final metadata completion |
| `REF_PROTPARAM_FEATURES` | ExPASy ProtParam; "ProtParam" | Not provided in task context | Tool/reference support | Canonical paper or stable identifier not provided in current verified pack | Partially verified / needs canonical citation verification; claim relevance verified as tool support | pI, GRAVY, amino-acid composition, and physicochemical feature explanation | Treat as feature/tool support only; exact canonical citation still needs final verification. | Keep in queue until canonical citation verification |
| `REF_PRACTICPP_IMBALANCE` | Shi et al.; "PractiCPP" | 2024 | Bioinformatics | DOI: `10.1093/bioinformatics/btae058` | Metadata verified; claim relevance verified | Adjacent CPP benchmark realism, extreme imbalance, deduplication, conflicting-label removal, negative/unlabeled caution | Adjacent CPP benchmark context only; not direct BBB validation. | Ready for bibliography preparation |

## How these references should be used

### Introduction / biological background

- `REF_BRAINPEPS_DATABASE`
- `REF_B3PDB_DATABASE`

### Dataset lineage / related work

- `REF_BRAINPEPS_DATABASE`
- `REF_B3PDB_DATABASE`
- `REF_B3PRED`
- `REF_BBPPRED`
- `REF_BBPPREDICT`

### Methods / metrics

- `REF_PRAUC_IMBALANCE`
- `REF_MCC_BINARY_CLASSIFICATION`

### Leakage and benchmark hygiene

- `REF_PRACTICPP_IMBALANCE`

### Dataset documentation and reproducibility

- `REF_DATASETS_FOR_DATASETS`

### Software citations

- `REF_SCIKIT_LEARN`
- `REF_PANDAS`
- `REF_MATPLOTLIB`
- `REF_PROTPARAM_FEATURES`

## What these references must not be used to claim

- Permea validated BBB delivery.
- Permea achieved biological validation.
- Current metrics prove robust generalization.
- The dataset is leakage-free.
- Feature importance proves mechanism.
- Dataset licensing is resolved.
- Public preprint submission is ready.

## Remaining unverified references

- `REF_PEPBENCHMARK_KMER_HOMOLOGY`
- `REF_PERSEUCPP`
- `REF_AUGUR`
- `REF_BRAINPEPPASS`
- `REF_ESM_BBB_PRED`
- `REF_B3BPFN`
- `REF_DEEPB3P3`
- `REF_BBB_SHUTTLE_REVIEW`
- `REF_CPP_CLINICAL_REVIEW`

## Recommended next step

Create `references.bib` only after one more verification pass or explicit user approval. Insert citation placeholders only after bibliography mapping is approved.
