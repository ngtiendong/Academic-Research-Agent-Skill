# Tool Layer Reference

Research Agent Skill is designed to work with concrete research tools, not only free-form chat.

## Tool-Assisted Ingestion

When available, use tools to create inspectable evidence artifacts before writing research claims.

| Tool class | Purpose | Typical output |
|---|---|---|
| Paper downloader | Download PDFs from paper lists, arXiv links, DOI pages, or curated source lists. | `papers/`, download report, missing-source list |
| PDF-to-Markdown converter | Convert papers into readable Markdown notes for agent inspection. | per-paper `.md` notes |
| Figure/table extractor | Extract captions, crop figures/tables, and summarize visual evidence. | figure/table crops, caption index, visual analysis report |
| Source analysis matrix builder | Compare papers by problem, method, dataset, metric, result, limitation, and relevance. | `19_Source_Analysis_Matrix.md/.csv` |
| Claim tracer | Link draft claims back to sources, figures, tables, or experiment artifacts. | claim verification report |

## Minimum Tool Contract

Tools should produce artifacts that can be reviewed by a human and reused by an agent.

Recommended fields:

- source id,
- source path or URL,
- title,
- venue/year when available,
- extraction status,
- key claims,
- method summary,
- datasets and metrics,
- figures/tables detected,
- limitations,
- relevance to current project,
- errors or missing files.

## Figure and Table Reading

Figures and tables often contain the most important evidence in technical papers. When a tool extracts them, the agent should inspect:

- figure/table caption,
- surrounding context,
- what result or mechanism is shown,
- which metric or dataset is involved,
- whether the visual supports a reusable claim,
- whether the visual reveals a limitation or hidden assumption.

## Source Labels

Use source labels consistently:

- `downloaded`: PDF was retrieved locally.
- `converted`: Markdown note was generated.
- `visuals-extracted`: figures/tables were extracted or indexed.
- `inspected`: agent read the relevant source material.
- `evidence-ready`: source can support claims.
- `blocked`: download, conversion, or extraction failed.

## Agent Behavior

If tool outputs exist, read them before drafting. If a tool fails, report the failure instead of fabricating missing evidence.
