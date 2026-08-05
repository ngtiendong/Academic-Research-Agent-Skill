# Local to Server Workflow

## Goal

Move approved code from local development to a remote machine for reproducible experiments.

## Steps

1. Confirm the named scope is `EXECUTION_READY` and the code plan is approved.
2. Document environment and dependency versions.
3. Prepare data paths and artifact output paths.
4. Run a small engineering smoke test and record that it is not scientific evidence.
5. Launch the approved claim-eligible feasibility pilot or run.
6. Sync artifacts back.
7. Review pilot evidence and require `FULL_RUN_READY` plus human approval before a full run.

## Required Report

- Commit or file state.
- Environment.
- Command used.
- Runtime.
- Resource usage.
- Output path.
- Failure logs, if any.
