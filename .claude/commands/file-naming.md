# /file-naming

Act as the repository librarian.

## Language

Follow `config/language.yaml` when present.

## Task

Resolve the active naming profile and normalize research artifact names without changing their meaning. Precedence is explicit user instruction, then project-local rule or established artifact set, then the skill default.

## Convention

```text
01_Project_State.md
02_Scope.md
03_Draft.md
04_Literature_Review.md
05_Lit_Grounding.md
06_Math_Formalization.md
10_Risk_Plan.md
11_WorkBreakdown.md
12_Code_Execution_Plan.md
13_Implementation_Guide.md
14_Agent_Brief_PhaseN.md
15_Changelog.md
18_Source_Notes_Index.md
19_Source_Analysis_Matrix.md
20_Reality_Gate.md
21_Hypothesis_Decision_Map.md
22_Experimental_Unit_Audit_Plan.md
23_Feasibility_Pilot_Protocol.md
24_Mechanism_Method_Routing.md
```

Do not fill numbering gaps or repurpose a reserved slot. In an isolated reframe folder, let the folder carry the candidate name instead of repeating an acronym in every filename.

## Output

- `Current Names`
- `Proposed Names`
- `Reason`
- `Potential Broken References`
- `Validation Command`
- `Approval Needed`
