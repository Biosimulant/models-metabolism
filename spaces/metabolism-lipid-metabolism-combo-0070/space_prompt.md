# Space Prompt - metabolism-lipid-metabolism-combo-0070

Create a scientifically coherent **metabolism / lipid_metabolism** comparative space using:
- Base models: metabolism-sbml-gupta2009-eicosanoid-metabolism-biomd0000000436-model, metabolism-sbml-mcauley2012-whole-body-cholesterol-metabolism-biomd0000000434-model, metabolism-sbml-morgan2016-dynamics-of-cholesterol-metabolism-an-model1508170000-model, metabolism-sbml-sips2015-glucose-and-non-esterified-fatty-acids-model1806080001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
