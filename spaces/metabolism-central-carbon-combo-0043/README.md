# COMBO_0043 - Metabolism Central Carbon

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
- `metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-p-s-model1604280049-model`: Metabolism: Castillo2016WholeGenomeMetabolicModelOfPSModel1604280049Model
- `metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-r-o-model1604280023-model`: Metabolism: Castillo2016WholeGenomeMetabolicModelOfROModel1604280023Model
- `metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-s-c-model1604280034-model`: Metabolism: Castillo2016WholeGenomeMetabolicModelOfSCModel1604280034Model

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
- metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-p-s-model1604280049-model :: biomodels_ebi:MODEL1604280049 :: https://www.ebi.ac.uk/biomodels/MODEL1604280049
- metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-r-o-model1604280023-model :: biomodels_ebi:MODEL1604280023 :: https://www.ebi.ac.uk/biomodels/MODEL1604280023
- metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-s-c-model1604280034-model :: biomodels_ebi:MODEL1604280034 :: https://www.ebi.ac.uk/biomodels/MODEL1604280034

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
