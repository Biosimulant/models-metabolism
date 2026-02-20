# Space Plan - metabolism-general-combo-0062

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-kurpad-2023-vitamin-b12-metabolism-in-humans-stu-model2503310002-model, metabolism-sbml-lai2007-o2-transport-metabolism-biomd0000000248-model, metabolism-sbml-lavoie2020-f-cylindrus-genome-scale-model-model2001280001-model, metabolism-sbml-lee2017-paracetamol-first-pass-metabolism-pk-mod-biomd0000000947-model

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
