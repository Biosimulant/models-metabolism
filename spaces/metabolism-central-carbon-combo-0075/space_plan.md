# Space Plan - metabolism-central-carbon-combo-0075

## Scientific Scope
- Domain: metabolism
- Theme: central_carbon
- Base models: metabolism-sbml-agora-strain-specific-genome-scale-metabolic-mod-model2406250011-model, metabolism-sbml-ahmad2017-genome-scale-metabolic-model-igt736-of-model1703060000-model, metabolism-sbml-akir2004-central-carbon-metabolism-of-s-cerevisi-model1008240001-model, metabolism-sbml-alam2010-genome-scale-metabolic-network-of-strep-model1507180005-model

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
