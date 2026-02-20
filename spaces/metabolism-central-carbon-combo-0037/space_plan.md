# Space Plan - metabolism-central-carbon-combo-0037

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-f-v-model1604280003-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-h-c-model1604280027-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-k-l-model1604280015-model

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
