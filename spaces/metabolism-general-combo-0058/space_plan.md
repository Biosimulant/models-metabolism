# Space Plan - metabolism-general-combo-0058

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200001-model, metabolism-sbml-green1994-whole-body-vitamin-a-metabolism-in-hum-model2403010001-model, metabolism-sbml-green2024-whole-body-vitamin-a-metabolism-in-hum-model2411290001-model, metabolism-sbml-haiman2020-full-kinase-regulatory-model-of-eryth-model2012150001-model

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
