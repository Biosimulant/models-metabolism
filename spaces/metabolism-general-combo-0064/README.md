# COMBO_0064 - Metabolism General

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
- `metabolism-sbml-mitchell2013-liver-iron-metabolism-biomd0000000498-model`: Metabolism: Mitchell2013LiverIronMetabolismBiomd0000000498Model
- `metabolism-sbml-moore2023-gloeocapsopsis-dulcis-model-model2303050001-model`: Metabolism: Moore2023GloeocapsopsisDulcisModelModel2303050001Model
- `metabolism-sbml-mosca2012-central-carbon-metabolism-regulated-by-biomd0000000426-model`: Metabolism: Mosca2012CentralCarbonMetabolismRegulatedByBiomd0000000426Model
- `metabolism-sbml-mulquiney1999-bpg-metabolism-model5950552398-model`: Metabolism: Mulquiney1999BpgMetabolismModel5950552398Model

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
- metabolism-sbml-mitchell2013-liver-iron-metabolism-biomd0000000498-model :: biomodels_ebi:BIOMD0000000498 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000498
- metabolism-sbml-moore2023-gloeocapsopsis-dulcis-model-model2303050001-model :: biomodels_ebi:MODEL2303050001 :: https://www.ebi.ac.uk/biomodels/MODEL2303050001
- metabolism-sbml-mosca2012-central-carbon-metabolism-regulated-by-biomd0000000426-model :: biomodels_ebi:BIOMD0000000426 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000426
- metabolism-sbml-mulquiney1999-bpg-metabolism-model5950552398-model :: biomodels_ebi:MODEL5950552398 :: https://www.ebi.ac.uk/biomodels/MODEL5950552398

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
