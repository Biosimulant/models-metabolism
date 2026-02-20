# Space Plan - metabolism-general-combo-0045

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-adams2019-the-regulatory-role-of-shikimate-in-pl-biomd0000000847-model, metabolism-sbml-aubert2002-coupling-between-brain-electrical-act-biomd0000000570-model, metabolism-sbml-aubert2005-interaction-between-astrocytes-and-ne-model1411210000-model

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
