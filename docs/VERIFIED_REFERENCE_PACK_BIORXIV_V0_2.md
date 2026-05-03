# Verified Reference Pack for bioRxiv v0.1 - Second Pass

## Purpose

This pack records the second set of verified reference candidates supplied for the bioRxiv v0.1 manuscript-candidate package.

This is not the final bibliography, does not insert citations into the manuscript, and does not modify `references.bib`. References are ready for draft bibliography preparation only where the supplied metadata are sufficient. No author lists, pages, PMIDs, URLs, abstracts, licenses, or missing identifiers are inferred.

## Verification status legend

- Metadata verified from supplied second-pass context
- Claim relevance verified from supplied second-pass context
- Ready for bibliography preparation
- Partially verified / benchmark-standardization lead
- Keep caveat before use

## Verified reference table

| Placeholder key | Reference | Year | Venue | DOI/identifier | Verification status | Supported manuscript role | Claim-boundary caveat | Bibliography readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REF_BBB_SHUTTLE_REVIEW` | Oller-Salvia, Sanchez-Navarro, Giralt, Teixido; "Blood-brain barrier shuttle peptides: an emerging paradigm for brain delivery" | 2016 | Chemical Society Reviews | DOI: `10.1039/C6CS00076B` | Metadata verified; claim relevance verified | BBB shuttle peptide biological framing | Background only; does not validate Permea predictions or delivery. | Ready for bibliography preparation |
| `REF_AUGUR` | Gu et al.; "Prediction of blood-brain barrier penetrating peptides based on data augmentation with Augur" | 2024 | BMC Biology | DOI: `10.1186/s12915-024-01883-4` | Metadata verified; claim relevance verified | Modern BBB peptide predictor using data augmentation / Borderline-SMOTE / imbalance handling | Comparator context only; do not claim Permea uses or outperforms this approach. | Ready for bibliography preparation |
| `REF_BRAINPEPPASS` | de Oliveira et al.; "BrainPepPass: A Framework Based on Supervised Dimensionality Reduction for Predicting Blood-Brain Barrier-Penetrating Peptides" | 2024 | Journal of Chemical Information and Modeling | DOI: `10.1021/acs.jcim.3c00951` | Metadata verified; claim relevance verified | Structure-aware / chemically richer BBB peptide predictor | Comparator context only; not evidence for current feature surface sufficiency beyond this benchmark. | Ready for bibliography preparation |
| `REF_DEEPB3P3` | Ma and Wolfinger; "A prediction model for blood-brain barrier penetrating peptides based on masked peptide transformers with dynamic routing" | 2023 | Briefings in Bioinformatics | DOI: `10.1093/bib/bbad399` | Metadata verified; claim relevance verified | Deep learning / transformer / capsule model comparator | Comparator context only; do not imply direct benchmark superiority. | Ready for bibliography preparation |
| `REF_ESM_BBB_PRED` | Naseem et al.; "ESM-BBB-Pred: a fine-tuned ESM 2.0 and deep neural networks for the identification of blood-brain barrier peptides" | 2025 | Briefings in Bioinformatics | DOI: `10.1093/bib/bbaf066` | Metadata verified; claim relevance verified | PLM/deep-learning comparator | Comparator context only; do not imply Permea performs PLM-style modeling. | Ready for bibliography preparation |
| `REF_B3BPFN` | Liu et al.; "Prediction of Blood-Brain Barrier-Penetrating Peptides Using B3BPFN" | 2026 | Frontiers in Molecular Biosciences | DOI: `10.3389/fmolb.2026.1858506` | Metadata verified; claim relevance verified | Very recent PLM/tabular foundation-model style comparator | Comparator context only; do not make public readiness or SOTA claims. | Ready for bibliography preparation |
| `REF_PERSEUCPP` | Bernardes-Loch et al.; "PerseuCPP: a machine learning strategy to predict cell-penetrating peptides and their uptake efficiency" | 2025 | Bioinformatics Advances | DOI: `10.1093/bioadv/vbaf213` | Metadata verified; claim relevance verified | Adjacent CPP benchmark / descriptor / independent validation reference | Adjacent CPP context only; not direct BBB validation. | Ready for bibliography preparation |
| `REF_CPP_COMPUTATIONAL_REVIEW` | "Biological Membrane-Penetrating Peptides: Computational Prediction and Applications" | 2022 | Frontiers in Cellular and Infection Microbiology | DOI: `10.3389/fcimb.2022.838259` | Metadata verified to supplied title/venue/year/DOI; claim relevance verified | Optional broader review for CPP/B3PP computational prediction and applications | Use for broad computational context only; no therapeutic or validation claim. | Ready for bibliography preparation if author metadata is acceptable for draft handling; otherwise defer from `references.bib`. |
| `REF_PEPBENCHMARK` | Zhang et al.; "PepBenchmark: A Standardized Benchmark for Peptide Machine Learning" | 2026 | ICLR 2026 poster / OpenReview | Not supplied | Partially verified / benchmark-standardization lead | Strong benchmark-standardization reference | Treat as partial; do not make precise k-mer/homology split claims unless exact PDF/supplement details are available in repo. | Deferred pending exact citation type and support details |

## Recommended use

### BBB and peptide-delivery background

- `REF_BBB_SHUTTLE_REVIEW`

### BBB peptide predictor related work

- `REF_AUGUR`
- `REF_BRAINPEPPASS`
- `REF_DEEPB3P3`
- `REF_ESM_BBB_PRED`
- `REF_B3BPFN`

### Adjacent CPP and benchmark context

- `REF_PERSEUCPP`
- `REF_CPP_COMPUTATIONAL_REVIEW`
- `REF_PEPBENCHMARK`

## What these references must not be used to claim

- Permea has biological or wet-lab validation.
- Current metrics demonstrate leakage-free or robust generalization.
- Permea is a state-of-the-art BBB peptide predictor.
- Feature importance proves biological mechanism.
- The dataset attribution, licensing, or redistribution status is resolved.
- Public preprint submission is ready.

## Remaining caveats

- `REF_PEPBENCHMARK` remains partial and should not be inserted into manuscript citations or `references.bib` until exact citation type and claim support are verified.
- `REF_CPP_COMPUTATIONAL_REVIEW` has title, venue, year, and DOI supplied, but no author metadata was supplied. Defer from `references.bib` if the draft bibliography policy requires author metadata.
- References with incomplete metadata should remain in planning docs rather than becoming final bibliography entries.
