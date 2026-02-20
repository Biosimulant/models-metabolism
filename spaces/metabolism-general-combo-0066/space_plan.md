# Space Plan - metabolism-general-combo-0066

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-oliveira2020-e-coli-extended-central-carbon-meta-model2010160002-model, metabolism-sbml-oliveira2020-extended-e-coli-central-carbon-meta-model2010030001-model, metabolism-sbml-olsen2003-neutrophil-oscillatory-metabolism-biomd0000000143-model, metabolism-sbml-ponce-de-leon2015-genome-scale-model-of-bacteria-model1601050000-model

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
