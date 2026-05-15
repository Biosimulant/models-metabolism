# Poolman2004_CalvinCycle

Cleaned metabolism SBML ODE lab. The bundled SBML file remains the scientific source of truth.

Validation evidence: Tellurium loaded and simulated 18 floating species

## What You'll See

These dark-mode screenshots show the default Poolman2004_CalvinCycle run over 10 model-time units with outputs sampled every 1. The lab exposes 5 inputs (`initial_metabolic_pathway_state_1`, `initial_metabolic_pathway_state_2`, `initial_metabolic_pathway_state_3`, `initial_metabolic_pathway_state_4`, `initial_metabolic_pathway_state_5`) and 8 outputs (`metabolic_pathway_state_1`, `metabolic_pathway_state_2`, `metabolic_pathway_state_3`, `metabolic_pathway_state_4`, `metabolic_pathway_state_5`, and 3 more). The default input state includes `initial_metabolic_pathway_state_1`=`0.33644`, `initial_metabolic_pathway_state_2`=`3.35479`, `initial_metabolic_pathway_state_3`=`0.49806`, `initial_metabolic_pathway_state_4`=`0.14825`. This a model from the article: Applications of metabolic modelling to plant metabolism. It can be used to explore metabolic flux dynamics and compare pathway behavior across conditions.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run interpretation table summarizes the configured Poolman2004_CalvinCycle simulation and its reported output statistics.

![Poolman2004_CalvinCycle Lab - run interpretation](assets/01-poolman2004-calvincycle-lab-run-interpretation.png)

The observable dynamics plot traces the main reported outputs over the captured run window, including `metabolic_pathway_state_1`, `metabolic_pathway_state_2`, `metabolic_pathway_state_3`, `metabolic_pathway_state_4`, and 4 more.

![Poolman2004_CalvinCycle observable dynamics](assets/02-poolman2004-calvincycle-observable-dynamics.png)

The largest-observable-excursions chart ranks which reported variables moved the most during this simulation.

![Largest observable excursions](assets/03-largest-observable-excursions.png)

The phase-relationship plot compares paired observable values to show how the dominant trajectories move relative to one another.

![Observable phase relationship](assets/04-observable-phase-relationship.png)

<!-- BIOSIMULANT_VISUALS_END -->
