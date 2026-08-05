# Agent Operations Center

This folder defines how the research agents operate.

```text
_agents/
├── configs/      # Role contracts for each agent
├── rules/        # Shared research quality rules
└── workflows/    # End-to-end procedures
```

## Roles

| Agent | Responsibility |
|---|---|
| Orchestrator | State, naming, routing, Reality Gates, escalation |
| Strategist | Scope, literature, minimal formalization, experimental-unit definition |
| Critic | Novelty, Reality Gate challenge, review, claim verification |
| Planner | Bounded falsifiers first; risks, milestones, and WBS after clearance |
| Architect | Approved code and experiment architecture |
| Executor | Evidence recovery, implementation, smoke tests, feasibility pilots, and runs |
| DevOps | Environment, remote runs, artifact sync |

## Rule Priority

1. Do not fabricate sources or results.
2. Human approval gates override agent momentum.
3. Evidence must precede claims.
4. Reality Gate before broad execution planning.
5. Claim-eligible feasibility pilot before full run.
6. Keep outputs traceable to artifacts.
