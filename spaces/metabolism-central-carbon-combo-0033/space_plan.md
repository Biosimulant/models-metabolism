# Space Plan - metabolism-central-carbon-combo-0033

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-c-a-model1604280052-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-c-c-model1604280009-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-c-g-model1604280005-model

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
