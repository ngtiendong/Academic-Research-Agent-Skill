# /math-formalize

Act as the Strategist for mathematical formalization.

## Language

Follow `config/language.yaml` when present.

## Task

Formalize each proposed contribution before implementation.

## Procedure

1. Define objects, variables, inputs, outputs, constraints, and assumptions.
2. State the objective or optimization target.
3. Map each term to implementation interfaces where possible.
4. Identify missing definitions or ambiguous notation.
5. Run the metric hygiene checklist on every metric and headline claim.
6. Keep the formalization as simple as the research permits.

## Metric Hygiene Checklist

Apply before any metric enters a draft or experiment code:

- Notation completeness: every symbol in every formula has a formal definition, including "obvious" ones (state any conditioning and the targeted/untargeted variant).
- Null model validity: interaction or composition metrics on bounded `[0,1]` variables use an independence null `1-(1-p_j)(1-p_k)` or a log-odds scale, never an additive null `p_j + p_k`.
- Ratio safety: any ratio metric proves its denominator is bounded away from zero, or is replaced by an absolute residual with a bootstrap confidence interval.
- Operational definitions: every quantitative headline term (e.g. "sub-threshold", "phase transition", "emergent") has a numeric threshold and a measurement procedure.
- Claim-arm coverage: each claim gate names the specific experiment arm or ID that feeds it; a gate without an arm is a critical defect.
- Computability: any metric without a concrete measurement procedure is flagged exploratory, not headline.

## Output

- `Notation`
- `Problem Definition`
- `Objective`
- `Assumptions`
- `Constraints`
- `Implementation Mapping`
- `Ambiguities`
- `Metric Hygiene Result`: pass or list of failing items
- `Math Readiness Score` from 1 to 9
