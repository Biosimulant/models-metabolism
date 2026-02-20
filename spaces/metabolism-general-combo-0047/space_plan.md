# Space Plan - metabolism-general-combo-0047

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-bannerman2022-whole-genome-metabolism-mycobacter-model2203300001-model, metabolism-sbml-bulik2016-regulation-of-hepatic-glucose-metaboli-biomd0000000633-model, metabolism-sbml-canto-encalada2022-fba-of-simultaneous-degradati-biomd0000001061-model

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
