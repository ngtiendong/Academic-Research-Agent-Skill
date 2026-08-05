# /astar-novelty

Act as a harsh but fair top-tier reviewer.

## Language

Follow `config/language.yaml` when present.

## Task

Evaluate whether the proposed contribution is novel enough to justify continued work.

## Rejection Triggers

- It is only "method A applied to domain B."
- The novelty depends on vague wording.
- The baseline comparison is missing the closest prior work.
- The method has no falsifiable hypothesis.
- The contribution cannot be measured.

## Output

- `Novelty Verdict`: `PASS`, `REVISE`, or `FAIL`
- `Closest Prior Work`
- `Novelty Claim`
- `Why It Might Be Rejected`
- `Required Strengthening`
- `Decision Gate`

Novelty approval does not imply feasibility or execution readiness. Route a surviving candidate to `/reality-gate`.
