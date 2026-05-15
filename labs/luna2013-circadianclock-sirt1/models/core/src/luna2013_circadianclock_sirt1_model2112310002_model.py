# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Luna2013_CircadianClock_SIRT1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Luna2013CircadianclockSirt1Model2112310002Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Luna2013_CircadianClock_SIRT1."""

    _SBML_ID = 'MODEL2112310002'
    _TITLE = 'Luna2013_CircadianClock_SIRT1'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'species_1': 'metabolic_pathway_state_1', 'species_2': 'metabolic_pathway_state_2', 'species_3': 'metabolic_pathway_state_3', 'species_4': 'cp2', 'species_5': 'nad', 'species_6': 'metabolic_pathway_state_6', 'species_7': 'metabolic_pathway_state_7', 'species_11': 'metabolic_pathway_state_8', 'species_12': 'metabolic_pathway_state_9'}
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_11', 'species_12']
    _SPECIES_LABELS = {'species_1': 'Metabolic Pathway state 1', 'species_2': 'Metabolic Pathway state 2', 'species_3': 'Metabolic Pathway state 3', 'species_4': 'Cp2', 'species_5': 'NAD', 'species_6': 'Metabolic Pathway state 6', 'species_7': 'Metabolic Pathway state 7', 'species_11': 'Metabolic Pathway state 8', 'species_12': 'Metabolic Pathway state 9'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('species_1', 1.54597010260715, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `species_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('species_2', 0.101793613432364, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `species_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('species_3', 0.0723157888573554, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `species_3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_cp2': ('species_4', 0.0475926846633792, 'native SBML value', 'Initial condition for cp2. Maps to bundled SBML symbol `species_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad': ('species_5', 5.20806131539501, 'native SBML value', 'Initial condition for nad. Maps to bundled SBML symbol `species_5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('species_1', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('species_2', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('species_3', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'cp2': ('species_4', 'native SBML value', 'Cp2. Maps to SBML symbol `species_4`.'), 'nad': ('species_5', 'native SBML value', 'NAD. Maps to SBML symbol `species_5`.')}

    def __init__(self, model_path: str = 'data/MODEL2112310002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
