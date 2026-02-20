# Space Prompt - metabolism-general-combo-0066

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-oliveira2020-e-coli-extended-central-carbon-meta-model2010160002-model, metabolism-sbml-oliveira2020-extended-e-coli-central-carbon-meta-model2010030001-model, metabolism-sbml-olsen2003-neutrophil-oscillatory-metabolism-biomd0000000143-model, metabolism-sbml-ponce-de-leon2015-genome-scale-model-of-bacteria-model1601050000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
