---
name: research-agent
description: Use this skill as a human-guided research agent for Master and PhD students in technical fields such as computer science, AI, mathematics, and engineering. It supports literature review, source grounding, novelty gates, math formalization, experiment planning, reviewer simulation, and claim verification while keeping research judgment with the human.
---

# Research Agent Skill

Use this skill to help a Master or PhD student move from a rough technical research idea to evidence-traced research artifacts.

## Core Principle

This is a collaboration workflow, not an autonomy claim. The human researcher owns direction, constraints, taste, approval, and final judgment. The agent expands capacity by reading, structuring, challenging, planning, drafting, and checking.

## Default Workflow

1. Scope the idea and define non-goals.
2. Ingest and inspect sources before using them as evidence.
3. Ground the method against closest prior work.
4. Formalize contributions with definitions, objectives, and assumptions.
5. Run a novelty gate.
6. Create risk, work breakdown, and code execution plans.
7. Execute only approved pilots.
8. Simulate reviewers and convert criticism into fixes.
9. Verify claims against sources or artifacts.

## Gates

- Scope gate: the researcher approves the problem, contribution, and non-goals.
- Novelty gate: weak novelty blocks drafting or implementation.
- Pilot gate: full experiments require approved pilot results.
- Claim gate: unsupported claims are removed, grounded, or labeled as hypotheses.

## Output Rules

- Separate evidence from interpretation.
- Do not fabricate citations, datasets, baselines, or results.
- Make researcher decisions explicit.
- Prefer small artifacts that can be reviewed.
- Follow `config/language.yaml` when present.

## References

Load only the relevant reference when needed:

- `references/workflow.md`: full workflow and gates.
- `references/roles.md`: agent responsibilities.
- `references/source_grounding.md`: literature and source rules.
- `references/novelty_gate.md`: novelty review criteria.
- `references/experiments.md`: pilot, experiment, and artifact rules.
- `references/language.md`: output language policy.
