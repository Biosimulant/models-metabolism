# COMBO_0052 - Metabolism General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Biochemical flux and energy balance across metabolic pathways.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `metabolism-sbml-costa2015-central-metabolism-of-e-coli-non-regul-model1504080005-model`: Metabolism: Costa2015CentralMetabolismOfEColiNonRegulModel1504080005Model
- `metabolism-sbml-costa2015-central-metabolism-of-e-coli-regulated-model1504080004-model`: Metabolism: Costa2015CentralMetabolismOfEColiRegulatedModel1504080004Model
- `metabolism-sbml-curien2009-aspartate-metabolism-biomd0000000212-model`: Metabolism: Curien2009AspartateMetabolismBiomd0000000212Model

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
- metabolism-sbml-costa2015-central-metabolism-of-e-coli-non-regul-model1504080005-model :: biomodels_ebi:MODEL1504080005 :: https://www.ebi.ac.uk/biomodels/MODEL1504080005
- metabolism-sbml-costa2015-central-metabolism-of-e-coli-regulated-model1504080004-model :: biomodels_ebi:MODEL1504080004 :: https://www.ebi.ac.uk/biomodels/MODEL1504080004
- metabolism-sbml-curien2009-aspartate-metabolism-biomd0000000212-model :: biomodels_ebi:BIOMD0000000212 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000212

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
