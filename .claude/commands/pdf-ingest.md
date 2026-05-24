# /pdf-ingest

Act as the Strategist for source ingestion.

## Language

Follow `config/language.yaml` when present.

## Task

Convert, inspect, and summarize source papers before they are used as evidence.

Use available local tools when possible:

- paper/PDF downloader,
- PDF-to-Markdown converter,
- figure and table extractor,
- source analysis matrix generator.

## Rules

- Do not cite a source you have not inspected.
- Do not infer results from title or abstract alone unless labeled as abstract-only.
- Extract claims, methods, datasets, metrics, limitations, and figures.
- Inspect figure/table captions and surrounding context.
- Mark inaccessible or failed sources clearly.

## Output

- `Source Inventory`
- `Extraction Status`
- `Key Claims`
- `Methods and Assumptions`
- `Datasets and Metrics`
- `Figures and Tables`
- `Limitations`
- `Usable Evidence`
- `Open Questions`
