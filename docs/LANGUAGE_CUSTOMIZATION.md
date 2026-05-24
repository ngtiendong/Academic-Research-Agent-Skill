# Language Customization

The system separates prompt language from output language.

## Design Choice

Prompts are written in English because most models follow technical research instructions more reliably in English. User-facing outputs can be localized through `config/language.yaml`.

## Configuration

```yaml
output_language: "Vietnamese"
secondary_language: "English"
translation_mode: "technical-terms-in-english"
```

## Modes

| Mode | Behavior |
|---|---|
| `english-only` | All output in English. |
| `technical-terms-in-english` | Localized prose, technical terms kept in English. |
| `bilingual-summary` | Main answer plus short summary in the secondary language. |

## Prompt Instruction Pattern

Each command should follow this rule:

```text
If config/language.yaml exists, obey output_language and translation_mode.
If it does not exist, write in English.
Never translate paper titles, model names, dataset names, metrics, or citation keys unless the user explicitly asks.
```
