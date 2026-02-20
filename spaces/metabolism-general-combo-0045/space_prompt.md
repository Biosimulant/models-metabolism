# Space Prompt - metabolism-general-combo-0045

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-adams2019-the-regulatory-role-of-shikimate-in-pl-biomd0000000847-model, metabolism-sbml-aubert2002-coupling-between-brain-electrical-act-biomd0000000570-model, metabolism-sbml-aubert2005-interaction-between-astrocytes-and-ne-model1411210000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
