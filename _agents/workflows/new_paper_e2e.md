# New Research Project Workflow

## Phase 1: Scope

Command: `/paper-scope`

Gate: Human approves problem statement, contributions, and non-goals.

## Phase 2: Source Ingestion

Command: `/pdf-ingest`

Gate: Sources are inspected and labeled.

## Phase 3: Literature Grounding

Command: `/lit-ground`

Gate: Closest prior work and baselines are identified.

## Phase 4: Mathematical Formalization

Command: `/math-formalize`

Gate: Contributions have definitions, objectives, and assumptions.

## Phase 5: Novelty Review

Command: `/astar-novelty`

Gate: Pass or conditional pass with fix plan.

## Phase 6: Execution Planning

Commands: `/risk-plan`, `/wbs`, `/code-exec-plan`

Gate: Human approves pilot.

## Phase 7: Implementation and Pilot

Commands: `/agent-brief`, `/phase-exec`

Gate: Pilot results are reviewed before full run.

## Phase 8: Review and Writing

Commands: `/reviewer-sim`, `/paper-review-fix`

Gate: Critical issues resolved and claims verified.
