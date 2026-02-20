# Space Prompt - metabolism-general-combo-0067

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-reddyhoff2015-acetaminophen-metabolism-and-toxic-biomd0000000609-model, metabolism-sbml-reed2008-glutathione-metabolism-biomd0000000268-model, metabolism-sbml-reyes-palomares2012-a-combined-model-hepatic-pol-biomd0000000450-model, metabolism-sbml-reyes-palomares2012-a-combined-model-hepatic-pol-biomd0000000674-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
