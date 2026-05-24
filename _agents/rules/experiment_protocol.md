# Experiment Protocol Rule

Experiments must be reproducible, falsifiable, and traceable.

## Required

- Baselines.
- Dataset version.
- Metrics.
- Random seeds.
- Environment.
- Pilot run before full run.
- Structured result artifact.
- Failure notes.

## Recommended Result Schema

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
