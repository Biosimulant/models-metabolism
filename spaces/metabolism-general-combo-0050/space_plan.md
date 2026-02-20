# Space Plan - metabolism-general-combo-0050

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-cloutier2009-energymetabolism-modelc-model1006230068-model, metabolism-sbml-cloutier2009-energymetabolism-modeld-model1006230095-model, metabolism-sbml-cloutier2009-energymetabolism-modele-model1006230059-model

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
