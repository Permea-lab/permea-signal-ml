# Citation Placeholder Map for bioRxiv v0.1 - Second Pass

## Purpose

This map records where the second-pass verified references may support future citation insertion.

No manuscript text is modified by this map. Citation placeholders should be inserted only after `references.bib` contains the corresponding BibTeX key.

## Placeholder-to-section table

| Placeholder key | Draft BibTeX key | Proposed manuscript section | Target sentence/claim type | Reference role | Insertion priority | Caveat |
| --- | --- | --- | --- | --- | --- | --- |
| `REF_BBB_SHUTTLE_REVIEW` | `bbb_shuttle_review_2016` | Introduction / Related Work | BBB shuttle peptide framing and brain-delivery context | Biological background | Priority 1 | Background only; not Permea validation. |
| `REF_AUGUR` | `augur_2024` | Related Work | Modern BBB peptide predictor using data augmentation and imbalance handling | Comparator context | Priority 2 | Do not imply direct benchmark comparability or superiority. |
| `REF_BRAINPEPPASS` | `brainpeppass_2024` | Related Work | Structure-aware or chemically richer BBB peptide prediction | Comparator context | Priority 2 | Do not imply current feature set captures structure-aware evidence. |
| `REF_DEEPB3P3` | `deepb3p3_2023` | Related Work | Transformer/capsule-style BBB peptide predictor | Comparator context | Priority 2 | Do not imply Permea uses deep model architecture. |
| `REF_ESM_BBB_PRED` | `esm_bbb_pred_2025` | Related Work | PLM/deep-learning BBB peptide predictor | Comparator context | Priority 2 | Do not imply Permea PLM benchmark results. |
| `REF_B3BPFN` | `b3bpfn_2026` | Related Work | Recent PLM/tabular foundation-model style BBB peptide predictor | Comparator context | Priority 3 | Context only; no SOTA claim. |
| `REF_PERSEUCPP` | `perseucpp_2025` | Related Work / Limitations | Adjacent CPP descriptor and independent-validation context | Adjacent benchmark context | Priority 3 | CPP context is adjacent, not direct BBB validation. |
| `REF_CPP_COMPUTATIONAL_REVIEW` | `cpp_computational_review_2022` | Introduction / Discussion | Broader computational CPP/B3PP prediction landscape | Optional review context | Priority 3 | Defer if author metadata is required for bibliography. |
| `REF_PEPBENCHMARK` | deferred | Related Work / Benchmark hygiene | Peptide benchmark standardization | Partial benchmark lead | Do not cite yet | Do not make k-mer/homology claims without PDF/supplement support. |

## Citation insertion priority

### Priority 1

- `REF_BBB_SHUTTLE_REVIEW`

### Priority 2

- `REF_AUGUR`
- `REF_BRAINPEPPASS`
- `REF_DEEPB3P3`
- `REF_ESM_BBB_PRED`

### Priority 3

- `REF_B3BPFN`
- `REF_PERSEUCPP`
- `REF_CPP_COMPUTATIONAL_REVIEW`

## Do-not-cite-yet list

- `REF_PEPBENCHMARK`

## Boundary rules for insertion

- Use only keys present in `references.bib`.
- Cite related work to establish landscape, not to claim Permea superiority.
- Keep leakage and benchmark-hygiene claims tied to repo audit outputs and verified references only.
- Do not insert partial references into manuscript text.
