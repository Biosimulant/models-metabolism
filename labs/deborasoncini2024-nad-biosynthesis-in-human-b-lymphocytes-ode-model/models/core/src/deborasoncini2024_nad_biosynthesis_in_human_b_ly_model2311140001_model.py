# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for DeboraSoncini2024 - NAD_Biosynthesis_in Human_B_Lymphocytes,ODE model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Deborasoncini2024NadBiosynthesisInHumanBLyModel2311140001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for DeboraSoncini2024 - NAD_Biosynthesis_in Human_B_Lymphocytes,ODE model."""

    _SBML_ID = 'MODEL2311140001'
    _TITLE = 'DeboraSoncini2024 - NAD_Biosynthesis_in Human_B_Lymphocytes,ODE model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Hydroxykynurenine': 'nad_metabolism_state_1', 'Hydroxyanthranilate': 'nad_metabolism_state_2', 'Quinolinate': 'nad_metabolism_state_3', 'NaMN': 'nad_metabolism_state_4', 'PPi': 'nad_metabolism_state_5', 'NaAD': 'nad_metabolism_state_6', 'NAD': 'nad', 'NMN': 'nad_metabolism_state_8', 'NADP': 'nadp', 'Nam': 'nad_metabolism_state_10', 'ADPribose': 'nad_metabolism_state_11', 'ADPriboseP': 'nad_metabolism_state_12', 'L_Kynurenine': 'nad_metabolism_state_13', 'NR': 'nad_metabolism_state_14', 'Formyl_kynurenine': 'nad_metabolism_state_15', 'Kynurenic_acid': 'nad_metabolism_state_16', 'Xanthurenic_acid': 'nad_metabolism_state_17', 'ACMS': 'nad_metabolism_state_18'}
    _OBSERVABLES = ['Hydroxykynurenine', 'Hydroxyanthranilate', 'Quinolinate', 'NaMN', 'PPi', 'NaAD', 'NAD', 'NMN', 'NADP', 'Nam', 'ADPribose', 'ADPriboseP', 'L_Kynurenine', 'NR', 'Formyl_kynurenine', 'Kynurenic_acid', 'Xanthurenic_acid', 'ACMS']
    _SPECIES_LABELS = {'Hydroxykynurenine': 'NAD Metabolism state 1', 'Hydroxyanthranilate': 'NAD Metabolism state 2', 'Quinolinate': 'NAD Metabolism state 3', 'NaMN': 'NAD Metabolism state 4', 'PPi': 'NAD Metabolism state 5', 'NaAD': 'NAD Metabolism state 6', 'NAD': 'NAD', 'NMN': 'NAD Metabolism state 8', 'NADP': 'NADP', 'Nam': 'NAD Metabolism state 10', 'ADPribose': 'NAD Metabolism state 11', 'ADPriboseP': 'NAD Metabolism state 12', 'L_Kynurenine': 'NAD Metabolism state 13', 'NR': 'NAD Metabolism state 14', 'Formyl_kynurenine': 'NAD Metabolism state 15', 'Kynurenic_acid': 'NAD Metabolism state 16', 'Xanthurenic_acid': 'NAD Metabolism state 17', 'ACMS': 'NAD Metabolism state 18'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nad_metabolism_state_1': ('Hydroxykynurenine', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 1. Maps to bundled SBML symbol `Hydroxykynurenine`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_2': ('Hydroxyanthranilate', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 2. Maps to bundled SBML symbol `Hydroxyanthranilate`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_3': ('Quinolinate', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 3. Maps to bundled SBML symbol `Quinolinate`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_4': ('NaMN', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 4. Maps to bundled SBML symbol `NaMN`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_5': ('PPi', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 5. Maps to bundled SBML symbol `PPi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'nad_metabolism_state_1': ('Hydroxykynurenine', 'native SBML value', 'NAD Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Hydroxykynurenine`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'nad_metabolism_state_2': ('Hydroxyanthranilate', 'native SBML value', 'NAD Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Hydroxyanthranilate`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'nad_metabolism_state_3': ('Quinolinate', 'native SBML value', 'NAD Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Quinolinate`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'nad_metabolism_state_4': ('NaMN', 'native SBML value', 'NAD Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `NaMN`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'nad_metabolism_state_5': ('PPi', 'native SBML value', 'NAD Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PPi`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2311140001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
