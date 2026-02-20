# Space Plan - metabolism-lipid-metabolism-combo-0068

## Scientific Scope
- Domain: metabolism
- Theme: lipid_metabolism
- Base models: metabolism-sbml-davies2023-cholesterol-metabolism-and-atheroscle-model2306300001-model, metabolism-sbml-gupta2009-eicosanoid-metabolism-biomd0000000436-model, metabolism-sbml-mcauley2012-whole-body-cholesterol-metabolism-biomd0000000434-model, metabolism-sbml-morgan2016-dynamics-of-cholesterol-metabolism-an-model1508170000-model

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
