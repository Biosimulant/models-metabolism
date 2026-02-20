# Space Plan - metabolism-central-carbon-combo-0040

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-n-h-model1604280025-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-p-b-model1604280014-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-p-c-model1604280001-model

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
