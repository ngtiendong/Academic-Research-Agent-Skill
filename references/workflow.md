# Workflow Reference

## Collaboration pattern

Every stage must answer:

- What does the researcher decide?
- What does the agent prepare?
- What inspected evidence supports advancement?
- What stops, drops, or narrows the work?
- Which deeper artifacts remain prohibited?

## Lifecycle

| Stage | Human role | Agent role | Default artifact |
|---|---|---|---|
| State and naming | Confirm project/paper identity | Resolve local naming profile and current gate | `01_Project_State.md` |
| Candidate scope | Approve question, non-goals, and kill conditions | Draft a falsifiable candidate contract | `02_Scope.md` |
| Source ingestion | Provide sources and context | Inspect and label sources | `18_Source_Notes_Index.md` |
| Literature grounding | Judge relevance | Pressure-test closest prior work | `05_Lit_Grounding.md` |
| Provisional formalization | Validate meaning | Define the minimum object, measurement, and assumptions needed for falsification | `06_Math_Formalization.md` |
| Novelty gate | Continue, revise, or fail | Establish the exact residual over competitors | novelty report |
| Reality Gate | Approve only the bounded next test | Audit the actual unit, measurement, intervention, access, yield, and dependencies | `20_Reality_Gate.md` |
| Experimental-unit audit | Decide pass, replace, narrow, or stop | Recover and inspect real inputs/provenance | `22_Experimental_Unit_Audit_Plan.md` plus evidence package |
| Feasibility pilot | Approve the frozen contrast | Run the smallest claim-eligible falsifier | `23_Feasibility_Pilot_Protocol.md` plus result package |
| Claim freeze | Approve surviving claims | Update scope/formalization and drop failed branches | state, scope, and claim ledger |
| Execution planning | Approve implementation scope | Build risk, work, and code plans only for surviving claims | `10_Risk_Plan.md`, `11_WorkBreakdown.md`, `12_Code_Execution_Plan.md` |
| Implementation/full run | Approve brief/full scale | Execute only the authorized stage | code, raw outputs, logs, run report |
| Review and writing | Choose fixes and wording | Simulate reviewers and draft bounded claims | review package and draft |
| Claim verification | Approve final claims | Trace every claim to a source or result | verification report |

Project-local naming rules may insert a paper identifier or use established slot variants. Preserve the logical artifact type and never repurpose a reserved slot.

## Artifact materialization by evidence stage

| Evidence stage | Create/update now | Keep deferred unless explicitly requested |
|---|---|---|
| Raw idea; sources uninspected | state, candidate scope; source index only for identifiable sources | literature grounding, formalization, novelty report, Reality Gate, audit/pilot plan, WBS, code plan, draft |
| Sources inspected; candidate still unstable | source notes/matrix, literature grounding, scope revision | Reality Gate and execution artifacts |
| Residual and minimum measurement defined | provisional formalization and novelty decision | audit/pilot artifacts until a real unit/access target is named |
| Feasibility-sensitive request or named unit/access path | Reality Gate; one bounded audit plan if required | broad planning and implementation under `BLOCK` |
| `FEASIBILITY_PILOT_ONLY` | feasibility protocol and minimal pilot support | broad WBS, architecture, full draft, full run |
| `EXECUTION_READY` | risk/WBS/code plan for the named scope | full run until `FULL_RUN_READY` |

A future artifact may be mentioned in a roadmap without being created. Do not confuse a complete artifact tree with research progress.

## Gate sequence

### Scope Gate

Pass when the research question, non-goals, target audience, required evidence, falsifier, and kill conditions are clear.

### Novelty Gate

Use `PASS`, `REVISE`, or `FAIL`. Pass only when a measurable residual over closest prior work exists and the work is not only method A applied to domain B.

If sources or competitors have not been inspected, the gate is `NOT_ASSESSED`, not `REVISE`.

### Reality Gate

Use `BLOCK`, `FEASIBILITY_PILOT_ONLY`, `EXECUTION_READY`, or `FULL_RUN_READY`. Read [reality_gate.md](reality_gate.md). Planning depth must not exceed the verdict.

For a raw idea without a named experimental unit or access path, record `NOT_ASSESSED` and no execution authorization. Create a formal Reality Gate artifact only when the decision is feasibility-sensitive, after a reframe, or when the user explicitly requests the audit.

### Feasibility Pilot Gate

Pass only when a small real run validates the experimental unit, preprocessing, baseline/counterfactual, measurement, controls, result artifacts, valid yield, and a decisive signal. Code running alone is an engineering smoke pass.

### Full-Run Gate

Require a claim-eligible pilot, frozen primary contrast and sample logic, complete provenance, bounded cost, and explicit human approval.

### Claim Gate

Pass when every factual claim links to an inspected source, formal artifact, or result. Narrow, label, or remove unsupported claims.

## Reframe rule

When the novelty nucleus, experimental unit, central estimand, or headline claim changes:

1. create or use an isolated reframe workspace when history must be preserved;
2. return to scope, evidence, formalization, novelty, and Reality Gate;
3. invalidate downstream authorization from the old scope;
4. do not reuse old WBS/code plans as evidence of readiness;
5. record the human decision before promoting the reframe.
