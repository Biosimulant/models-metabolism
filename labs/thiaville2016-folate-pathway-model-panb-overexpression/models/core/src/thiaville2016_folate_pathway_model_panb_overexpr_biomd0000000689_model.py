# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Thiaville2016 - Folate pathway model (PanB overexpression)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Thiaville2016FolatePathwayModelPanbOverexprBiomd0000000689Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Thiaville2016 - Folate pathway model (PanB overexpression)."""

    _SBML_ID = 'BIOMD0000000689'
    _TITLE = 'Thiaville2016 - Folate pathway model (PanB overexpression)'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'H2_HMPt': 'folate_metabolism_state_1', 'H2_HMPterinPP': 'folate_metabolism_state_2', 'p_ABA': 'para_aminobenzoate', 'H2_Pteroate': 'folate_metabolism_state_4', 'DHF': 'dihydrofolate', 'THF': 'tetrahydrofolate', 'CH2_THF': 'folate_metabolism_state_7'}
    _OBSERVABLES = ['H2_HMPt', 'H2_HMPterinPP', 'p_ABA', 'H2_Pteroate', 'DHF', 'THF', 'CH2_THF']
    _SPECIES_LABELS = {'H2_HMPt': 'Folate Metabolism state 1', 'H2_HMPterinPP': 'Folate Metabolism state 2', 'p_ABA': 'Para Aminobenzoate', 'H2_Pteroate': 'Folate Metabolism state 4', 'DHF': 'Dihydrofolate', 'THF': 'Tetrahydrofolate', 'CH2_THF': 'Folate Metabolism state 7'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_folate_metabolism_state_1': ('H2_HMPt', 3.315e-06, 'native SBML value', 'Initial condition for folate metabolism state 1. Maps to bundled SBML symbol `H2_HMPt`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_folate_metabolism_state_2': ('H2_HMPterinPP', 1e-05, 'native SBML value', 'Initial condition for folate metabolism state 2. Maps to bundled SBML symbol `H2_HMPterinPP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_para_aminobenzoate': ('p_ABA', 1e-05, 'native SBML value', 'Initial condition for para aminobenzoate. Maps to bundled SBML symbol `p_ABA`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_folate_metabolism_state_4': ('H2_Pteroate', 1e-05, 'native SBML value', 'Initial condition for folate metabolism state 4. Maps to bundled SBML symbol `H2_Pteroate`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_dihydrofolate': ('DHF', 1e-05, 'native SBML value', 'Initial condition for dihydrofolate. Maps to bundled SBML symbol `DHF`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'folate_metabolism_state_1': ('H2_HMPt', 'native SBML value', 'Folate Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `H2_HMPt`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'folate_metabolism_state_2': ('H2_HMPterinPP', 'native SBML value', 'Folate Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `H2_HMPterinPP`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'para_aminobenzoate': ('p_ABA', 'native SBML value', 'Para Aminobenzoate. Maps to SBML symbol `p_ABA`.'), 'folate_metabolism_state_4': ('H2_Pteroate', 'native SBML value', 'Folate Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `H2_Pteroate`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'dihydrofolate': ('DHF', 'native SBML value', 'Dihydrofolate. Maps to SBML symbol `DHF`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000689.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
