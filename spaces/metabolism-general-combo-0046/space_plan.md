# Space Plan - metabolism-general-combo-0046

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-babaev2024-cyp2c9-variants-model2412180002-model, metabolism-sbml-babaev2025-cyp2c9-and-abcb1-losartan-metabolism-model2504020001-model, metabolism-sbml-bannerman2022-whole-genome-metabolism-m-abscessu-model2203300002-model

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
