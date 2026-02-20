# Space Plan - metabolism-general-combo-0054

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-deborasoncini2024-nad-biosynthesis-in-human-b-ly-model2311140001-model, metabolism-sbml-dicenzo2020-sinorhizobium-meliloti-1021-genome-s-model2003240001-model, metabolism-sbml-dvarak2020-pxr-targeting-using-microbial-metabol-model2002050001-model

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
