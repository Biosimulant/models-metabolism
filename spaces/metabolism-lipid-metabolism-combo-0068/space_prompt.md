# Space Prompt - metabolism-lipid-metabolism-combo-0068

Create a scientifically coherent **metabolism / lipid_metabolism** comparative space using:
- Base models: metabolism-sbml-davies2023-cholesterol-metabolism-and-atheroscle-model2306300001-model, metabolism-sbml-gupta2009-eicosanoid-metabolism-biomd0000000436-model, metabolism-sbml-mcauley2012-whole-body-cholesterol-metabolism-biomd0000000434-model, metabolism-sbml-morgan2016-dynamics-of-cholesterol-metabolism-an-model1508170000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
