# Space Plan - metabolism-general-combo-0052

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-costa2015-central-metabolism-of-e-coli-non-regul-model1504080005-model, metabolism-sbml-costa2015-central-metabolism-of-e-coli-regulated-model1504080004-model, metabolism-sbml-curien2009-aspartate-metabolism-biomd0000000212-model

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
