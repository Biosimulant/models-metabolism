# Space Prompt - metabolism-general-combo-0058

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200001-model, metabolism-sbml-green1994-whole-body-vitamin-a-metabolism-in-hum-model2403010001-model, metabolism-sbml-green2024-whole-body-vitamin-a-metabolism-in-hum-model2411290001-model, metabolism-sbml-haiman2020-full-kinase-regulatory-model-of-eryth-model2012150001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
