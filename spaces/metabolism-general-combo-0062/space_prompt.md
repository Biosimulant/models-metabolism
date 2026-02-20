# Space Prompt - metabolism-general-combo-0062

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-kurpad-2023-vitamin-b12-metabolism-in-humans-stu-model2503310002-model, metabolism-sbml-lai2007-o2-transport-metabolism-biomd0000000248-model, metabolism-sbml-lavoie2020-f-cylindrus-genome-scale-model-model2001280001-model, metabolism-sbml-lee2017-paracetamol-first-pass-metabolism-pk-mod-biomd0000000947-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
