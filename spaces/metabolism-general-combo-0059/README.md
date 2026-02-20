# COMBO_0059 - Metabolism General

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
- `metabolism-sbml-haiman2020-functional-enzyme-states-in-the-e-col-model2012150003-model`: Metabolism: Haiman2020FunctionalEnzymeStatesInTheEColModel2012150003Model
- `metabolism-sbml-haiman2020-pyruvate-kinase-regulatory-model-of-e-model2012150002-model`: Metabolism: Haiman2020PyruvateKinaseRegulatoryModelOfEModel2012150002Model
- `metabolism-sbml-heinemann2005-genome-scale-reconstruction-of-sta-model1507180072-model`: Metabolism: Heinemann2005GenomeScaleReconstructionOfStaModel1507180072Model
- `metabolism-sbml-icho2441-model2206100001-model`: Metabolism: Icho2441Model2206100001Model

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
- metabolism-sbml-haiman2020-functional-enzyme-states-in-the-e-col-model2012150003-model :: biomodels_ebi:MODEL2012150003 :: https://www.ebi.ac.uk/biomodels/MODEL2012150003
- metabolism-sbml-haiman2020-pyruvate-kinase-regulatory-model-of-e-model2012150002-model :: biomodels_ebi:MODEL2012150002 :: https://www.ebi.ac.uk/biomodels/MODEL2012150002
- metabolism-sbml-heinemann2005-genome-scale-reconstruction-of-sta-model1507180072-model :: biomodels_ebi:MODEL1507180072 :: https://www.ebi.ac.uk/biomodels/MODEL1507180072
- metabolism-sbml-icho2441-model2206100001-model :: biomodels_ebi:MODEL2206100001 :: https://www.ebi.ac.uk/biomodels/MODEL2206100001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
