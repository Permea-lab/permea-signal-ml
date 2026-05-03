# Permea Signal ML v0.1 Evidence Package

## Purpose

Permea Signal ML v0.1 is the first reproducible public computational evidence surface for `permea-signal-ml`. It defines the current benchmark-facing artifact package for BBB-oriented peptide and permeability-related signal modeling under the current repository contract.

## Scope

The scope of this package is narrow by design. It covers sequence-derived physicochemical features, baseline benchmark models, and benchmark-oriented outputs for BBB-oriented peptide / permeability-related signal analysis. It is intended to support transparent comparison, reproducible reruns, and candidate prioritization workflows before experimental validation.

## Included current-contract artifacts

The current-contract evidence surface consists of regenerated artifacts produced under the present repository structure, configs, and output conventions. These artifacts include benchmark metrics JSON files, prediction tables, ranking tables, summary tables, run manifests, and compact comparison tables for the current baseline reruns.

## Imported legacy artifacts

Imported legacy artifacts are retained for continuity, provenance recovery, and side-by-side comparison. They help document what existed before the current contract was defined, but they should not be treated as current benchmark evidence unless they have been regenerated under the current repository workflow.

## Regenerated artifact policy

Regenerated current-contract artifacts are the current public benchmark evidence surface. They should be preferred over imported legacy outputs when describing present repository behavior, benchmark results, or evidence status. Imported artifacts may remain visible for reference, but regenerated artifacts define the current benchmark contract.

## Current claim boundary

This package supports only initial computational evidence for candidate prioritization before experimental validation. It does not support claims of solved delivery, universal permeability prediction, validated biological performance, or experimental confirmation.

## Current evidence summary

The current evidence surface shows that baseline models trained on sequence-derived physicochemical features produce non-random benchmark signal on the present BBB-oriented dataset surface. The strongest current use of this package is bounded comparison across baseline methods and transparent generation of artifacts that can be inspected, rerun, and extended; it does not establish biological validation or delivery performance.

## Known limitations

Current evidence remains computational and benchmark-oriented. Dataset version, attribution, and licensing are still marked for confirmation in the current workflow. The repository does not yet establish biological truth, assay behavior, or transport performance outside the present benchmark surface.

## Why this package matters

This package matters because it turns `permea-signal-ml` from a generic ML scaffold into a reproducible public evidence package with explicit claim boundaries. It gives Permea a concrete, inspectable benchmark surface that preserves legacy continuity while making regenerated current-contract evidence the primary public reference point.

The broader Permea standard layer for taxonomy, claim discipline, benchmark contracts, and result artifacts is defined in the companion `permea-core` docs:

- [Delivery Taxonomy](https://github.com/Permea-lab/permea-core/blob/main/docs/DELIVERY-TAXONOMY.md)
- [Evidence Ladder](https://github.com/Permea-lab/permea-core/blob/main/docs/EVIDENCE-LADDER.md)
- [Benchmark Contract](https://github.com/Permea-lab/permea-core/blob/main/docs/BENCHMARK-CONTRACT.md)
- [Result Artifact Schema](https://github.com/Permea-lab/permea-core/blob/main/docs/RESULT-ARTIFACT-SCHEMA.md)
