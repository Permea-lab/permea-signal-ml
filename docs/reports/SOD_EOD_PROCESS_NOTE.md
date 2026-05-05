# SOD/EOD Process Note

## Purpose

This note defines the lightweight daily handoff process for Permea EOD and SOD documentation.

## EOD Process

At EOD, create or update:

- a dated EOD report summarizing completed work, evidence status, blockers, repo state, and next recommended tasks
- the next-day SOD handoff that can bootstrap a new ChatGPT/Codex conversation
- a dated ChatGPT SOD prompt file
- a dated Codex SOD prompt file

EOD reports should preserve claim boundaries. They should not claim public preprint readiness unless a final readiness audit and founder/manual approval have explicitly passed.

## SOD Process

At SOD, read the latest SOD handoff first. Then:

1. Confirm repository state.
2. Summarize previous completed work.
3. Present top priorities for the day.
4. Ask the user to choose a path if decisions are needed.
5. Generate a scoped Codex task prompt from the selected path.

## ChatGPT/Codex Behavior

- ChatGPT should propose daily priorities based on the latest SOD handoff and current repo state.
- Codex prompts should be generated from SOD priorities and should name allowed and forbidden file scopes.
- ChatGPT and Codex SOD prompt files should be stored next to the EOD/SOD handoff reports under `docs/reports/`.
- Public claims remain bounded until final readiness closure.
- Do not claim public preprint readiness unless final readiness audit, metadata/disclosure, dataset legal, references, supplement/export, and founder/manual approval blockers are closed.

## Claim-Boundary Reminder

The current package is computational evidence only. It does not claim leakage-free status, robust generalization, biological validation, wet-lab validation, therapeutic efficacy, or clinical efficacy.

## Current First SOD Task Pattern

After creating EOD/SOD reports, the next task should usually be:

Task 100 - Commit Permea 2026-05-04 EOD and 2026-05-05 SOD Reports
