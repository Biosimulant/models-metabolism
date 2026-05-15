# Piedrafita2010_MR_System

Cleaned metabolism SBML ODE lab. The bundled SBML file remains the scientific source of truth.

Validation evidence: Tellurium loaded and simulated 8 floating species

## What You'll See

These dark-mode screenshots show the default Piedrafita2010_MR_System run over 10 model-time units with outputs sampled every 1. The lab exposes 5 inputs (`initial_metabolic_pathway_state_1`, `initial_metabolic_pathway_state_2`, `initial_metabolic_pathway_state_3`, `initial_metabolic_pathway_state_4`, `initial_metabolic_pathway_state_5`) and 8 outputs (`metabolic_pathway_state_1`, `metabolic_pathway_state_2`, `metabolic_pathway_state_3`, `metabolic_pathway_state_4`, `metabolic_pathway_state_5`, and 3 more). The default input state includes `initial_metabolic_pathway_state_1`=`5`, `initial_metabolic_pathway_state_2`=`0`, `initial_metabolic_pathway_state_3`=`0`, `initial_metabolic_pathway_state_4`=`0`. This is the self maintaining metabolism model described in the article: A Simple Self-Maintaining Metabolic System: Robustness, Autocatalysis, Bistability. Piedrafita G, Montero F, Morán F, Cárdenas M.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run interpretation table summarizes the configured Piedrafita2010_MR_System simulation and its reported output statistics.

![Piedrafita2010_MR_System Lab - run interpretation](assets/01-piedrafita2010-mr-system-lab-run-interpretation.png)

The observable dynamics plot traces the main reported outputs over the captured run window, including `metabolic_pathway_state_1`, `metabolic_pathway_state_2`, `metabolic_pathway_state_3`, `metabolic_pathway_state_4`, and 4 more.

![Piedrafita2010_MR_System observable dynamics](assets/02-piedrafita2010-mr-system-observable-dynamics.png)

The largest-observable-excursions chart ranks which reported variables moved the most during this simulation.

![Largest observable excursions](assets/03-largest-observable-excursions.png)

The phase-relationship plot compares paired observable values to show how the dominant trajectories move relative to one another.

![Observable phase relationship](assets/04-observable-phase-relationship.png)

<!-- BIOSIMULANT_VISUALS_END -->
