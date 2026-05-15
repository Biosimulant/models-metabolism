# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Aubert2002 - Coupling between Brain electrical activity, Metabolism and Hemodynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aubert2002CouplingBetweenBrainElectricalActBiomd0000000570Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Aubert2002 - Coupling between Brain electrical activity, Metabolism and Hemodynamics."""

    _SBML_ID = 'BIOMD0000000570'
    _TITLE = 'Aubert2002 - Coupling between Brain electrical activity, Metabolism and Hemodynamics'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'species_1': 'brain_energy_state_1', 'species_4': 'glucose', 'species_5': 'glyceraldehyde_3_phosphate', 'species_7': 'nadh', 'species_8': 'pyruvate', 'species_9': 'phosphoenolpyruvate', 'species_10': 'lactate', 'species_11': 'brain_energy_state_8', 'species_13': 'brain_energy_state_9', 'species_17': 'glucose_2', 'species_18': 'lactate_2', 'species_19': 'brain_energy_state_12', 'dHb': 'brain_energy_state_13'}
    _OBSERVABLES = ['species_1', 'species_4', 'species_5', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_13', 'species_17', 'species_18', 'species_19', 'dHb']
    _SPECIES_LABELS = {'species_1': 'Brain Energy state 1', 'species_4': 'glucose', 'species_5': 'glyceraldehyde 3 phosphate', 'species_7': 'NADH', 'species_8': 'pyruvate', 'species_9': 'phosphoenolpyruvate', 'species_10': 'lactate', 'species_11': 'Brain Energy state 8', 'species_13': 'Brain Energy state 9', 'species_17': 'glucose 2', 'species_18': 'lactate 2', 'species_19': 'Brain Energy state 12', 'dHb': 'Brain Energy state 13'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_brain_energy_state_1': ('species_1', 15.0, 'native SBML value', 'Initial condition for brain energy state 1. Maps to bundled SBML symbol `species_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose': ('species_4', 1.2, 'native SBML value', 'Initial condition for glucose. Maps to bundled SBML symbol `species_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glyceraldehyde_3_phosphate': ('species_5', 0.0057, 'native SBML value', 'Initial condition for glyceraldehyde 3 phosphate. Maps to bundled SBML symbol `species_5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nadh': ('species_7', 0.026, 'native SBML value', 'Initial condition for nadh. Maps to bundled SBML symbol `species_7`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pyruvate': ('species_8', 0.16, 'native SBML value', 'Initial condition for pyruvate. Maps to bundled SBML symbol `species_8`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'brain_energy_state_1': ('species_1', 'native SBML value', 'Brain Energy state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glucose': ('species_4', 'native SBML value', 'glucose. Maps to SBML symbol `species_4`.'), 'glyceraldehyde_3_phosphate': ('species_5', 'native SBML value', 'glyceraldehyde 3 phosphate. Maps to SBML symbol `species_5`.'), 'nadh': ('species_7', 'native SBML value', 'NADH. Maps to SBML symbol `species_7`.'), 'pyruvate': ('species_8', 'native SBML value', 'pyruvate. Maps to SBML symbol `species_8`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000570.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
