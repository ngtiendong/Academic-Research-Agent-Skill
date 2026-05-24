# Getting Started

Research Agent Skill is a repository-hosted research agent workflow for Master and PhD students in technical fields such as computer science, AI, mathematics, and engineering. It gives the assistant a disciplined research process while keeping the researcher in control.

## 1. Install

```bash
git clone <your-repo-url>
cd Academic-Research-Agent-Skill
cp config/language.example.yaml config/language.yaml
```

Use it with an AI assistant that can read repository instructions, such as Claude, ChatGPT, Gemini, local LLM agents, or similar tools.

## 2. Start With a Topic Brief

```bash
cp examples/topic_brief.md my_topic.md
```

Fill in:

- research topic,
- target audience or venue,
- known papers,
- constraints,
- preferred output language,
- what you want to learn or decide.

## 3. Ask the Agent to Use the Skill

```text
Read SKILL.md, CLAUDE.md, and my_topic.md.
Use the Research Agent Skill to help me scope this research idea.
Do not skip human decision gates.
```

## 4. Recommended First Run

```text
/paper-scope
/pdf-ingest
/lit-ground
/math-formalize
/astar-novelty
/risk-plan
/code-exec-plan
/reviewer-sim
```

## 5. What You Should Expect

The agent should not simply produce a polished paper. It should produce reviewable artifacts:

- a scoped problem,
- contribution options,
- literature grounding,
- formal definitions,
- novelty critique,
- pilot plan,
- reviewer objections,
- explicit decisions for you.

If local tools are available, the agent should also use or inspect tool outputs:

- downloaded PDFs,
- PDF-to-Markdown notes,
- figure/table extraction reports,
- source analysis matrices,
- claim verification reports.

## 6. How Researchers Should Use It

Use the workflow as a learning loop:

1. Ask the agent to draft an artifact.
2. Read the assumptions.
3. Challenge weak parts.
4. Approve, reject, or revise.
5. Move to the next gate.

The value is not only the output. The value is seeing how a research idea becomes sharper under source grounding, formalization, and critique.
