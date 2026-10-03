# Experiment Protocol Rule

Experiments must be reproducible, falsifiable, and traceable.

## Required

- Baselines.
- Dataset version.
- Metrics.
- Random seeds.
- Environment.
- A named Reality Gate verdict before implementation planning.
- Scientific feasibility pilot before full run.
- Structured result artifact.
- Failure notes.

## Before Implementation

- Reality Gate: inspect the actual experimental unit, access path, measurement, intervention, competitor delta, valid yield, and joint dependencies. Under `BLOCK`, perform only corrective evidence work; under `FEASIBILITY_PILOT_ONLY`, build only the bounded falsifier.
- Measurement-layer audit: review every metric the experiment depends on (null models for bounded variables, denominators bounded away from zero, notation completeness, computability) before writing dependent code. A metric that fails the audit blocks implementation.
- Input-validity gate: when an experiment perturbs inputs (e.g. visual or text perturbations), confirm the perturbation survives the real preprocessing pipeline before running, so a null effect is not a preprocessing artifact.
- Capability gate: before claiming that an intervention disrupts capability X, demonstrate X under a clean or untreated paired control with uncertainty.
- Resource reality: estimate context, tokens, memory, runtime, and cost from the actual processor or a timed micro-test, and budget from valid yield rather than requested rows.
- Record substitutions: any model, scale, dataset, processor, or configuration substitution made during execution is recorded the same day in the state, relevant plans, and risk register. Reopen affected gates; no silent substitution.
- Interpretation discipline: establish within-model or within-condition validity before attributing pooled differences to architecture, family, or mechanism labels.

## Recommended Result Schema

```json
{
  "run_id": "string",
  "code_commit": "string",
  "hypothesis": "string",
  "dataset_name_and_version": "string",
  "model_id_and_revision": "string",
  "experimental_unit_id": "string",
  "baseline": "string",
  "method": "string",
  "metrics": {},
  "raw_output_path": "string",
  "validity_flags": {},
  "exclusion_reason": null,
  "seed": 42,
  "environment": {},
  "runtime_and_peak_resource": {},
  "substitutions": [],
  "claim_status": "hypothesis | supported | partially-supported | contradicted | unverified | dropped",
  "notes": "string"
}
```
