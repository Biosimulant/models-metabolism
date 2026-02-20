# Space Plan - metabolism-general-combo-0055

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-ecmodel-of-humangem-model2210090003-model, metabolism-sbml-enuh2022-phb-and-osmoprotectant-metabolism-model-model2204110001-model, metabolism-sbml-erythrocyte-model-of-the-hemoglobin-oxygen-disso-model2305140001-model

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
