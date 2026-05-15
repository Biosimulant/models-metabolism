# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Mosca2012 - Central Carbon Metabolism Regulated by AKT."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mosca2012CentralCarbonMetabolismRegulatedByBiomd0000000426Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Mosca2012 - Central Carbon Metabolism Regulated by AKT."""

    _SBML_ID = 'BIOMD0000000426'
    _TITLE = 'Mosca2012 - Central Carbon Metabolism Regulated by AKT'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'species_1': 'glucose', 'species_2': 'glucose_6_phosphate', 'species_4': 'atp', 'species_5': 'fructose_6_phosphate', 'species_6': 'fructose_1_6_bisphosphate', 'species_7': 'e4p', 'species_8': 'glycolysis_state_7', 'species_11': 'nadph', 'species_12': 'glycolysis_state_9', 'species_13': 'ru5p', 'species_14': 'x5p', 'species_15': 'r5p', 'species_16': 'glyceraldehyde_3_phosphate', 'species_17': 's7p', 'species_19': 'nad', 'species_22': 'g1p', 'species_27': 'glycolysis_state_17', 'species_28': 'pg3', 'species_29': 'pg2', 'species_30': 'phosphoenolpyruvate', 'species_31': 'pyruvate'}
    _OBSERVABLES = ['species_1', 'species_2', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_11', 'species_12', 'species_13', 'species_14', 'species_15', 'species_16', 'species_17', 'species_19', 'species_22', 'species_27', 'species_28', 'species_29', 'species_30', 'species_31']
    _SPECIES_LABELS = {'species_1': 'glucose', 'species_2': 'glucose 6 phosphate', 'species_4': 'ATP', 'species_5': 'fructose 6 phosphate', 'species_6': 'fructose 1 6 bisphosphate', 'species_7': 'E4p', 'species_8': 'Glycolysis state 7', 'species_11': 'NADPH', 'species_12': 'Glycolysis state 9', 'species_13': 'Ru5p', 'species_14': 'X5p', 'species_15': 'R5p', 'species_16': 'glyceraldehyde 3 phosphate', 'species_17': 'S7p', 'species_19': 'NAD', 'species_22': 'G1p', 'species_27': 'Glycolysis state 17', 'species_28': 'Pg3', 'species_29': 'Pg2', 'species_30': 'phosphoenolpyruvate', 'species_31': 'pyruvate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose': ('species_1', 0.000897, 'native SBML value', 'Initial condition for glucose. Maps to bundled SBML symbol `species_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('species_2', 0.00109, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `species_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('species_4', 0.0087, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `species_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('species_5', 3.62e-05, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `species_5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_1_6_bisphosphate': ('species_6', 0.000367, 'native SBML value', 'Initial condition for fructose 1 6 bisphosphate. Maps to bundled SBML symbol `species_6`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glucose': ('species_1', 'native SBML value', 'glucose. Maps to SBML symbol `species_1`.'), 'glucose_6_phosphate': ('species_2', 'native SBML value', 'glucose 6 phosphate. Maps to SBML symbol `species_2`.'), 'atp': ('species_4', 'native SBML value', 'ATP. Maps to SBML symbol `species_4`.'), 'fructose_6_phosphate': ('species_5', 'native SBML value', 'fructose 6 phosphate. Maps to SBML symbol `species_5`.'), 'fructose_1_6_bisphosphate': ('species_6', 'native SBML value', 'fructose 1 6 bisphosphate. Maps to SBML symbol `species_6`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000426.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
