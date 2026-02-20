# Space Plan - metabolism-general-combo-0061

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-kees2018-genome-scale-constraint-based-model-of-model1710040000-model, metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1204270001-model, metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1209260000-model, metabolism-sbml-kolbe2019-spatio-temporal-liver-zonation-model2009110001-model

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
