# P-REPRO Public-Safe Reproducibility Packet

Status: merged public reproducibility packet on the public repository branch; not a tagged release, formal publication, dataset release, or manuscript release.

This packet gives a reviewer a public-safe map of reproducible aggregate artifacts derived from prior public-safe packet review. It is intended to make the public reproducibility surface inspectable without exposing row-level or private execution material.

This packet can reproduce or verify:

- public aggregate artifact existence
- checksum and shape summaries for public aggregate files
- public validation commands and expected summaries
- public-safe figure manifests and exported figure files
- claim boundaries and public/private release boundaries

This packet cannot reproduce or expose:

- row-level dataset records
- raw sequences
- row-level labels
- row-level predictions
- embeddings or representation matrices
- split internals, split manifests, or group assignments
- new model outputs
- calibration recomputation
- threshold sweep recomputation
- wet-lab validation
- independent validation

Packet files:

- [public_artifact_manifest.md](public_artifact_manifest.md)
- [validation_commands.md](validation_commands.md)
- [expected_output_summary.md](expected_output_summary.md)
- [aggregate_result_checksum_shape_summary.md](aggregate_result_checksum_shape_summary.md)
- [figure_manifest_summary.md](figure_manifest_summary.md)
- [claim_boundary_checklist.md](claim_boundary_checklist.md)
- [public_private_boundary_checklist.md](public_private_boundary_checklist.md)
- [reviewer_walkthrough.md](reviewer_walkthrough.md)
- [reproducibility_packet_manifest.json](reproducibility_packet_manifest.json)
- [correction_manifest.json](correction_manifest.json)
