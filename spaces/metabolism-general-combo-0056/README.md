# COMBO_0056 - Metabolism General

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
- `metabolism-sbml-fatma2018-model-of-central-carbon-metabolism-of-model1802080001-model`: Metabolism: Fatma2018ModelOfCentralCarbonMetabolismOfModel1802080001Model
- `metabolism-sbml-feala2007-dros-mel-central-metabolism-model2784700357-model`: Metabolism: Feala2007DrosMelCentralMetabolismModel2784700357Model
- `metabolism-sbml-feist2007-ecmetabol-flux1-model3023609334-model`: Metabolism: Feist2007EcmetabolFlux1Model3023609334Model
- `metabolism-sbml-feist2007-ecmetabol-flux2-model3023641273-model`: Metabolism: Feist2007EcmetabolFlux2Model3023641273Model

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
- metabolism-sbml-fatma2018-model-of-central-carbon-metabolism-of-model1802080001-model :: biomodels_ebi:MODEL1802080001 :: https://www.ebi.ac.uk/biomodels/MODEL1802080001
- metabolism-sbml-feala2007-dros-mel-central-metabolism-model2784700357-model :: biomodels_ebi:MODEL2784700357 :: https://www.ebi.ac.uk/biomodels/MODEL2784700357
- metabolism-sbml-feist2007-ecmetabol-flux1-model3023609334-model :: biomodels_ebi:MODEL3023609334 :: https://www.ebi.ac.uk/biomodels/MODEL3023609334
- metabolism-sbml-feist2007-ecmetabol-flux2-model3023641273-model :: biomodels_ebi:MODEL3023641273 :: https://www.ebi.ac.uk/biomodels/MODEL3023641273

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
