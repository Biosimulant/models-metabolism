# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Teusink1998_Glycolysis_TurboDesign."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Teusink1998GlycolysisTurbodesignBiomd0000000253Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Teusink1998_Glycolysis_TurboDesign."""

    _SBML_ID = 'BIOMD0000000253'
    _TITLE = 'Teusink1998_Glycolysis_TurboDesign'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'HMP': 'hexose_monophosphate', 'Fru16P2': 'fructose_1_6_bisphosphate', 'ATP': 'atp'}
    _OBSERVABLES = ['HMP', 'Fru16P2', 'ATP']
    _SPECIES_LABELS = {'HMP': 'Hexose Monophosphate', 'Fru16P2': 'Fructose 1 6 Bisphosphate', 'ATP': 'ATP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_hexose_monophosphate': ('HMP', 0.1, 'native SBML value', 'Initial condition for hexose monophosphate. Maps to bundled SBML symbol `HMP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_1_6_bisphosphate': ('Fru16P2', 1.0, 'native SBML value', 'Initial condition for fructose 1 6 bisphosphate. Maps to bundled SBML symbol `Fru16P2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 4.0, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'hexose_monophosphate': ('HMP', 'native SBML value', 'Hexose Monophosphate. Maps to SBML symbol `HMP`.'), 'fructose_1_6_bisphosphate': ('Fru16P2', 'native SBML value', 'Fructose 1 6 Bisphosphate. Maps to SBML symbol `Fru16P2`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000253.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
