# Space Plan - metabolism-central-carbon-combo-0073

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-abymbel891-strain-specific-genome-scale-metaboli-model2406250010-model, metabolism-sbml-achcar2012-glycolysis-in-bloodstream-form-t-bruc-biomd0000000428-model, metabolism-sbml-agora-strain-specific-genome-scale-metabolic-mod-model2406250011-model, metabolism-sbml-ahmad2017-genome-scale-metabolic-model-igt736-of-model1703060000-model

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
