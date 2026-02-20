# Space Prompt - metabolism-general-combo-0047

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-bannerman2022-whole-genome-metabolism-mycobacter-model2203300001-model, metabolism-sbml-bulik2016-regulation-of-hepatic-glucose-metaboli-biomd0000000633-model, metabolism-sbml-canto-encalada2022-fba-of-simultaneous-degradati-biomd0000001061-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
