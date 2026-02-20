# COMBO_0062 - Metabolism General

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
- `metabolism-sbml-kurpad-2023-vitamin-b12-metabolism-in-humans-stu-model2503310002-model`: Metabolism: Kurpad2023VitaminB12MetabolismInHumansStuModel2503310002Model
- `metabolism-sbml-lai2007-o2-transport-metabolism-biomd0000000248-model`: Metabolism: Lai2007O2TransportMetabolismBiomd0000000248Model
- `metabolism-sbml-lavoie2020-f-cylindrus-genome-scale-model-model2001280001-model`: Metabolism: Lavoie2020FCylindrusGenomeScaleModelModel2001280001Model
- `metabolism-sbml-lee2017-paracetamol-first-pass-metabolism-pk-mod-biomd0000000947-model`: Metabolism: Lee2017ParacetamolFirstPassMetabolismPkModBiomd0000000947Model

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
- metabolism-sbml-kurpad-2023-vitamin-b12-metabolism-in-humans-stu-model2503310002-model :: biomodels_ebi:MODEL2503310002 :: https://www.ebi.ac.uk/biomodels/MODEL2503310002
- metabolism-sbml-lai2007-o2-transport-metabolism-biomd0000000248-model :: biomodels_ebi:BIOMD0000000248 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000248
- metabolism-sbml-lavoie2020-f-cylindrus-genome-scale-model-model2001280001-model :: biomodels_ebi:MODEL2001280001 :: https://www.ebi.ac.uk/biomodels/MODEL2001280001
- metabolism-sbml-lee2017-paracetamol-first-pass-metabolism-pk-mod-biomd0000000947-model :: biomodels_ebi:BIOMD0000000947 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000947

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
