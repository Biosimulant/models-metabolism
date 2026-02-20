# Space Prompt - metabolism-general-combo-0069

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-reyes-palomares2012-a-combined-model-hepatic-pol-biomd0000000450-model, metabolism-sbml-reyes-palomares2012-a-combined-model-hepatic-pol-biomd0000000674-model, metabolism-sbml-rienksma2014-genome-scale-constraint-based-metab-model1411110000-model, metabolism-sbml-saa2016-mammalian-methionine-cycle-approximate-b-model1603150000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
