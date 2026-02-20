# Space Prompt - metabolism-general-combo-0061

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-kees2018-genome-scale-constraint-based-model-of-model1710040000-model, metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1204270001-model, metabolism-sbml-koenig2012-hepatic-glucose-metabolism-model1209260000-model, metabolism-sbml-kolbe2019-spatio-temporal-liver-zonation-model2009110001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
