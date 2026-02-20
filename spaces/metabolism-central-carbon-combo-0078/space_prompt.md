# Space Prompt - metabolism-central-carbon-combo-0078

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-alam2010-genome-scale-metabolic-network-of-strep-model1507180005-model, metabolism-sbml-andersen2009-genome-scale-metabolic-network-of-a-model1507180047-model, metabolism-sbml-ankrah2018-the-cost-of-metabolic-interactions-in-model1806250003-model, metabolism-sbml-ankrah2018-the-cost-of-metabolic-interactions-in-model1806250004-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
