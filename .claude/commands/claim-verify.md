# /claim-verify

Act as the Critic responsible for claim closure.

## Language

Follow `config/language.yaml` when present.

## Task

Trace every retained factual, novelty, method, and empirical claim to inspected evidence. Distinguish direct support, inference, contradiction, and missing evidence.

## Output

- `Claim Ledger`.
- `Evidence Path` for each claim.
- `Status`: `supported`, `partially-supported`, `contradicted`, `unverified`, or `dropped`.
- `Required Narrowing or Removal`.
- `Draft Readiness`.
- `Researcher Decision`.
