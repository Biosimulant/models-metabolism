# Babaev2024 - CYP2C9 variants

Cleaned metabolism SBML ODE lab. The bundled SBML file remains the scientific source of truth.

Validation evidence: Tellurium loaded and simulated 7 floating species

## What You'll See

These dark-mode screenshots show the default Babaev2024 - CYP2C9 variants run over 10 model-time units with outputs sampled every 1. The lab exposes 5 inputs (`initial_drug_metabolite_e3174`, `initial_drug_metabolite_e3174_2`, `initial_drug_metabolism_state_3`, `initial_drug_metabolism_state_4`, `initial_drug_metabolism_state_5_extracellular`) and 8 outputs (`drug_metabolite_e3174`, `drug_metabolite_e3174_2`, `drug_metabolism_state_3`, `drug_metabolism_state_4`, `drug_metabolism_state_5_extracellular`, and 3 more). The default input state includes `initial_drug_metabolite_e3174`=`0`, `initial_drug_metabolite_e3174_2`=`0`, `initial_drug_metabolism_state_3`=`0`, `initial_drug_metabolism_state_4`=`0`. Modified model of losartan metabolism (Karatza and Karalis, 2020) incorporating different allelic variants of CYP2C9. It can be used to explore metabolic flux dynamics and compare pathway behavior across conditions.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run interpretation table summarizes the configured Babaev2024 - CYP2C9 variants simulation and its reported output statistics.

![Babaev2024 - CYP2C9 variants Lab - run interpretation](assets/01-babaev2024-cyp2c9-variants-lab-run-interpretation.png)

The observable dynamics plot traces the main reported outputs over the captured run window, including `drug_metabolite_e3174`, `drug_metabolite_e3174_2`, `drug_metabolism_state_3`, `drug_metabolism_state_4`, and 4 more.

![Babaev2024 - CYP2C9 variants observable dynamics](assets/02-babaev2024-cyp2c9-variants-observable-dynamics.png)

The largest-observable-excursions chart ranks which reported variables moved the most during this simulation.

![Largest observable excursions](assets/03-largest-observable-excursions.png)

The phase-relationship plot compares paired observable values to show how the dominant trajectories move relative to one another.

![Observable phase relationship](assets/04-observable-phase-relationship.png)

<!-- BIOSIMULANT_VISUALS_END -->
