# Space Plan - metabolism-general-combo-0059

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-haiman2020-functional-enzyme-states-in-the-e-col-model2012150003-model, metabolism-sbml-haiman2020-pyruvate-kinase-regulatory-model-of-e-model2012150002-model, metabolism-sbml-heinemann2005-genome-scale-reconstruction-of-sta-model1507180072-model, metabolism-sbml-icho2441-model2206100001-model

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
