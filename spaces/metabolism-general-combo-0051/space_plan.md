# Space Plan - metabolism-general-combo-0051

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-cloutier2009-energymetabolism-modelf-model1006230096-model, metabolism-sbml-costa2014-computational-model-of-l-lactis-metabo-biomd0000000572-model, metabolism-sbml-costa2015-central-metabolism-of-e-coli-extended-model1504080006-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
