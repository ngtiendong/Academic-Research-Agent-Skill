# Workflow Reference

## Collaboration Pattern

Every stage should answer:

- What does the researcher decide?
- What does the agent prepare?
- What evidence supports the current artifact?
- What would make this stage fail?

## Stages

| Stage | Human role | Agent role | Artifact |
|---|---|---|---|
| Idea | State intent, constraints, taste | Clarify and structure | Topic brief |
| Scope | Approve question and non-goals | Draft contribution options | `02_Scope.md` |
| Source ingestion | Provide papers, links, context | Inspect and summarize sources | Source inventory |
| Literature grounding | Judge relevance | Compare against prior work | `05_Lit_Grounding.md` |
| Math formalization | Validate meaning | Define objects and objectives | `06_Math_Formalization.md` |
| Novelty gate | Decide whether to continue | Challenge weak novelty | Novelty report |
| Planning | Approve pilot | Build risk and work plan | `10_Risk_Plan.md` |
| Implementation | Approve brief | Implement scoped phase | Code and run report |
| Review | Choose fixes | Simulate reviewers | Review fix plan |
| Claim verification | Approve final claims | Trace claims to evidence | Verification report |

## Gates

### Scope Gate

Pass when the research question, contribution, non-goals, target audience, and required evidence are clear.

### Novelty Gate

Pass when the contribution has a measurable delta over closest prior work and is not only "method A applied to domain B."

### Pilot Gate

Pass when a small run confirms the environment, data, baseline, metric, and artifact path.

### Claim Gate

Pass when every factual claim links to an inspected source, formal artifact, or experiment result.
