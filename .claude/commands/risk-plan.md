# /risk-plan

Act as the Planner.

## Language

Follow `config/language.yaml` when present.

## Task

Create a research execution risk plan only for the scope named `EXECUTION_READY`. Under `BLOCK` or `FEASIBILITY_PILOT_ONLY`, return only the bounded corrective/pilot risk and stop conditions.

## Include

- Feasibility risks.
- Compute and data risks.
- Baseline risks.
- Evaluation risks.
- Writing and claim risks.
- Timeline risks.

## Output

- `Risk Register`
- `Mitigation`
- `Contingency`
- `Stop Conditions`
- `Scientific Feasibility-Pilot Criteria`
- `Full Run Approval Gate`
