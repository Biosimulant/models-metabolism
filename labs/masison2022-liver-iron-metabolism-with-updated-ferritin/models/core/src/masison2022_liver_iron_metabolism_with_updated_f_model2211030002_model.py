# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Masison2022 - Liver Iron Metabolism with updated ferritin."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Masison2022LiverIronMetabolismWithUpdatedFModel2211030002Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Masison2022 - Liver Iron Metabolism with updated ferritin."""

    _SBML_ID = 'MODEL2211030002'
    _TITLE = 'Masison2022 - Liver Iron Metabolism with updated ferritin'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'species_7': 'iron_metabolism_state_1', 'species_1': 'iron_metabolism_state_2', 'species_5': 'iron_metabolism_state_3', 'species_2': 'iron_metabolism_state_4', 'species_4': 'iron_metabolism_state_5', 'species_6': 'iron_metabolism_state_6', 'species_3': 'iron_metabolism_state_7', 'species_12': 'iron_metabolism_state_8', 'species_8': 'iron_metabolism_state_9', 'species_9': 'iron_metabolism_state_10', 'species_15': 'iron_metabolism_state_11', 'species_16': 'iron_metabolism_state_12', 'species_17': 'iron_metabolism_state_13', 'species_18': 'iron_metabolism_state_14', 'species_19': 'iron_metabolism_state_15', 'species_10': 'iron_metabolism_state_16', 'core': 'iron_metabolism_state_17', 'FT_cage': 'iron_metabolism_state_18', 'DFP': 'iron_metabolism_state_19'}
    _OBSERVABLES = ['species_7', 'species_1', 'species_5', 'species_2', 'species_4', 'species_6', 'species_3', 'species_12', 'species_8', 'species_9', 'species_15', 'species_16', 'species_17', 'species_18', 'species_19', 'species_10', 'core', 'FT_cage', 'DFP']
    _SPECIES_LABELS = {'species_7': 'Iron Metabolism state 1', 'species_1': 'Iron Metabolism state 2', 'species_5': 'Iron Metabolism state 3', 'species_2': 'Iron Metabolism state 4', 'species_4': 'Iron Metabolism state 5', 'species_6': 'Iron Metabolism state 6', 'species_3': 'Iron Metabolism state 7', 'species_12': 'Iron Metabolism state 8', 'species_8': 'Iron Metabolism state 9', 'species_9': 'Iron Metabolism state 10', 'species_15': 'Iron Metabolism state 11', 'species_16': 'Iron Metabolism state 12', 'species_17': 'Iron Metabolism state 13', 'species_18': 'Iron Metabolism state 14', 'species_19': 'Iron Metabolism state 15', 'species_10': 'Iron Metabolism state 16', 'core': 'Iron Metabolism state 17', 'FT_cage': 'Iron Metabolism state 18', 'DFP': 'Iron Metabolism state 19'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_iron_metabolism_state_1': ('species_7', 1.13750420250257e-08, 'native SBML value', 'Initial condition for iron metabolism state 1. Maps to bundled SBML symbol `species_7`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_metabolism_state_2': ('species_1', 5.53114277751551e-11, 'native SBML value', 'Initial condition for iron metabolism state 2. Maps to bundled SBML symbol `species_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_metabolism_state_3': ('species_5', 4.81985997445553e-09, 'native SBML value', 'Initial condition for iron metabolism state 3. Maps to bundled SBML symbol `species_5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_metabolism_state_4': ('species_2', 4.91004767574587e-06, 'native SBML value', 'Initial condition for iron metabolism state 4. Maps to bundled SBML symbol `species_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_metabolism_state_5': ('species_4', 4.04747006186017e-06, 'native SBML value', 'Initial condition for iron metabolism state 5. Maps to bundled SBML symbol `species_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'iron_metabolism_state_1': ('species_7', 'native SBML value', 'Iron Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_7`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'iron_metabolism_state_2': ('species_1', 'native SBML value', 'Iron Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'iron_metabolism_state_3': ('species_5', 'native SBML value', 'Iron Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_5`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'iron_metabolism_state_4': ('species_2', 'native SBML value', 'Iron Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'iron_metabolism_state_5': ('species_4', 'native SBML value', 'Iron Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_4`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2211030002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
