# Space Prompt - metabolism-general-combo-0065

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-nijhout2006-hepatic-folate-metab-model1007200000-model, metabolism-sbml-norman2019-genome-scale-model-of-clostridium-aut-model1810120001-model, metabolism-sbml-odea2007-a-homeostatic-model-of-i-b-metabolism-t-model1908270002-model, metabolism-sbml-odea2007-ikappab-biomd0000000147-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
