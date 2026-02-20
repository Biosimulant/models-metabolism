# COMBO_0061 - Metabolism General

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
- `metabolism-sbml-kees2018-genome-scale-constraint-based-model-of-model1710040000-model`: Metabolism: Kees2018GenomeScaleConstraintBasedModelOfModel1710040000Model
- `metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1204270001-model`: Metabolism: Koenig2012HepaticGlucoseMetabolismModel1204270001Model
- `metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1209260000-model`: Metabolism: Koenig2012HepaticGlucoseMetabolismModel1209260000Model
- `metabolism-sbml-kolbe2019-spatio-temporal-liver-zonation-model2009110001-model`: Metabolism: Kolbe2019SpatioTemporalLiverZonationModel2009110001Model

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
- metabolism-sbml-kees2018-genome-scale-constraint-based-model-of-model1710040000-model :: biomodels_ebi:MODEL1710040000 :: https://www.ebi.ac.uk/biomodels/MODEL1710040000
- metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1204270001-model :: biomodels_ebi:MODEL1204270001 :: https://www.ebi.ac.uk/biomodels/MODEL1204270001
- metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1209260000-model :: biomodels_ebi:MODEL1209260000 :: https://www.ebi.ac.uk/biomodels/MODEL1209260000
- metabolism-sbml-kolbe2019-spatio-temporal-liver-zonation-model2009110001-model :: biomodels_ebi:MODEL2009110001 :: https://www.ebi.ac.uk/biomodels/MODEL2009110001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
