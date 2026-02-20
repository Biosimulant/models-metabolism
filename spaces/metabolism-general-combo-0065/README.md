# COMBO_0065 - Metabolism General

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
- `metabolism-sbml-nijhout2006-hepatic-folate-metab-model1007200000-model`: Metabolism: Nijhout2006HepaticFolateMetabModel1007200000Model
- `metabolism-sbml-norman2019-genome-scale-model-of-clostridium-aut-model1810120001-model`: Metabolism: Norman2019GenomeScaleModelOfClostridiumAutModel1810120001Model
- `metabolism-sbml-odea2007-a-homeostatic-model-of-i-b-metabolism-t-model1908270002-model`: Metabolism: Odea2007AHomeostaticModelOfIBMetabolismTModel1908270002Model
- `metabolism-sbml-odea2007-ikappab-biomd0000000147-model`: Metabolism: Odea2007IkappabBiomd0000000147Model

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
- metabolism-sbml-nijhout2006-hepatic-folate-metab-model1007200000-model :: biomodels_ebi:MODEL1007200000 :: https://www.ebi.ac.uk/biomodels/MODEL1007200000
- metabolism-sbml-norman2019-genome-scale-model-of-clostridium-aut-model1810120001-model :: biomodels_ebi:MODEL1810120001 :: https://www.ebi.ac.uk/biomodels/MODEL1810120001
- metabolism-sbml-odea2007-a-homeostatic-model-of-i-b-metabolism-t-model1908270002-model :: biomodels_ebi:MODEL1908270002 :: https://www.ebi.ac.uk/biomodels/MODEL1908270002
- metabolism-sbml-odea2007-ikappab-biomd0000000147-model :: biomodels_ebi:BIOMD0000000147 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000147

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
