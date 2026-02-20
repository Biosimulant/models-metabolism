# Space Prompt - metabolism-general-combo-0053

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-curto1998-purine-metabolism-biomd0000000015-model, metabolism-sbml-czajka2024-lipomyces-genome-scale-model-model2403190001-model, metabolism-sbml-dalvigarcia2021-dopaminergic-and-serotonergic-ky-model2103060001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
