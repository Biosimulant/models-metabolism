# Space Prompt - metabolism-general-combo-0048

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-chedere2022-nad-biosynthesis-in-human-liver-model2205250001-model, metabolism-sbml-choudhary2016-epithelial-to-mesenchymal-transiti-model1602080000-model, metabolism-sbml-cifelli2008-whole-body-vitamin-a-metabolism-in-h-model2403080002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
