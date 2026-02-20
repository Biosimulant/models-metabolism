# Space Prompt - metabolism-general-combo-0051

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-cloutier2009-energymetabolism-modelf-model1006230096-model, metabolism-sbml-costa2014-computational-model-of-l-lactis-metabo-biomd0000000572-model, metabolism-sbml-costa2015-central-metabolism-of-e-coli-extended-model1504080006-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
