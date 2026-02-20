# Space Prompt - metabolism-general-combo-0052

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-costa2015-central-metabolism-of-e-coli-non-regul-model1504080005-model, metabolism-sbml-costa2015-central-metabolism-of-e-coli-regulated-model1504080004-model, metabolism-sbml-curien2009-aspartate-metabolism-biomd0000000212-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
