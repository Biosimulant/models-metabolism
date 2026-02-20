# Space Prompt - metabolism-central-carbon-combo-0076

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-ahmad2017-genome-scale-metabolic-model-igt736-of-model1703060000-model, metabolism-sbml-akir2004-central-carbon-metabolism-of-s-cerevisi-model1008240001-model, metabolism-sbml-alam2010-genome-scale-metabolic-network-of-strep-model1507180005-model, metabolism-sbml-andersen2009-genome-scale-metabolic-network-of-a-model1507180047-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
