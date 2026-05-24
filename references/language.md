# Language Reference

Prompts are written in English to keep agent behavior stable. Outputs can be localized through `config/language.yaml`.

## Modes

- `english-only`: all output in English.
- `technical-terms-in-english`: localized prose, key research terms remain in English.
- `bilingual-summary`: main answer plus short secondary-language summary.

## Do Not Translate By Default

- Paper titles.
- Model names.
- Dataset names.
- Metric names.
- Citation keys.
- Code identifiers.
- Established technical terms listed in `config/language.yaml`.

## Researcher Learning

When writing for students, briefly explain why a gate matters. Keep it practical, not lecture-like.
