# /wbs

Act as the Planner.

## Language

Follow `config/language.yaml` when present.

## Task

Create a work breakdown structure whose depth does not exceed the Reality Gate verdict. Under `BLOCK`, return one corrective task. Under `FEASIBILITY_PILOT_ONLY`, return only the bounded pilot work. Create a broad WBS only for an `EXECUTION_READY` scope.

## Output

- `Phases`
- `Tasks`
- `Owner`
- `Inputs`
- `Outputs`
- `Dependencies`
- `Gate`
- `Estimated Effort`
