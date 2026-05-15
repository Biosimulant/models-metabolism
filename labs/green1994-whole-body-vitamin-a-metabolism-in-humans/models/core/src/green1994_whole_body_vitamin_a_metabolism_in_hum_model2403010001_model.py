# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Green1994 - whole-body vitamin A metabolism in humans."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Green1994WholeBodyVitaminAMetabolismInHumModel2403010001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Green1994 - whole-body vitamin A metabolism in humans."""

    _SBML_ID = 'MODEL2403010001'
    _TITLE = 'Green1994 - whole-body vitamin A metabolism in humans'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'M_1': 'vitamin_a_metabolism_state_1', 'M_2': 'vitamin_a_metabolism_state_2', 'M_3': 'vitamin_a_metabolism_state_3', 'M_1_0': 'vitamin_a_metabolism_state_4', 'M_2_0': 'vitamin_a_metabolism_state_5', 'M_3_0': 'vitamin_a_metabolism_state_6'}
    _OBSERVABLES = ['M_1', 'M_2', 'M_3', 'M_1_0', 'M_2_0', 'M_3_0']
    _SPECIES_LABELS = {'M_1': 'Vitamin A Metabolism state 1', 'M_2': 'Vitamin A Metabolism state 2', 'M_3': 'Vitamin A Metabolism state 3', 'M_1_0': 'Vitamin A Metabolism state 4', 'M_2_0': 'Vitamin A Metabolism state 5', 'M_3_0': 'Vitamin A Metabolism state 6'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_vitamin_a_metabolism_state_1': ('M_1', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 1. Maps to bundled SBML symbol `M_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_2': ('M_2', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 2. Maps to bundled SBML symbol `M_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_3': ('M_3', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 3. Maps to bundled SBML symbol `M_3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_4': ('M_1_0', 1.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 4. Maps to bundled SBML symbol `M_1_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_vitamin_a_metabolism_state_5': ('M_2_0', 0.0, 'native SBML value', 'Initial condition for vitamin a metabolism state 5. Maps to bundled SBML symbol `M_2_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'vitamin_a_metabolism_state_1': ('M_1', 'native SBML value', 'Vitamin A Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_2': ('M_2', 'native SBML value', 'Vitamin A Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_3': ('M_3', 'native SBML value', 'Vitamin A Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_4': ('M_1_0', 'native SBML value', 'Vitamin A Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_1_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'vitamin_a_metabolism_state_5': ('M_2_0', 'native SBML value', 'Vitamin A Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `M_2_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2403010001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
