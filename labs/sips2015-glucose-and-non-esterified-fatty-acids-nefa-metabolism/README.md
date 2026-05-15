# Sips2015 - Glucose and non-esterified fatty acids (NEFA) metabolism

Cleaned metabolism SBML ODE lab. The bundled SBML file remains the scientific source of truth.

Validation evidence: Tellurium loaded and simulated 20 floating species

## What You'll See

These dark-mode screenshots show the default Sips2015 - Glucose and non-esterified fatty acids (NEFA) metabolism run over 10 model-time units with outputs sampled every 1. The lab exposes 5 inputs (`initial_glycolysis_state_1`, `initial_glycolysis_state_2`, `initial_glycolysis_state_3`, `initial_glycolysis_state_4`, `initial_glycolysis_state_5`) and 8 outputs (`glycolysis_state_1`, `glycolysis_state_2`, `glycolysis_state_3`, `glycolysis_state_4`, `glycolysis_state_5`, and 3 more). The default input state includes `initial_glycolysis_state_1`=`0.0982882779338853`, `initial_glycolysis_state_2`=`0.245720694834713`, `initial_glycolysis_state_3`=`0.64712`, `initial_glycolysis_state_4`=`-1.55`. This a model from the article: Model-Based Quantification of the Systemic Interplay between Glucose and Fatty Acids in the Postprandial State. It can be used to explore metabolic flux dynamics and compare pathway behavior across conditions.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run interpretation table summarizes the configured Sips2015 - Glucose and non-esterified fatty acids (NEFA) metabolism simulation and its reported output statistics.

![Sips2015 - Glucose and non-esterified fatty acids (NEFA) metabolism Lab - run interpretation](assets/01-sips2015-glucose-and-non-esterified-fatty-acids-nefa-metabolism-lab-run-interpre.png)

The observable dynamics plot traces the main reported outputs over the captured run window, including `glycolysis_state_1`, `glycolysis_state_2`, `glycolysis_state_3`, `glycolysis_state_4`, and 4 more.

![Sips2015 - Glucose and non-esterified fatty acids (NEFA) metabolism observable dynamics](assets/02-sips2015-glucose-and-non-esterified-fatty-acids-nefa-metabolism-observable-dynam.png)

The largest-observable-excursions chart ranks which reported variables moved the most during this simulation.

![Largest observable excursions](assets/03-largest-observable-excursions.png)

The phase-relationship plot compares paired observable values to show how the dominant trajectories move relative to one another.

![Observable phase relationship](assets/04-observable-phase-relationship.png)

<!-- BIOSIMULANT_VISUALS_END -->
