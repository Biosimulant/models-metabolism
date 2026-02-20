# Space Prompt - metabolism-general-combo-0064

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-mitchell2013-liver-iron-metabolism-biomd0000000498-model, metabolism-sbml-moore2023-gloeocapsopsis-dulcis-model-model2303050001-model, metabolism-sbml-mosca2012-central-carbon-metabolism-regulated-by-biomd0000000426-model, metabolism-sbml-mulquiney1999-bpg-metabolism-model5950552398-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
