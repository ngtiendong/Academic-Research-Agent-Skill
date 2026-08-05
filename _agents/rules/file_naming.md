# File Naming Rule

Resolve names in this order:

1. an explicit user instruction for the current task;
2. the project-local naming rule or an established artifact set;
3. the default profile below.

Numbering is a profile for stable navigation. It does not change the semantic artifact type and must never be used to make an unrelated file look canonical.

## Default artifact registry

| Slot | Logical artifact | Default filename |
|---:|---|---|
| 01 | Project state | `01_Project_State.md` |
| 02 | Scope | `02_Scope.md` |
| 03 | Draft | `03_Draft.md` |
| 04 | Literature review | `04_Literature_Review.md` |
| 05 | Literature grounding | `05_Lit_Grounding.md` |
| 06 | Mathematical formalization | `06_Math_Formalization.md` |
| 07 | Reviewer simulation | `07_ReviewerSim_<Venue>.md` |
| 08 | Review fixes | `08_ReviewFixes_<Venue>.md` |
| 10 | Risk plan | `10_Risk_Plan.md` |
| 11 | Work breakdown | `11_WorkBreakdown.md` |
| 12 | Code execution plan | `12_Code_Execution_Plan.md` |
| 13 | Implementation guide | `13_Implementation_Guide.md` |
| 14 | Phase brief | `14_Agent_Brief_PhaseN.md` |
| 15 | Changelog/decision log | `15_Changelog.md` |
| 18 | Source-notes index | `18_Source_Notes_Index.md` |
| 19 | Source-analysis matrix | `19_Source_Analysis_Matrix.md` |
| 20 | Research Reality Gate | `20_Reality_Gate.md` |
| 21 | Hypothesis decision map | `21_Hypothesis_Decision_Map.md` |
| 22 | Experimental-unit audit plan | `22_Experimental_Unit_Audit_Plan.md` |
| 23 | Scientific feasibility-pilot protocol | `23_Feasibility_Pilot_Protocol.md` |
| 24 | Mechanism-method routing | `24_Mechanism_Method_Routing.md` |

Slots `09` and `16-17` are intentionally unassigned in the default profile. Project-local profiles may reserve additional slots or use established paper-specific variants.

## Project profile

A project may insert an identifier between the slot and artifact stem, for example:

```text
01_Paper1_Pipeline_State.md
02_Paper1_Scope.md
20_Paper1_Reality_Gate.md
23_Paper1_Feasibility_Pilot_Protocol.md
```

`Pipeline_State` is an accepted project-local variant of `Project_State`. `Paper_Notes_Index` and `Paper_Analysis_Matrix` are accepted variants of the source-level names. Preserve local variants consistently; do not mix profiles inside one artifact set.

## Reframe workspace

- Let an isolated folder carry the reframe/candidate name.
- Do not repeat a candidate acronym in every filename unless the project profile explicitly requires it.
- Reuse canonical state and scope artifacts inside the reframe folder.
- Add slots `20-24` only for their registered semantic types.
- Do not create empty files to fill numeric gaps.
- Do not rename a hypothesis map to `03_Draft.md`, a Reality Gate to `04_Literature_Review.md`, or any other false equivalence.

Run `scripts/validate_artifact_set.py <artifact-folder>` after creating or renaming a multi-file artifact set.

## Materialization rule

The registry describes valid names, not a required file bundle. Create only the artifact supported by the current stage. A raw idea normally starts with `01_Project_State.md` and `02_Scope.md`; add `18_Source_Notes_Index.md` only when identifiable sources can be indexed. Do not create slots `05-06` or `20-24` merely to make a project look complete.
