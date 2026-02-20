# Space Plan - metabolism-general-combo-0053

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-curto1998-purine-metabolism-biomd0000000015-model, metabolism-sbml-czajka2024-lipomyces-genome-scale-model-model2403190001-model, metabolism-sbml-dalvigarcia2021-dopaminergic-and-serotonergic-ky-model2103060001-model

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
