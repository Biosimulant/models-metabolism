# Space Plan - metabolism-central-carbon-combo-0079

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-andersen2009-genome-scale-metabolic-network-of-a-model1507180047-model, metabolism-sbml-ankrah2018-the-cost-of-metabolic-interactions-in-model1806250003-model, metabolism-sbml-ankrah2018-the-cost-of-metabolic-interactions-in-model1806250004-model, metabolism-sbml-ankrah2018-the-cost-of-metabolic-interactions-in-model1806250005-model

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
