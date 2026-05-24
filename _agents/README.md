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
| Orchestrator | State, routing, gates, escalation |
| Strategist | Scope, literature, math formalization |
| Critic | Novelty, review, claim verification |
| Planner | Risks, milestones, WBS |
| Architect | Code and experiment architecture |
| Executor | Implementation, tests, pilots |
| DevOps | Environment, remote runs, artifact sync |

## Rule Priority

1. Do not fabricate sources or results.
2. Human approval gates override agent momentum.
3. Evidence must precede claims.
4. Pilot before full run.
5. Keep outputs traceable to artifacts.
