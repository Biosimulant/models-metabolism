# Space Plan - metabolism-central-carbon-combo-0031

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-a-n-model1604280008-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-a-n-model1604280021-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-a-o-model1604280012-model

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
