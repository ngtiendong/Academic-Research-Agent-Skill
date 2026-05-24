# Research Tools

Research Agent Skill is designed to work with a practical tool layer for technical literature review.

## Tool Categories

| Tool | Purpose | Output |
|---|---|---|
| Paper downloader | Download PDFs from paper lists, arXiv URLs, DOI pages, or curated reading lists. | local PDFs, download report, missing-source list |
| PDF-to-Markdown converter | Convert papers into readable notes for agents and students. | per-paper Markdown notes |
| Figure/table analyzer | Extract captions, crop visual evidence, and summarize important figures/tables. | crops, caption index, visual analysis report |
| Source matrix generator | Compare many papers systematically. | Markdown/CSV analysis matrix |
| Claim verifier | Link claims to source notes, figures, tables, or experiment results. | claim verification report |

## Why Tools Matter

Academic papers often hide key evidence in figures, tables, appendices, and evaluation details. A chat-only workflow tends to miss these. Tool-assisted ingestion makes the workflow more inspectable:

- PDFs are stored locally.
- Markdown notes can be searched and reviewed.
- Figures and tables can be analyzed separately.
- Source matrices make comparison easier.
- Claims can be traced back to evidence.

## Recommended Artifact Layout

```text
papers/
paper_notes/
figure_tables/
source_lists/
19_Source_Analysis_Matrix.md
19_Source_Analysis_Matrix.csv
download_report.md
claim_verification_report.md
```

## Agent Rule

If these artifacts exist, the agent should read them before drafting. If extraction fails, it should report the failure and ask for a decision instead of inventing missing evidence.
