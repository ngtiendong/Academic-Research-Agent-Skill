# /agent-brief

Act as the Orchestrator creating a self-contained brief for an Executor.

## Language

Follow `config/language.yaml` when present.

## Task

Write a brief that lets another agent complete one reality-authorized phase without reading prior conversation. Include the current verdict and stop immediately if the requested phase exceeds it.

## Output

- `Mission`
- `Context`
- `Inputs`
- `Files to Read`
- `Files to Modify`
- `Non-Goals`
- `Reality Verdict and Authorized Scope`
- `Prohibited Work`
- `Expected Outputs`
- `Tests or Checks`
- `Stop Conditions`
- `Report Format`
