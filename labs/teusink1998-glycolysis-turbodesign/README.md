# Teusink1998_Glycolysis_TurboDesign

Cleaned metabolism SBML ODE lab. The bundled SBML file remains the scientific source of truth.

Validation evidence: Tellurium loaded and simulated 3 floating species

## What You'll See

These dark-mode screenshots show the default Teusink1998_Glycolysis_TurboDesign run over 10 model-time units with outputs sampled every 1. The lab exposes 3 inputs (`initial_hexose_monophosphate`, `initial_fructose_1_6_bisphosphate`, `initial_atp`) and 6 outputs (`hexose_monophosphate`, `fructose_1_6_bisphosphate`, `atp`, `observable_values`, `run_summary`, and 1 more). The default input state includes `initial_hexose_monophosphate`=`0.1`, `initial_fructose_1_6_bisphosphate`=`1`, `initial_atp`=`4`. This is the model described in the article: The danger of metabolic pathways with turbo design Teusink B, Walsh MC, van Dam K, Westerhoff HV Trends Biochem. It can be used to explore metabolic flux dynamics and compare pathway behavior across conditions.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run interpretation table summarizes the configured Teusink1998_Glycolysis_TurboDesign simulation and its reported output statistics.

![Teusink1998_Glycolysis_TurboDesign Lab - run interpretation](assets/01-teusink1998-glycolysis-turbodesign-lab-run-interpretation.png)

The observable dynamics plot traces the main reported outputs over the captured run window, including `hexose_monophosphate`, `fructose_1_6_bisphosphate`, `atp`, `observable_values`, and 2 more.

![Teusink1998_Glycolysis_TurboDesign observable dynamics](assets/02-teusink1998-glycolysis-turbodesign-observable-dynamics.png)

The largest-observable-excursions chart ranks which reported variables moved the most during this simulation.

![Largest observable excursions](assets/03-largest-observable-excursions.png)

The phase-relationship plot compares paired observable values to show how the dominant trajectories move relative to one another.

![Observable phase relationship](assets/04-observable-phase-relationship.png)

<!-- BIOSIMULANT_VISUALS_END -->
