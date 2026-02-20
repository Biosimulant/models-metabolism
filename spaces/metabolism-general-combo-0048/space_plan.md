# Space Plan - metabolism-general-combo-0048

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-chedere2022-nad-biosynthesis-in-human-liver-model2205250001-model, metabolism-sbml-choudhary2016-epithelial-to-mesenchymal-transiti-model1602080000-model, metabolism-sbml-cifelli2008-whole-body-vitamin-a-metabolism-in-h-model2403080002-model

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
