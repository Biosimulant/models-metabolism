# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Gupta2009 - Eicosanoid Metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gupta2009EicosanoidMetabolismBiomd0000000436Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Gupta2009 - Eicosanoid Metabolism."""

    _SBML_ID = 'BIOMD0000000436'
    _TITLE = 'Gupta2009 - Eicosanoid Metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'HETE': 'lipid_metabolism_state_1', 'PGH2': 'lipid_metabolism_state_2', 'PGE2': 'lipid_metabolism_state_3', 'PGF2a': 'lipid_metabolism_state_4', 'PGD2': 'lipid_metabolism_state_5', 'PGJ2': 'lipid_metabolism_state_6', 'dPGJ2': 'lipid_metabolism_state_7', 'AA': 'arachidonic_acid', 'LPS': 'lipid_metabolism_state_9', 'DG': 'lipid_metabolism_state_10', 'GPCho': 'lipid_metabolism_state_11', 'dPGD2': 'lipid_metabolism_state_12'}
    _OBSERVABLES = ['HETE', 'PGH2', 'PGE2', 'PGF2a', 'PGD2', 'PGJ2', 'dPGJ2', 'AA', 'LPS', 'DG', 'GPCho', 'dPGD2']
    _SPECIES_LABELS = {'HETE': 'Lipid Metabolism state 1', 'PGH2': 'Lipid Metabolism state 2', 'PGE2': 'Lipid Metabolism state 3', 'PGF2a': 'Lipid Metabolism state 4', 'PGD2': 'Lipid Metabolism state 5', 'PGJ2': 'Lipid Metabolism state 6', 'dPGJ2': 'Lipid Metabolism state 7', 'AA': 'Arachidonic Acid', 'LPS': 'Lipid Metabolism state 9', 'DG': 'Lipid Metabolism state 10', 'GPCho': 'Lipid Metabolism state 11', 'dPGD2': 'Lipid Metabolism state 12'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lipid_metabolism_state_1': ('HETE', 0.0, 'native SBML value', 'Initial condition for lipid metabolism state 1. Maps to bundled SBML symbol `HETE`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lipid_metabolism_state_2': ('PGH2', 0.0, 'native SBML value', 'Initial condition for lipid metabolism state 2. Maps to bundled SBML symbol `PGH2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lipid_metabolism_state_3': ('PGE2', 0.0, 'native SBML value', 'Initial condition for lipid metabolism state 3. Maps to bundled SBML symbol `PGE2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lipid_metabolism_state_4': ('PGF2a', 0.0, 'native SBML value', 'Initial condition for lipid metabolism state 4. Maps to bundled SBML symbol `PGF2a`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lipid_metabolism_state_5': ('PGD2', 0.0, 'native SBML value', 'Initial condition for lipid metabolism state 5. Maps to bundled SBML symbol `PGD2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'lipid_metabolism_state_1': ('HETE', 'native SBML value', 'Lipid Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `HETE`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'lipid_metabolism_state_2': ('PGH2', 'native SBML value', 'Lipid Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PGH2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'lipid_metabolism_state_3': ('PGE2', 'native SBML value', 'Lipid Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PGE2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'lipid_metabolism_state_4': ('PGF2a', 'native SBML value', 'Lipid Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PGF2a`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'lipid_metabolism_state_5': ('PGD2', 'native SBML value', 'Lipid Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PGD2`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000436.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
