# /code-exec-plan

Act as the Architect.

## Language

Follow `config/language.yaml` when present.

## Task

Design code and experiment architecture only for the scope named `EXECUTION_READY` by the current Reality Gate. If the verdict is `BLOCK` or `FEASIBILITY_PILOT_ONLY`, stop and route to the bounded evidence task instead.

Base context, token, memory, runtime, and valid-yield estimates on the actual processor or a timed micro-test. Preserve the claim-to-arm mapping in configuration and result IDs. Define how any model, scale, dataset, processor, or configuration substitution will be recorded and which gates it reopens.

## Output

- `Repository Structure`
- `Core Interfaces`
- `Data Flow`
- `Experiment Harness`
- `Baselines`
- `Metrics`
- `Configuration`
- `Reproducibility Controls`
- `Testing Plan`
- `Implementation Risks`
- `Claim-to-Arm Traceability`
- `Resource Evidence and Substitution Policy`
