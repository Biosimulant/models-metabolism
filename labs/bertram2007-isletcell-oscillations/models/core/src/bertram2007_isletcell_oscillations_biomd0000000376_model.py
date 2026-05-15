# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Bertram2007_IsletCell_Oscillations."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bertram2007IsletcellOscillationsBiomd0000000376Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Bertram2007_IsletCell_Oscillations."""

    _SBML_ID = 'BIOMD0000000376'
    _TITLE = 'Bertram2007_IsletCell_Oscillations'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Vm': 'pancreatic_metabolism_state_1', 'n': 'pancreatic_metabolism_state_2', 'G6P': 'glucose_6_phosphate', 'FBP': 'fructose_bisphosphate', 'NADHm': 'mitochondrial_nadh', 'delta_psi': 'pancreatic_metabolism_state_6', 'Cam': 'mitochondrial_ca', 'ADPm': 'mitochondrial_adp', 'adp': 'adp', 'c': 'pancreatic_metabolism_state_10', 'Caer': 'pancreatic_metabolism_state_11'}
    _OBSERVABLES = ['Vm', 'n', 'G6P', 'FBP', 'NADHm', 'delta_psi', 'Cam', 'ADPm', 'adp', 'c', 'Caer']
    _SPECIES_LABELS = {'Vm': 'Pancreatic Metabolism state 1', 'n': 'Pancreatic Metabolism state 2', 'G6P': 'Glucose 6 Phosphate', 'FBP': 'Fructose Bisphosphate', 'NADHm': 'Mitochondrial NADH', 'delta_psi': 'Pancreatic Metabolism state 6', 'Cam': 'Mitochondrial CA', 'ADPm': 'Mitochondrial ADP', 'adp': 'ADP', 'c': 'Pancreatic Metabolism state 10', 'Caer': 'Pancreatic Metabolism state 11'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pancreatic_metabolism_state_1': ('Vm', -60.0, 'native SBML value', 'Initial condition for pancreatic metabolism state 1. Maps to bundled SBML symbol `Vm`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pancreatic_metabolism_state_2': ('n', 0.0, 'native SBML value', 'Initial condition for pancreatic metabolism state 2. Maps to bundled SBML symbol `n`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 301.0, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_bisphosphate': ('FBP', 2.16, 'native SBML value', 'Initial condition for fructose bisphosphate. Maps to bundled SBML symbol `FBP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_mitochondrial_nadh': ('NADHm', 0.4, 'native SBML value', 'Initial condition for mitochondrial nadh. Maps to bundled SBML symbol `NADHm`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'pancreatic_metabolism_state_1': ('Vm', 'native SBML value', 'Pancreatic Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Vm`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'pancreatic_metabolism_state_2': ('n', 'native SBML value', 'Pancreatic Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `n`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'fructose_bisphosphate': ('FBP', 'native SBML value', 'Fructose Bisphosphate. Maps to SBML symbol `FBP`.'), 'mitochondrial_nadh': ('NADHm', 'native SBML value', 'Mitochondrial NADH. Maps to SBML symbol `NADHm`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000376.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
