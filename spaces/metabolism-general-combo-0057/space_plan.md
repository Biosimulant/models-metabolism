# Space Plan - metabolism-general-combo-0057

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-feist2014-geobacter-metallireducens-gs-15-metabo-model2204190002-model, metabolism-sbml-ford2020-whole-body-vitamin-a-metabolism-in-huma-model2312190001-model, metabolism-sbml-furr2005-whole-body-vitamin-a-metabolism-in-huma-model2405200001-model, metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200000-model

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
