# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Green1985 - whole-body vitamin A metabolism in rats."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Green1985WholeBodyVitaminAMetabolismInRatModel2311220001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Green1985 - whole-body vitamin A metabolism in rats."""

    _SBML_ID = 'MODEL2311220001'
    _TITLE = 'Green1985 - whole-body vitamin A metabolism in rats'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'M_11': 'vitamin_a_metabolism_state_1', 'M_21': 'vitamin_a_metabolism_state_2', 'M_2': 'vitamin_a_metabolism_state_3', 'M_3': 'vitamin_a_metabolism_state_4', 'M_5': 'vitamin_a_metabolism_state_5', 'M_13': 'vitamin_a_metabolism_state_6', 'M_14': 'vitamin_a_metabolism_state_7', 'M_16': 'vitamin_a_metabolism_state_8', 'M_17': 'vitamin_a_metabolism_state_9', 'M_11_0': 'vitamin_a_metabolism_state_10', 'M_21_0': 'vitamin_a_metabolism_state_11', 'M_2_0': 'vitamin_a_metabolism_state_12', 'M_3_0': 'vitamin_a_metabolism_state_13', 'M_5_0': 'vitamin_a_metabolism_state_14', 'M_13_0': 'vitamin_a_metabolism_state_15', 'M_14_0': 'vitamin_a_metabolism_state_16', 'M_16_0': 'vitamin_a_metabolism_state_17', 'M_17_0': 'vitamin_a_metabolism_state_18'}
    _OBSERVABLES = ['M_11', 'M_21', 'M_2', 'M_3', 'M_5', 'M_13', 'M_14', 'M_16', 'M_17', 'M_11_0', 'M_21_0', 'M_2_0', 'M_3_0', 'M_5_0', 'M_13_0', 'M_14_0', 'M_16_0', 'M_17_0']
    _SPECIES_LABELS = {'M_11': 'Vitamin A Metabolism state 1', 'M_21': 'Vitamin A Metabolism state 2', 'M_2': 'Vitamin A Metabolism state 3', 'M_3': 'Vitamin A Metabolism state 4', 'M_5': 'Vitamin A Metabolism state 5', 'M_13': 'Vitamin A Metabolism state 6', 'M_14': 'Vitamin A Metabolism state 7', 'M_16': 'Vitamin A Metabolism state 8', 'M_17': 'Vitamin A Metabolism state 9', 'M_11_0': 'Vitamin A Metabolism state 10', 'M_21_0': 'Vitamin A Metabolism state 11', 'M_2_0': 'Vitamin A Metabolism state 12', 'M_3_0': 'Vitamin A Metabolism state 13', 'M_5_0': 'Vitamin A Metabolism state 14', 'M_13_0': 'Vitamin A Metabolism state 15', 'M_14_0': 'Vitamin A Metabolism state 16', 'M_16_0': 'Vitamin A Metabolism state 17', 'M_17_0': 'Vitamin A Metabolism state 18'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_vitamin_a_metabolism_state_1': ('M_11', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 1. Maps to bundled SBML symbol `M_11`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_2': ('M_21', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 2. Maps to bundled SBML symbol `M_21`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_3': ('M_2', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 3. Maps to bundled SBML symbol `M_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_4': ('M_3', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 4. Maps to bundled SBML symbol `M_3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_5': ('M_5', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 5. Maps to bundled SBML symbol `M_5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'vitamin_a_metabolism_state_1': ('M_11', 'native SBML value', 'Vitamin A Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_11`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_2': ('M_21', 'native SBML value', 'Vitamin A Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_21`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_3': ('M_2', 'native SBML value', 'Vitamin A Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_4': ('M_3', 'native SBML value', 'Vitamin A Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_5': ('M_5', 'native SBML value', 'Vitamin A Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_5`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2311220001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
