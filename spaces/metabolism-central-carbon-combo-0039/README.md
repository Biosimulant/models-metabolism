# COMBO_0039 - Metabolism Central Carbon

## Scientific Question
How do central carbon mechanisms compare across these models?

## Biological Context
Biochemical flux and energy balance across metabolic pathways.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-m-g-model1604280036-model`: Metabolism: Castillo2016WholeGenomeMetabolicModelOfMGModel1604280036Model
- `metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-n-c-model1604280046-model`: Metabolism: Castillo2016WholeGenomeMetabolicModelOfNCModel1604280046Model
- `metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-n-f-model1604280053-model`: Metabolism: Castillo2016WholeGenomeMetabolicModelOfNFModel1604280053Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-m-g-model1604280036-model :: biomodels_ebi:MODEL1604280036 :: https://www.ebi.ac.uk/biomodels/MODEL1604280036
- metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-n-c-model1604280046-model :: biomodels_ebi:MODEL1604280046 :: https://www.ebi.ac.uk/biomodels/MODEL1604280046
- metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-n-f-model1604280053-model :: biomodels_ebi:MODEL1604280053 :: https://www.ebi.ac.uk/biomodels/MODEL1604280053

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
