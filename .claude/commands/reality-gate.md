# /reality-gate

Act as a skeptical research auditor. Read `references/reality_gate.md` before deciding.

## Language

Follow `config/language.yaml` when present.

## Task

Determine what work the inspected evidence actually authorizes. Audit scientific reality, engineering reality, and paper viability separately.

## Required checks

- Phenomenon.
- Experimental unit.
- Measurement.
- Treatment/intervention validity.
- Access and preprocessing.
- Closest-competitor delta.
- Resource envelope and observed valid yield.
- Joint claim dependencies and real stop/drop branches.

Use only `pass`, `fail`, `unknown`, or justified `not_applicable` for each certificate. A `pass` requires an evidence path. An `unknown` requires one bounded test with an owner, maximum cost, acceptance criterion, and stop condition.

## Output

- `Verdict`: `BLOCK`, `FEASIBILITY_PILOT_ONLY`, `EXECUTION_READY`, or `FULL_RUN_READY`.
- `Authorized Scope`.
- `Prohibited Work`.
- `Fatal Assumption First`.
- `Certificate Table` with evidence paths.
- `Claim Survival Graph`.
- `Next Test` with owner, maximum cost, acceptance, and stop.
- `Researcher Decision`.
