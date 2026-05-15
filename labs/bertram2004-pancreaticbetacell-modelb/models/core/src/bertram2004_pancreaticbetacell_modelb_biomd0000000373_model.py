# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Bertram2004_PancreaticBetaCell_modelB."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bertram2004PancreaticbetacellModelbBiomd0000000373Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Bertram2004_PancreaticBetaCell_modelB."""

    _SBML_ID = 'BIOMD0000000373'
    _TITLE = 'Bertram2004_PancreaticBetaCell_modelB'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'V': 'pancreatic_metabolism_state_1', 'n': 'pancreatic_metabolism_state_2', 'c': 'pancreatic_metabolism_state_3', 'cer': 'pancreatic_metabolism_state_4', 'g6p': 'glucose_6_phosphate', 'fbp': 'fructose_bisphosphate', 'adp': 'adp'}
    _OBSERVABLES = ['V', 'n', 'c', 'cer', 'g6p', 'fbp', 'adp']
    _SPECIES_LABELS = {'V': 'Pancreatic Metabolism state 1', 'n': 'Pancreatic Metabolism state 2', 'c': 'Pancreatic Metabolism state 3', 'cer': 'Pancreatic Metabolism state 4', 'g6p': 'Glucose 6 Phosphate', 'fbp': 'Fructose Bisphosphate', 'adp': 'ADP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pancreatic_metabolism_state_1': ('V', -60.0, 'native SBML value', 'Initial condition for pancreatic metabolism state 1. Maps to bundled SBML symbol `V`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pancreatic_metabolism_state_2': ('n', 0.025, 'native SBML value', 'Initial condition for pancreatic metabolism state 2. Maps to bundled SBML symbol `n`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pancreatic_metabolism_state_3': ('c', 0.25, 'native SBML value', 'Initial condition for pancreatic metabolism state 3. Maps to bundled SBML symbol `c`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pancreatic_metabolism_state_4': ('cer', 185.0, 'native SBML value', 'Initial condition for pancreatic metabolism state 4. Maps to bundled SBML symbol `cer`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('g6p', 200.0, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `g6p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'pancreatic_metabolism_state_1': ('V', 'native SBML value', 'Pancreatic Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `V`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'pancreatic_metabolism_state_2': ('n', 'native SBML value', 'Pancreatic Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `n`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'pancreatic_metabolism_state_3': ('c', 'native SBML value', 'Pancreatic Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `c`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'pancreatic_metabolism_state_4': ('cer', 'native SBML value', 'Pancreatic Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `cer`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glucose_6_phosphate': ('g6p', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `g6p`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000373.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
