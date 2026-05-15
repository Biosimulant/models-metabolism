# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Sokol2025 - Kinetic model of the first three reactions of glycolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sokol2025KineticModelOfTheFirstThreeReactModel2502210002Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Sokol2025 - Kinetic model of the first three reactions of glycolysis."""

    _SBML_ID = 'MODEL2502210002'
    _TITLE = 'Sokol2025 - Kinetic model of the first three reactions of glycolysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ADP': 'adp', 'ATP': 'atp', 'G6P': 'glucose_6_phosphate', 'GLC': 'glucose', 'F6P': 'fructose_6_phosphate', 'FBP': 'fructose_bisphosphate'}
    _OBSERVABLES = ['ADP', 'ATP', 'G6P', 'GLC', 'F6P', 'FBP']
    _SPECIES_LABELS = {'ADP': 'ADP', 'ATP': 'ATP', 'G6P': 'Glucose 6 Phosphate', 'GLC': 'Glucose', 'F6P': 'Fructose 6 Phosphate', 'FBP': 'Fructose Bisphosphate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('ADP', 1.02876420481711e-06, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 24.9999838070557, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 0.125387382474129, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose': ('GLC', 5.1381410880857, 'native SBML value', 'Initial condition for glucose. Maps to bundled SBML symbol `GLC`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('F6P', 0.999998114992648, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'glucose': ('GLC', 'native SBML value', 'Glucose. Maps to SBML symbol `GLC`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.')}

    def __init__(self, model_path: str = 'data/MODEL2502210002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
