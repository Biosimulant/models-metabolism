# Space Plan - metabolism-central-carbon-combo-0044

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-s-j-model1604280026-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-s-p-model1604280041-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-s-r-model1604280042-model

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
