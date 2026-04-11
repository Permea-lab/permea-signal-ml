# Biocore Migration Checklist

## Files to inspect

- [ ] Inspect `/Users/albertkim/02_PROJECTS/16_permea_bbb_analysis`
- [ ] Confirm whether `dataset_with_features.csv` exists
- [ ] Confirm whether `rf_feature_importance.png` exists
- [ ] Confirm whether `candidate_ranking.png` exists
- [ ] Inspect legacy notebooks
- [ ] Inspect legacy metrics exports if present
- [ ] Inspect legacy predictions or ranking tables if present

## Files to import

- [ ] Import usable figure artifacts into `figures/`
- [ ] Import usable metrics files into `results/metrics/` if provenance is acceptable
- [ ] Import usable prediction files into `results/predictions/` if provenance is acceptable
- [ ] Import usable ranking tables into `results/tables/` if provenance is acceptable
- [ ] Import processed dataset artifacts into `data/processed/` only after schema and provenance review

## Files to regenerate

- [ ] Regenerate manifest files in current contract format
- [ ] Regenerate summary CSV outputs in current contract format
- [ ] Regenerate metrics JSON if legacy format is incomplete
- [ ] Regenerate predictions CSV if fold structure or score fields are missing
- [ ] Regenerate ranking CSV if only figure outputs exist

## Provenance to verify

- [ ] Dataset name
- [ ] Dataset version
- [ ] Source path
- [ ] Label definition
- [ ] Split policy
- [ ] Random seed
- [ ] Model configuration
- [ ] Feature configuration
- [ ] Licensing status
- [ ] Attribution requirements

## Naming updates needed

- [ ] Assign stable `run_id` values
- [ ] Rename imported metrics files to current convention
- [ ] Rename imported predictions files to current convention
- [ ] Rename imported ranking files to current convention
- [ ] Rename imported figures to current convention where appropriate

## Final review before commit

- [ ] Imported artifacts marked clearly as imported if not rerun
- [ ] Regenerated artifacts separated from imported artifacts clearly
- [ ] Provenance gaps documented explicitly
- [ ] No unsupported scientific claims introduced
- [ ] Benchmark contract alignment checked
