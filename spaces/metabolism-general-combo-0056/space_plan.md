# Space Plan - metabolism-general-combo-0056

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-fatma2018-model-of-central-carbon-metabolism-of-model1802080001-model, metabolism-sbml-feala2007-dros-mel-central-metabolism-model2784700357-model, metabolism-sbml-feist2007-ecmetabol-flux1-model3023609334-model, metabolism-sbml-feist2007-ecmetabol-flux2-model3023641273-model

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
