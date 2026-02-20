# Space Prompt - metabolism-general-combo-0056

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-fatma2018-model-of-central-carbon-metabolism-of-model1802080001-model, metabolism-sbml-feala2007-dros-mel-central-metabolism-model2784700357-model, metabolism-sbml-feist2007-ecmetabol-flux1-model3023609334-model, metabolism-sbml-feist2007-ecmetabol-flux2-model3023641273-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
