# COMBO_0028 - Metabolism Central Carbon

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
- `metabolism-sbml-casini2022-genome-scale-metabolic-model-imtd22ic-model2211290001-model`: Metabolism: Casini2022GenomeScaleMetabolicModelImtd22icModel2211290001Model
- `metabolism-sbml-caspeta2012-genome-scale-metabolic-network-of-pi-model1507180022-model`: Metabolism: Caspeta2012GenomeScaleMetabolicNetworkOfPiModel1507180022Model

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
- metabolism-sbml-casini2022-genome-scale-metabolic-model-imtd22ic-model2211290001-model :: biomodels_ebi:MODEL2211290001 :: https://www.ebi.ac.uk/biomodels/MODEL2211290001
- metabolism-sbml-caspeta2012-genome-scale-metabolic-network-of-pi-model1507180022-model :: biomodels_ebi:MODEL1507180022 :: https://www.ebi.ac.uk/biomodels/MODEL1507180022

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
