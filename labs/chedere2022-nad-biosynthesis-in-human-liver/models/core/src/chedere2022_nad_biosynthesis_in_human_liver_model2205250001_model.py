# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Chedere2022 - NAD Biosynthesis in Human Liver."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chedere2022NadBiosynthesisInHumanLiverModel2205250001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Chedere2022 - NAD Biosynthesis in Human Liver."""

    _SBML_ID = 'MODEL2205250001'
    _TITLE = 'Chedere2022 - NAD Biosynthesis in Human Liver'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'L_formyl_kyn': 'l_formyl_kyneurenine', 'Hydroxyurenine': 'hydroxykynurenine', 'Hydroxyanthranilate': 'nad_metabolism_state_3', 'Quinolinate': 'nad_metabolism_state_4', 'NaMN': 'nad_metabolism_state_5', 'NaAD': 'nad_metabolism_state_6', 'NAD': 'nad', 'NMN': 'nad_metabolism_state_8', 'NADP': 'nadp', 'Nam': 'nad_metabolism_state_10', 'ADPribose': 'nad_metabolism_state_11', 'ADPriboseP': 'nad_metabolism_state_12', 'L_kyneurenine': 'nad_metabolism_state_13', 'NR': 'nad_metabolism_state_14'}
    _OBSERVABLES = ['L_formyl_kyn', 'Hydroxyurenine', 'Hydroxyanthranilate', 'Quinolinate', 'NaMN', 'NaAD', 'NAD', 'NMN', 'NADP', 'Nam', 'ADPribose', 'ADPriboseP', 'L_kyneurenine', 'NR']
    _SPECIES_LABELS = {'L_formyl_kyn': 'L Formyl Kyneurenine', 'Hydroxyurenine': 'Hydroxykynurenine', 'Hydroxyanthranilate': 'NAD Metabolism state 3', 'Quinolinate': 'NAD Metabolism state 4', 'NaMN': 'NAD Metabolism state 5', 'NaAD': 'NAD Metabolism state 6', 'NAD': 'NAD', 'NMN': 'NAD Metabolism state 8', 'NADP': 'NADP', 'Nam': 'NAD Metabolism state 10', 'ADPribose': 'NAD Metabolism state 11', 'ADPriboseP': 'NAD Metabolism state 12', 'L_kyneurenine': 'NAD Metabolism state 13', 'NR': 'NAD Metabolism state 14'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_l_formyl_kyneurenine': ('L_formyl_kyn', 0.0, 'native SBML value', 'Initial condition for l formyl kyneurenine. Maps to bundled SBML symbol `L_formyl_kyn`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_hydroxykynurenine': ('Hydroxyurenine', 0.0, 'native SBML value', 'Initial condition for hydroxykynurenine. Maps to bundled SBML symbol `Hydroxyurenine`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_3': ('Hydroxyanthranilate', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 3. Maps to bundled SBML symbol `Hydroxyanthranilate`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_4': ('Quinolinate', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 4. Maps to bundled SBML symbol `Quinolinate`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad_metabolism_state_5': ('NaMN', 0.0, 'native SBML value', 'Initial condition for nad metabolism state 5. Maps to bundled SBML symbol `NaMN`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'l_formyl_kyneurenine': ('L_formyl_kyn', 'native SBML value', 'L Formyl Kyneurenine. Maps to SBML symbol `L_formyl_kyn`.'), 'hydroxykynurenine': ('Hydroxyurenine', 'native SBML value', 'Hydroxykynurenine. Maps to SBML symbol `Hydroxyurenine`.'), 'nad_metabolism_state_3': ('Hydroxyanthranilate', 'native SBML value', 'NAD Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Hydroxyanthranilate`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'nad_metabolism_state_4': ('Quinolinate', 'native SBML value', 'NAD Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Quinolinate`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'nad_metabolism_state_5': ('NaMN', 'native SBML value', 'NAD Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `NaMN`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2205250001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
