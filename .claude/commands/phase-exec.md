# /phase-exec

Act as the Executor.

## Language

Follow `config/language.yaml` when present.

## Task

Execute a phase from a provided `agent-brief`.

## Rules

- Read the brief completely before editing.
- Keep changes scoped.
- Do not overwrite unrelated user work.
- Run the smallest meaningful checks.
- Stop when a stop condition is met.

## Output

- `Completed Work`
- `Changed Files`
- `Checks Run`
- `Results`
- `Blockers`
- `Next Step`
