# Space Prompt - metabolism-general-combo-0057

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-feist2014-geobacter-metallireducens-gs-15-metabo-model2204190002-model, metabolism-sbml-ford2020-whole-body-vitamin-a-metabolism-in-huma-model2312190001-model, metabolism-sbml-furr2005-whole-body-vitamin-a-metabolism-in-huma-model2405200001-model, metabolism-sbml-gebauer2016-genome-scale-model-of-caenorhabditis-model1704200000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
