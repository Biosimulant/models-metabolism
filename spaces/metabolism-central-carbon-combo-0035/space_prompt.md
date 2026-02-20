# Space Prompt - metabolism-central-carbon-combo-0035

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-c-n-model1604280045-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-c-t-model1604280006-model, metabolism-sbml-castillo2016-whole-genome-metabolic-model-of-d-h-model1604280028-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
