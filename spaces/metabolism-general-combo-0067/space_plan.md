# Space Plan - metabolism-general-combo-0067

## Scientific Scope
- Domain: metabolism
- Theme: general
- Base models: metabolism-sbml-reddyhoff2015-acetaminophen-metabolism-and-toxic-biomd0000000609-model, metabolism-sbml-reed2008-glutathione-metabolism-biomd0000000268-model, metabolism-sbml-reyes-palomares2012-a-combined-model-hepatic-pol-biomd0000000450-model, metabolism-sbml-reyes-palomares2012-a-combined-model-hepatic-pol-biomd0000000674-model

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
