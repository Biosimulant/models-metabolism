# Space Plan - metabolism-central-carbon-combo-0008

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-ankrah2019-syntrophic-splitting-of-central-carbo-model1908040004-model, metabolism-sbml-ankrah2021-genome-scale-metabolic-model-of-droso-model2002040002-model

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
