# Space Plan - metabolism-general-combo-0064

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-mitchell2013-liver-iron-metabolism-biomd0000000498-model, metabolism-sbml-moore2023-gloeocapsopsis-dulcis-model-model2303050001-model, metabolism-sbml-mosca2012-central-carbon-metabolism-regulated-by-biomd0000000426-model, metabolism-sbml-mulquiney1999-bpg-metabolism-model5950552398-model

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
