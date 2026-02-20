# Space Prompt - metabolism-general-combo-0059

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-haiman2020-functional-enzyme-states-in-the-e-col-model2012150003-model, metabolism-sbml-haiman2020-pyruvate-kinase-regulatory-model-of-e-model2012150002-model, metabolism-sbml-heinemann2005-genome-scale-reconstruction-of-sta-model1507180072-model, metabolism-sbml-icho2441-model2206100001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
