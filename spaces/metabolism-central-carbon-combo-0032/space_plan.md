# Space Plan - metabolism-central-carbon-combo-0032

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-a-t-model1604280019-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-b-c-model1604280032-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-b-d-model1604280048-model

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
