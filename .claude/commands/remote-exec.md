# /remote-exec

Act as DevOps for remote or server execution.

## Language

Follow `config/language.yaml` when present.

## Task

Prepare a reproducible remote execution plan only for a named authorized scope. Confirm `EXECUTION_READY` before implementation and `FULL_RUN_READY` before a full run.

## Output

- `Environment`
- `Dependencies`
- `Data Transfer`
- `Run Commands`
- `Resource Estimate`
- `Monitoring`
- `Artifact Sync`
- `Rollback Plan`
