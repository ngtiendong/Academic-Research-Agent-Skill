# Research Reality Gate

Use this gate before implementation planning, after a reframe, when the user requests a feasibility decision, or whenever a research plan looks complete but rests on unverified assumptions. Do not manufacture a formal gate artifact for every raw idea; use `NOT_ASSESSED` until a measurable candidate and a named unit/access path exist.

## Evidence hierarchy

Prefer:

1. claim-eligible raw result rows with provenance;
2. inspected raw samples, model traces, timed micro-tests, and validated controls;
3. inspected primary sources and official dataset/model documentation;
4. current claim and measurement contracts;
5. plans, reviews, scores, and checklists.

Items 4–5 define obligations but cannot prove feasibility.

## Three decisions

| Layer | Question |
|---|---|
| Scientific reality | Can the actual unit, measurement, and intervention test the exact claim? |
| Engineering reality | Can the exact data/model/code path run with traceable inputs and bounded cost? |
| Paper viability | If the decisive result is null, does a pre-specified bounded claim remain without changing the question? |

Do not collapse these decisions into one score.

## Required certificates

| Certificate | Pass evidence |
|---|---|
| Phenomenon | small real paired sample, exact denominator, counterfactual/control, and uncertainty or frozen feasibility threshold |
| Experimental unit | complete ordered inputs, labels, provenance, grouping, inclusion rule, and observed valid yield |
| Measurement | formal event/score, denominator, operational computation on real output, valid control/null, missingness, and uncertainty |
| Treatment/intervention validity | stable truth and endpoint, before/after audit, matched control, and survival through real preprocessing |
| Access/preprocessing | versioned data/model access and one end-to-end trace without silent truncation, reorder, resize loss, or missing fields |
| Closest-competitor delta | inspected direct competitors, already-solved surface, residual, and a baseline/control that can falsify it |
| Resource/valid yield | timed micro-test, valid rows per attempted row, human time, compute/storage/API envelope, and retry cap |
| Joint claim dependency | explicit mandatory/optional graph, one nucleus, and kill/drop rule for every headline claim |

Use only `pass`, `fail`, `unknown`, or justified `not_applicable` for certificates. A `pass` requires inspected evidence. An `unknown` requires one bounded test, owner, maximum cost, acceptance criterion, and stop condition.

## Claim survival graph

Record for each headline claim:

```text
claim
→ required phenomenon
→ experimental unit
→ treatment/control
→ metric
→ result artifact
→ kill condition
```

Failure of a mandatory node fails the claim. Do not average mandatory gates or invent probabilities for them.

## Verdicts

- `BLOCK`: a certificate failed, an unknown lacks a bounded test, or the requested plan is deeper than the evidence.
- `FEASIBILITY_PILOT_ONLY`: no known fatal failure remains and every unknown has a bounded test.
- `EXECUTION_READY`: all hard certificates pass for the named implementation scope and the next gate is frozen.
- `FULL_RUN_READY`: execution requirements plus a claim-eligible pilot, frozen primary contrast/sample logic, complete provenance, and human approval.

## Plan-depth rule

- Under `BLOCK`, create only corrective evidence tasks.
- Under `FEASIBILITY_PILOT_ONLY`, create only the protocol/code needed for the bounded falsifier.
- Do not create broad WBS, model grids, multi-week code architecture, or full drafts while a cheaper fatal assumption remains unresolved.
- A positive point estimate does not authorize a full run.

## Decision-tree audit

A valid tree must contain a stop/drop branch. Fail the gate when every result says continue, reframe, or strengthen another claim. A null fallback is valid only when it was pre-specified, answers the same question, and uses the same experimental unit.

## Output contract

Return:

1. verdict and exact authorized scope;
2. fatal assumption tested first;
3. certificate table with evidence paths;
4. claim survival graph;
5. highest-information next test, owner, maximum cost, acceptance, and stop;
6. explicitly prohibited work;
7. researcher decision needed.
