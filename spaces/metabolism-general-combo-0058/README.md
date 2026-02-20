# COMBO_0058 - Metabolism General

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
- `metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200001-model`: Metabolism: Gebauer2016GenomeScaleModelOfCaenorhabditisModel1704200001Model
- `metabolism-sbml-green1994-whole-body-vitamin-a-metabolism-in-hum-model2403010001-model`: Metabolism: Green1994WholeBodyVitaminAMetabolismInHumModel2403010001Model
- `metabolism-sbml-green2024-whole-body-vitamin-a-metabolism-in-hum-model2411290001-model`: Metabolism: Green2024WholeBodyVitaminAMetabolismInHumModel2411290001Model
- `metabolism-sbml-haiman2020-full-kinase-regulatory-model-of-eryth-model2012150001-model`: Metabolism: Haiman2020FullKinaseRegulatoryModelOfErythModel2012150001Model

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
- metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200001-model :: biomodels_ebi:MODEL1704200001 :: https://www.ebi.ac.uk/biomodels/MODEL1704200001
- metabolism-sbml-green1994-whole-body-vitamin-a-metabolism-in-hum-model2403010001-model :: biomodels_ebi:MODEL2403010001 :: https://www.ebi.ac.uk/biomodels/MODEL2403010001
- metabolism-sbml-green2024-whole-body-vitamin-a-metabolism-in-hum-model2411290001-model :: biomodels_ebi:MODEL2411290001 :: https://www.ebi.ac.uk/biomodels/MODEL2411290001
- metabolism-sbml-haiman2020-full-kinase-regulatory-model-of-eryth-model2012150001-model :: biomodels_ebi:MODEL2012150001 :: https://www.ebi.ac.uk/biomodels/MODEL2012150001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
