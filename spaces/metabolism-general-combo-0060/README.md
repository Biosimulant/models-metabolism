# COMBO_0060 - Metabolism General

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
- `metabolism-sbml-jallet2024-idj1518-genome-scale-model-of-ethanol-model2403010003-model`: Metabolism: Jallet2024Idj1518GenomeScaleModelOfEthanolModel2403010003Model
- `metabolism-sbml-jallet2024-isotopic-model-of-ethanolamine-metabo-model2403010002-model`: Metabolism: Jallet2024IsotopicModelOfEthanolamineMetaboModel2403010002Model
- `metabolism-sbml-jensen2020-streptococcus-oralis-icj415-biomd0000001086-model`: Metabolism: Jensen2020StreptococcusOralisIcj415Biomd0000001086Model
- `metabolism-sbml-jeon2018-enzyme-clustering-in-glucose-metabolism-biomd0000001055-model`: Metabolism: Jeon2018EnzymeClusteringInGlucoseMetabolismBiomd0000001055Model

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
- metabolism-sbml-jallet2024-idj1518-genome-scale-model-of-ethanol-model2403010003-model :: biomodels_ebi:MODEL2403010003 :: https://www.ebi.ac.uk/biomodels/MODEL2403010003
- metabolism-sbml-jallet2024-isotopic-model-of-ethanolamine-metabo-model2403010002-model :: biomodels_ebi:MODEL2403010002 :: https://www.ebi.ac.uk/biomodels/MODEL2403010002
- metabolism-sbml-jensen2020-streptococcus-oralis-icj415-biomd0000001086-model :: biomodels_ebi:BIOMD0000001086 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001086
- metabolism-sbml-jeon2018-enzyme-clustering-in-glucose-metabolism-biomd0000001055-model :: biomodels_ebi:BIOMD0000001055 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001055

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
