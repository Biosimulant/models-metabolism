# Space Prompt - metabolism-central-carbon-combo-0071

Create a scientifically coherent **metabolism / central_carbon** comparative space using:
- Base models: metabolism-sbml-a-genome-scale-metabolic-model-for-helicobacter-model2404260001-model, metabolism-sbml-abuoun2009-genome-scale-metabolic-network-of-sal-model1507180009-model, metabolism-sbml-abymbel891-strain-specific-genome-scale-metaboli-model2406250010-model, metabolism-sbml-achcar2012-glycolysis-in-bloodstream-form-t-bruc-biomd0000000428-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
