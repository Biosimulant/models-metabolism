# COMBO_0063 - Metabolism General

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
- `metabolism-sbml-liu2019-clostridium-ljungdahlii-metabolism-model-model2204200003-model`: Metabolism: Liu2019ClostridiumLjungdahliiMetabolismModelModel2204200003Model
- `metabolism-sbml-luna2013-circadianclock-sirt1-model2112310002-model`: Metabolism: Luna2013CircadianclockSirt1Model2112310002Model
- `metabolism-sbml-masison2022-liver-iron-metabolism-with-updated-f-model2211030002-model`: Metabolism: Masison2022LiverIronMetabolismWithUpdatedFModel2211030002Model
- `metabolism-sbml-mcdougal2017-metabolism-in-ischemic-cardiomyocyt-biomd0000000961-model`: Metabolism: Mcdougal2017MetabolismInIschemicCardiomyocytBiomd0000000961Model

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
- metabolism-sbml-liu2019-clostridium-ljungdahlii-metabolism-model-model2204200003-model :: biomodels_ebi:MODEL2204200003 :: https://www.ebi.ac.uk/biomodels/MODEL2204200003
- metabolism-sbml-luna2013-circadianclock-sirt1-model2112310002-model :: biomodels_ebi:MODEL2112310002 :: https://www.ebi.ac.uk/biomodels/MODEL2112310002
- metabolism-sbml-masison2022-liver-iron-metabolism-with-updated-f-model2211030002-model :: biomodels_ebi:MODEL2211030002 :: https://www.ebi.ac.uk/biomodels/MODEL2211030002
- metabolism-sbml-mcdougal2017-metabolism-in-ischemic-cardiomyocyt-biomd0000000961-model :: biomodels_ebi:BIOMD0000000961 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000961

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
