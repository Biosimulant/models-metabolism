# Space Prompt - metabolism-central-carbon-combo-0073

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-abymbel891-strain-specific-genome-scale-metaboli-model2406250010-model, metabolism-sbml-achcar2012-glycolysis-in-bloodstream-form-t-bruc-biomd0000000428-model, metabolism-sbml-agora-strain-specific-genome-scale-metabolic-mod-model2406250011-model, metabolism-sbml-ahmad2017-genome-scale-metabolic-model-igt736-of-model1703060000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
