# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Wolf2000 - Cellular interaction on glycolytic oscillations in yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wolf2000CellularInteractionOnGlycolyticOsciBiomd0000000691Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Wolf2000 - Cellular interaction on glycolytic oscillations in yeast."""

    _SBML_ID = 'BIOMD0000000691'
    _TITLE = 'Wolf2000 - Cellular interaction on glycolytic oscillations in yeast'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'S1__Cell_1_': 'glycolysis_state_1', 'S1__Cell_2_': 'glycolysis_state_2', 'S2__Cell_1_': 'glycolysis_state_3', 'S2__Cell_2_': 'glycolysis_state_4', 'S3__Cell_1_': 'glycolysis_state_5', 'S3__Cell_2_': 'glycolysis_state_6', 'S4__Cell_1_': 'glycolysis_state_7', 'S4__Cell_2_': 'glycolysis_state_8', 'N2__Cell_1_': 'glycolysis_state_9', 'N2__Cell_2_': 'glycolysis_state_10', 'A3__Cell_1_': 'glycolysis_state_11', 'A3__Cell_2_': 'glycolysis_state_12', 'S4_ex': 'glycolysis_state_13'}
    _OBSERVABLES = ['S1__Cell_1_', 'S1__Cell_2_', 'S2__Cell_1_', 'S2__Cell_2_', 'S3__Cell_1_', 'S3__Cell_2_', 'S4__Cell_1_', 'S4__Cell_2_', 'N2__Cell_1_', 'N2__Cell_2_', 'A3__Cell_1_', 'A3__Cell_2_', 'S4_ex']
    _SPECIES_LABELS = {'S1__Cell_1_': 'Glycolysis state 1', 'S1__Cell_2_': 'Glycolysis state 2', 'S2__Cell_1_': 'Glycolysis state 3', 'S2__Cell_2_': 'Glycolysis state 4', 'S3__Cell_1_': 'Glycolysis state 5', 'S3__Cell_2_': 'Glycolysis state 6', 'S4__Cell_1_': 'Glycolysis state 7', 'S4__Cell_2_': 'Glycolysis state 8', 'N2__Cell_1_': 'Glycolysis state 9', 'N2__Cell_2_': 'Glycolysis state 10', 'A3__Cell_1_': 'Glycolysis state 11', 'A3__Cell_2_': 'Glycolysis state 12', 'S4_ex': 'Glycolysis state 13'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glycolysis_state_1': ('S1__Cell_1_', 5.8, 'native SBML value', 'Initial condition for glycolysis state 1. Maps to bundled SBML symbol `S1__Cell_1_`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_2': ('S1__Cell_2_', 2.9, 'native SBML value', 'Initial condition for glycolysis state 2. Maps to bundled SBML symbol `S1__Cell_2_`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_3': ('S2__Cell_1_', 0.9, 'native SBML value', 'Initial condition for glycolysis state 3. Maps to bundled SBML symbol `S2__Cell_1_`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_4': ('S2__Cell_2_', 0.45, 'native SBML value', 'Initial condition for glycolysis state 4. Maps to bundled SBML symbol `S2__Cell_2_`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_5': ('S3__Cell_1_', 0.2, 'native SBML value', 'Initial condition for glycolysis state 5. Maps to bundled SBML symbol `S3__Cell_1_`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glycolysis_state_1': ('S1__Cell_1_', 'native SBML value', 'Glycolysis state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `S1__Cell_1_`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_2': ('S1__Cell_2_', 'native SBML value', 'Glycolysis state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `S1__Cell_2_`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_3': ('S2__Cell_1_', 'native SBML value', 'Glycolysis state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `S2__Cell_1_`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_4': ('S2__Cell_2_', 'native SBML value', 'Glycolysis state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `S2__Cell_2_`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_5': ('S3__Cell_1_', 'native SBML value', 'Glycolysis state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `S3__Cell_1_`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000691.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
