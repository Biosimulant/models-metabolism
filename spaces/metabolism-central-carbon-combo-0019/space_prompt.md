# Space Prompt - metabolism-central-carbon-combo-0019

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-bertram2004-pancreaticbetacell-modelb-biomd0000000373-model, metabolism-sbml-bertram2007-isletcell-oscillations-biomd0000000376-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
