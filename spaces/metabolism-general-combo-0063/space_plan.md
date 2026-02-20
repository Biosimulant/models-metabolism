# Space Plan - metabolism-general-combo-0063

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-liu2019-clostridium-ljungdahlii-metabolism-model-model2204200003-model, metabolism-sbml-luna2013-circadianclock-sirt1-model2112310002-model, metabolism-sbml-masison2022-liver-iron-metabolism-with-updated-f-model2211030002-model, metabolism-sbml-mcdougal2017-metabolism-in-ischemic-cardiomyocyt-biomd0000000961-model

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
