# Experiments Reference

## Rule

Pilot before full run.

## Required Before Implementation

- Research question.
- Formalized inputs and outputs.
- Dataset and version.
- Baselines.
- Metrics.
- Random seeds.
- Environment.
- Artifact schema.
- Stop conditions.

## Pilot Criteria

A pilot should confirm:

- Code runs end to end.
- Data loading works.
- Baseline is reproducible.
- Metric is computed correctly.
- Result artifact is saved.
- Runtime and cost are acceptable.

## Result Schema

```json
{
  "run_id": "string",
  "hypothesis": "string",
  "dataset": "string",
  "baseline": "string",
  "method": "string",
  "metrics": {},
  "seed": 42,
  "environment": {},
  "notes": "string"
}
```

## Stop Conditions

- Required data is missing.
- Baseline cannot be reproduced.
- Metrics do not measure the claim.
- Runtime or cost exceeds approved budget.
- Results contradict the hypothesis and require redesign.
