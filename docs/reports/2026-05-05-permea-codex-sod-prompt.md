# Permea Codex SOD Prompt - 2026-05-05

Copy-paste this prompt into a new Codex conversation to begin a read-only SOD context restore.

```text
Task: Permea SOD Context Restore - 2026-05-05

You are working in the Permea project.

Repository target:
- Primary repo: permea-signal-ml
- Local path: /Users/albertkim/02_PROJECTS/18_Permea-lab/permea-signal-ml
- Remote: https://github.com/Permea-lab/permea-signal-ml.git
- Branch: master

Read:
- docs/reports/2026-05-04-permea-eod-report.md
- docs/reports/2026-05-05-permea-sod-handoff.md
- docs/reports/SOD_EOD_PROCESS_NOTE.md

Run:
- pwd
- git status --short --branch
- git log --oneline -10
- git remote -v

Do not modify files.
Do not stage files.
Do not commit.
Do not push.
Do not rerun models.
Do not rerun leakage audit.
Do not run new split generation.
Do not modify manuscript scientific content.
Do not modify references.bib.
Do not modify data, result, or figure artifacts.

Summarize:
- current repo state
- latest commit
- previous session work
- current blockers
- recommended next tasks

Maintain claim discipline:
- public bioRxiv remains Hold / not submission-ready
- do not claim leakage-free status
- do not claim robust generalization
- do not claim biological or wet-lab validation
- do not imply external expert review or peer review
```
