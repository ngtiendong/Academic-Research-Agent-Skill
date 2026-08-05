# Experiments Reference

## Core rule

Run the cheapest decisive falsifier before broad implementation. A technical smoke, a scientific feasibility pilot, and a full run are different stages.

## Before any experiment code

- Resolve the exact claim and falsifier.
- Pass or bound all Reality Gate certificates relevant to the requested stage.
- Define the experimental unit, cluster unit, inclusion/exclusion rule, and valid-yield funnel.
- Freeze formalized inputs, outputs, metrics, controls, and missingness behavior.
- Record dataset/model/processor versions and access.
- Audit every metric for computability, valid null/control, denominator, notation, and uncertainty.
- Verify that any input treatment survives the real preprocessing path and preserves the task endpoint.
- Define seed/determinism, environment, artifact schema, maximum cost, retries, and stop conditions.
- Record any model, scale, data, or config substitution on the same day.

## Engineering smoke

An engineering smoke may confirm:

- dependencies and access work;
- data/model loading completes;
- one input runs end to end;
- output fields are emitted;
- runtime, memory, and token/page packing are observed.

Label this `engineering_smoke`. It does not prove the dataset can test the claim, the phenomenon exists, or the paper is feasible.

## Scientific feasibility pilot

A claim-eligible pilot should confirm:

- the real experimental unit and provenance are valid;
- the model has the prerequisite capability;
- treatment, control, and counterfactual preserve the intended endpoint;
- the metric is hand-checked on actual output;
- the primary contrast can falsify the claim;
- the raw/result/report artifact path is complete;
- valid yield, runtime, human time, and compute are observed;
- the decisive signal meets a frozen feasibility rule or supports a real stop decision.

Use the smallest sample that can answer the feasibility question. A common range is 10–50, not a universal rule.

## Full run

Require:

- `FULL_RUN_READY` verdict;
- researcher approval;
- frozen primary contrast and sample-size/precision logic;
- pre-registered controls, exclusions, and multiplicity handling;
- complete provenance and rerun path;
- observed cost based on valid yield, not requested rows.

## Minimum result schema

```json
{
  "run_id": "string",
  "run_type": "engineering_smoke | feasibility_pilot | full | stop_debug",
  "claim_id": "string",
  "hypothesis": "string",
  "dataset": {"id": "string", "version": "string"},
  "model": {"id": "string", "revision": "string", "processor_revision": "string"},
  "arm_id": "string",
  "experimental_unit_id": "string",
  "cluster_id": "string",
  "input_provenance": {},
  "raw_output": {},
  "metrics": {},
  "validity_flags": {},
  "exclusion_reason": null,
  "seed": 42,
  "environment": {},
  "runtime": {},
  "code_commit": "string",
  "notes": "string"
}
```

## Artifact contract

For every pilot/full/stop-debug run, retain:

- raw machine output;
- full config and environment;
- stdout/stderr log;
- human-readable run report with the same stem;
- state/decision impact recorded after human review.

## Stop conditions

- required data or provenance is missing;
- the prerequisite capability is absent;
- the treatment changes the truth condition or fails preprocessing;
- the baseline/counterfactual cannot be reproduced;
- the metric does not measure the claim;
- matched controls explain the effect;
- valid yield or cost exceeds the approved bound;
- results trigger the pre-registered kill condition;
- a redesign would change the research question or novelty nucleus.

Report null and negative results honestly. Do not auto-pivot.
