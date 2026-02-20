# Space Plan - metabolism-general-combo-0060

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-jallet2024-idj1518-genome-scale-model-of-ethanol-model2403010003-model, metabolism-sbml-jallet2024-isotopic-model-of-ethanolamine-metabo-model2403010002-model, metabolism-sbml-jensen2020-streptococcus-oralis-icj415-biomd0000001086-model, metabolism-sbml-jeon2018-enzyme-clustering-in-glucose-metabolism-biomd0000001055-model

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
