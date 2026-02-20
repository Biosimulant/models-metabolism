# Space Prompt - metabolism-general-combo-0046

Create a scientifically coherent **metabolism / general** comparative space using:
- Base models: metabolism-sbml-babaev2024-cyp2c9-variants-model2412180002-model, metabolism-sbml-babaev2025-cyp2c9-and-abcb1-losartan-metabolism-model2504020001-model, metabolism-sbml-bannerman2022-whole-genome-metabolism-m-abscessu-model2203300002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
