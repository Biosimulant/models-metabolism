# Space Prompt - metabolism-general-combo-0060

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-jallet2024-idj1518-genome-scale-model-of-ethanol-model2403010003-model, metabolism-sbml-jallet2024-isotopic-model-of-ethanolamine-metabo-model2403010002-model, metabolism-sbml-jensen2020-streptococcus-oralis-icj415-biomd0000001086-model, metabolism-sbml-jeon2018-enzyme-clustering-in-glucose-metabolism-biomd0000001055-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
