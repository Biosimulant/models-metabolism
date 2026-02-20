# Space Prompt - metabolism-general-combo-0063

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-liu2019-clostridium-ljungdahlii-metabolism-model-model2204200003-model, metabolism-sbml-luna2013-circadianclock-sirt1-model2112310002-model, metabolism-sbml-masison2022-liver-iron-metabolism-with-updated-f-model2211030002-model, metabolism-sbml-mcdougal2017-metabolism-in-ischemic-cardiomyocyt-biomd0000000961-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
