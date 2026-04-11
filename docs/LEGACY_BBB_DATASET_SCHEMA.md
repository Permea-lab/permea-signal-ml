# Legacy BBB Dataset Schema

## Title

Imported Legacy BBB Processed Dataset Schema

## File inspected

- `data/processed/legacy_bbb_dataset_with_features.csv`

## Row count

- `2959`

## Columns

- `sequence`
- `label`
- `length`
- `charge`
- `gravy`
- `pI`
- `aromaticity`

## Missing values summary

- `sequence`: `0`
- `label`: `0`
- `length`: `0`
- `charge`: `0`
- `gravy`: `0`
- `pI`: `0`
- `aromaticity`: `0`

## Sequence identifier status

- `sequence_id` column not present

## Source column status

- `source` column not present

## Notes for rerun readiness

- the imported legacy processed dataset is usable as a source onboarding artifact
- it is not rerun-ready as-is because `sequence_id` is missing
- it is not rerun-ready as-is because `source` is missing
- feature columns already match the recovered legacy feature surface
- a derived rerun-ready dataset is required for the current repository pipeline
