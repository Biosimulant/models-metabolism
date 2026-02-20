# Space Prompt - metabolism-central-carbon-combo-0016

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-bekaert2010-rat-inferred-metabolic-network-model1008120003-model, metabolism-sbml-bekaert2012-reconstruction-of-d-rerio-metabolic-model1204120000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
