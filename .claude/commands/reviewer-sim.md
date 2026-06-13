# /reviewer-sim

Act as three reviewers: supportive, skeptical, and methods-focused.

## Language

Follow `config/language.yaml` when present.

## Task

Review a scope, draft, experiment plan, or result package.

## Procedure

1. Check novelty, clarity, evidence, methodology, experiments, and writing.
2. Review the measurement layer: null models for bounded variables (independence null, not additive), notation completeness, operational definitions of headline terms, and claim-arm coverage (every claim gate maps to an experiment arm or ID).
3. Separate critical issues from minor issues.
4. Give concrete fixes, not generic advice.
5. Identify claims that need source or artifact support.

## Output

- `Overall Score` from 1 to 10
- `Critical Issues`
- `Minor Issues`
- `Missing Evidence`
- `Recommended Fix Plan`
- `Acceptability After Fixes`
