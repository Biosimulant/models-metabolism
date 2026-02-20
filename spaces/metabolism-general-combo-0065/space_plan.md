# Space Plan - metabolism-general-combo-0065

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-nijhout2006-hepatic-folate-metab-model1007200000-model, metabolism-sbml-norman2019-genome-scale-model-of-clostridium-aut-model1810120001-model, metabolism-sbml-odea2007-a-homeostatic-model-of-i-b-metabolism-t-model1908270002-model, metabolism-sbml-odea2007-ikappab-biomd0000000147-model

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
