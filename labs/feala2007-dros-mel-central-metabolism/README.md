# Feala2007_dros_mel_central_metabolism

Cleaned metabolism SBML ODE lab. The bundled SBML file remains the scientific source of truth.

Validation evidence: Tellurium loaded and simulated 188 floating species

## What You'll See

These dark-mode screenshots show the default Feala2007_dros_mel_central_metabolism run over 10 model-time units with outputs sampled every 1. The lab exposes 5 inputs (`initial_metabolic_pathway_state_1`, `initial_metabolic_pathway_state_2`, `initial_m_d_glycerate_2_phosphate_c3h4o7p`, `initial_metabolic_pathway_state_4`, `initial_metabolic_pathway_state_5`) and 8 outputs (`metabolic_pathway_state_1`, `metabolic_pathway_state_2`, `m_d_glycerate_2_phosphate_c3h4o7p`, `metabolic_pathway_state_4`, `metabolic_pathway_state_5`, and 3 more). The default input state includes `initial_metabolic_pathway_state_1`=`0`, `initial_metabolic_pathway_state_2`=`0`, `initial_m_d_glycerate_2_phosphate_c3h4o7p`=`0`, `initial_metabolic_pathway_state_4`=`0`. Model described in: Flexibility in energy metabolism supports hypoxia tolerance in Drosophila flight muscle: metabolomic and computational systems analysis. It can be used to explore metabolic flux dynamics and compare pathway behavior across conditions.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run interpretation table summarizes the configured Feala2007_dros_mel_central_metabolism simulation and its reported output statistics.

![Feala2007_dros_mel_central_metabolism Lab - run interpretation](assets/01-feala2007-dros-mel-central-metabolism-lab-run-interpretation.png)

The observable dynamics plot traces the main reported outputs over the captured run window, including `metabolic_pathway_state_1`, `metabolic_pathway_state_2`, `m_d_glycerate_2_phosphate_c3h4o7p`, `metabolic_pathway_state_4`, and 4 more.

![Feala2007_dros_mel_central_metabolism observable dynamics](assets/02-feala2007-dros-mel-central-metabolism-observable-dynamics.png)

The largest-observable-excursions chart ranks which reported variables moved the most during this simulation.

![Largest observable excursions](assets/03-largest-observable-excursions.png)

The phase-relationship plot compares paired observable values to show how the dominant trajectories move relative to one another.

![Observable phase relationship](assets/04-observable-phase-relationship.png)

<!-- BIOSIMULANT_VISUALS_END -->
