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

## Before Implementation

- Measurement-layer audit: review every metric the experiment depends on (null models for bounded variables, denominators bounded away from zero, notation completeness, computability) before writing dependent code. A metric that fails the audit blocks implementation.
- Input-validity gate: when an experiment perturbs inputs (e.g. visual or text perturbations), confirm the perturbation survives the real preprocessing pipeline before running, so a null effect is not a preprocessing artifact.
- Record substitutions: any model, scale, or config substitution made during execution is recorded the same day in every planning artifact and the risk register. No silent substitution.

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
