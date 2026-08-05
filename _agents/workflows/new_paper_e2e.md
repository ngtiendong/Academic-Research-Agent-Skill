# New Research Project Workflow

## Phase 0: State and naming

Read project-local instructions, resolve the artifact naming profile, and record the current decision gate.

Gate: The researcher confirms the paper identity and requested decision.

## Phase 1: Candidate scope

Command: `/paper-scope`

Define the research question, non-goals, required evidence, cheapest falsifier, and kill conditions.

Gate: The researcher approves a falsifiable candidate, not a promise to build it.

## Phase 2: Source ingestion and grounding

Commands: `/pdf-ingest`, `/lit-ground`

Inspect sources, identify direct competitors, and separate inspected evidence from inference.

Gate: The residual problem and required baselines are explicit.

## Phase 3: Minimal formalization and novelty

Commands: `/math-formalize`, `/astar-novelty`

Formalize only what is needed to define the object, measurement, contrast, and residual novelty.

Gate: Novelty is `PASS`, `REVISE`, or `FAIL`. A pass does not imply feasibility.

## Phase 4: Research Reality Gate

Command: `/reality-gate`

Audit the real experimental unit, measurement, intervention, access/preprocessing path, competitor delta, valid yield/resource envelope, and joint claim dependencies.

Gate: `BLOCK`, `FEASIBILITY_PILOT_ONLY`, `EXECUTION_READY`, or `FULL_RUN_READY` with evidence paths and prohibited work.

## Phase 5: Bounded evidence recovery or feasibility pilot

Under `BLOCK`, perform only corrective evidence work. Under `FEASIBILITY_PILOT_ONLY`, run the smallest claim-eligible falsifier on real inputs. Do not prepare a broad implementation plan.

Gate: The researcher chooses stop, replace, narrow, reframe, or promote based on frozen criteria.

## Phase 6: Claim freeze and execution planning

Commands: `/risk-plan`, `/wbs`, `/code-exec-plan`

Drop failed branches, freeze the primary contrast and surviving claims, then plan only the authorized implementation scope.

Gate: `EXECUTION_READY` plus human approval before implementation; `FULL_RUN_READY` before scale-up.

## Phase 7: Implementation and full run

Commands: `/agent-brief`, `/phase-exec`

Execute the authorized brief with raw outputs, provenance, timing, valid-yield accounting, and stop conditions.

Gate: Run artifacts support the named claim and stay within the approved cost envelope.

## Phase 8: Review, writing, and claim closure

Commands: `/reviewer-sim`, `/paper-review-fix`, `/claim-verify`

Gate: Critical issues are resolved and every retained claim is traced to inspected evidence. Unsupported claims are narrowed, labeled, or removed.

## Reframe trigger

If the novelty nucleus, experimental unit, central estimand, or headline claim changes, invalidate downstream authorization and return to scope, evidence, formalization, novelty, and Reality Gate.
