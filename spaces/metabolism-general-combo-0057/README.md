# COMBO_0057 - Metabolism General

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
- `metabolism-sbml-feist2014-geobacter-metallireducens-gs-15-metabo-model2204190002-model`: Metabolism: Feist2014GeobacterMetallireducensGs15MetaboModel2204190002Model
- `metabolism-sbml-ford2020-whole-body-vitamin-a-metabolism-in-huma-model2312190001-model`: Metabolism: Ford2020WholeBodyVitaminAMetabolismInHumaModel2312190001Model
- `metabolism-sbml-furr2005-whole-body-vitamin-a-metabolism-in-huma-model2405200001-model`: Metabolism: Furr2005WholeBodyVitaminAMetabolismInHumaModel2405200001Model
- `metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200000-model`: Metabolism: Gebauer2016GenomeScaleModelOfCaenorhabditisModel1704200000Model

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
- metabolism-sbml-feist2014-geobacter-metallireducens-gs-15-metabo-model2204190002-model :: biomodels_ebi:MODEL2204190002 :: https://www.ebi.ac.uk/biomodels/MODEL2204190002
- metabolism-sbml-ford2020-whole-body-vitamin-a-metabolism-in-huma-model2312190001-model :: biomodels_ebi:MODEL2312190001 :: https://www.ebi.ac.uk/biomodels/MODEL2312190001
- metabolism-sbml-furr2005-whole-body-vitamin-a-metabolism-in-huma-model2405200001-model :: biomodels_ebi:MODEL2405200001 :: https://www.ebi.ac.uk/biomodels/MODEL2405200001
- metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200000-model :: biomodels_ebi:MODEL1704200000 :: https://www.ebi.ac.uk/biomodels/MODEL1704200000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
