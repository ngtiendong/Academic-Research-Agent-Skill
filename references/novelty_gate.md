# Novelty Gate Reference

## Purpose

Stop weak research ideas before they consume implementation and writing time.

## Fail Conditions

- The idea is only an existing method applied to a new domain.
- The contribution depends on vague language.
- The closest prior work is missing.
- The hypothesis is not falsifiable.
- The evaluation cannot distinguish the method from existing work.
- The baseline is weak or convenient.
- A headline claim or claim gate has no matching experiment arm or ID.

## Pass Conditions

- Clear delta over closest prior work.
- Measurable hypothesis.
- Explicit mechanism or explanation for why the method should work.
- Appropriate baselines.
- Known failure modes.
- Every headline novelty claim maps to a falsifying test, proof obligation, experiment arm, or result ID and a real kill/drop condition.

If direct competitors have not been inspected, use `NOT_ASSESSED`. Do not use `REVISE` as a synonym for missing evidence. A novelty pass authorizes the Reality Gate, not implementation.

## Output Template

```text
Novelty Verdict: NOT_ASSESSED | PASS | REVISE | FAIL
Closest Prior Work:
Residual Delta:
Falsifying Test, Proof Obligation, or Arm/Result ID:
Kill/Drop Condition:
Weakness:
Required Strengthening:
Researcher Decision:
```
