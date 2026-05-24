# Competitive Analysis

This document summarizes useful patterns from public research-agent repositories.

## AutoResearchClaw

Repository: https://github.com/aiming-lab/AutoResearchClaw

What it does well:

- Strong slogan: "Chat an Idea. Get a Paper."
- Visual first impression: logo, framework image, badges, generated paper showcase.
- Clear one-command quick start.
- Strong feature framing: pipeline stages, co-pilot mode, claim verification, cost guardrails, artifact outputs.
- Multilingual README links.
- Public changelog that signals active development.

What to learn:

- Lead with outcome, not architecture.
- Show artifacts early: generated paper, review report, citation verification, experiment folder.
- Add a short demo path before deep details.
- Make human-in-the-loop a product feature, not a caveat.

Risk:

- Claims are very strong. If your repo does not ship runnable automation, do not market it as equivalent.

## Agent Laboratory

Repository: https://github.com/SamuelSchmidgall/AgentLaboratory

What it does well:

- Clear academic positioning and paper citation.
- Three-phase framing: literature review, experimentation, report writing.
- Multilingual README.
- Simple run command from a YAML config.

What to learn:

- Researchers trust systems more when there is a paper, architecture diagram, and reproducible example.
- Language support should be explicit in config.

## GPT Researcher

Repository: https://github.com/assafelovic/gpt-researcher

What it does well:

- Clear pain points: outdated LLMs, hallucinations, shallow sources, token limits.
- Multiple usage modes: server, package, Docker, MCP.
- Architecture explanation with planner and execution agents.
- Frontend and documentation.

What to learn:

- Give several entry points for different users.
- State the problem in user language before listing features.

## STORM

Repository: https://github.com/stanford-oval/storm

What it does well:

- Strong research identity from Stanford.
- Explains the core insight: better question asking before writing.
- Human collaboration via Co-STORM.
- Mind map and perspective-guided question asking are memorable concepts.

What to learn:

- A repo gets stronger when it names one distinctive mechanism.
- Visualizing the user journey matters.

## PaperQA

Repository: https://github.com/Future-House/paper-qa

What it does well:

- Tight focus: high-accuracy RAG over scientific documents with citations.
- Strong credibility through evaluation claims and package maturity.
- Clear scientific-document niche.

What to learn:

- Narrow, reliable tools often earn more trust than broad autonomous claims.

## Differentiation for Research Agent Skill

The best positioning is not "another autonomous research agent." It should be:

> A human-guided research agent for Master and PhD students in CS, AI, math, engineering, and related technical fields.

Strong differentiators:

- A* novelty gate before drafting.
- Math formalization before implementation.
- Gate-based human approval.
- Claim verification and traceability.
- Skill-first template that can be adapted to general AI assistants and local LLM research agents.
- Student-friendly collaboration model: the researcher learns from each gate instead of receiving opaque final text.

Weak spots to fix before public launch:

- No runnable CLI yet.
- No screenshots or real artifact showcase yet.
- No benchmark or user study yet.
- No tests because this is currently a skill/workflow template, not a software package.

Recommended public claim:

> Research Agent Skill helps researchers collaborate with agents to produce better-scoped, better-grounded, and more reviewable research artifacts.

Claims to avoid:

- "Fully autonomous researcher."
- "One prompt to accepted paper."
- "Guaranteed high-quality research."
- "No human review required."
