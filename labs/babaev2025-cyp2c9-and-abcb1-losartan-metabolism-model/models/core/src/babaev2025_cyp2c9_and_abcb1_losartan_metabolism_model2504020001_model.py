# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Babaev2025 - CYP2C9 and ABCB1 losartan metabolism model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Babaev2025Cyp2c9AndAbcb1LosartanMetabolismModel2504020001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Babaev2025 - CYP2C9 and ABCB1 losartan metabolism model."""

    _SBML_ID = 'MODEL2504020001'
    _TITLE = 'Babaev2025 - CYP2C9 and ABCB1 losartan metabolism model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'E3174_out': 'losartan_metabolite_e3174', 'E3174_cc': 'losartan_metabolite_e3174_2', 'losartan_cc': 'drug_metabolism_state_3', 'losartan_ent': 'drug_metabolism_state_4', 'losartan_int': 'drug_metabolism_state_5', 'losartan_out': 'drug_metabolism_state_6_extracellular', 'losartan_pc': 'drug_metabolism_state_7', 'losartan_stm': 'drug_metabolism_state_8'}
    _OBSERVABLES = ['E3174_out', 'E3174_cc', 'losartan_cc', 'losartan_ent', 'losartan_int', 'losartan_out', 'losartan_pc', 'losartan_stm']
    _SPECIES_LABELS = {'E3174_out': 'Losartan metabolite E3174', 'E3174_cc': 'Losartan metabolite E3174 2', 'losartan_cc': 'Drug Metabolism state 3', 'losartan_ent': 'Drug Metabolism state 4', 'losartan_int': 'Drug Metabolism state 5', 'losartan_out': 'Drug Metabolism state 6 extracellular', 'losartan_pc': 'Drug Metabolism state 7', 'losartan_stm': 'Drug Metabolism state 8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_losartan_metabolite_e3174': ('E3174_out', 0.0, 'native SBML value', 'Initial condition for losartan metabolite e3174. Maps to bundled SBML symbol `E3174_out`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_losartan_metabolite_e3174_2': ('E3174_cc', 0.0, 'native SBML value', 'Initial condition for losartan metabolite e3174 2. Maps to bundled SBML symbol `E3174_cc`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_3': ('losartan_cc', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 3. Maps to bundled SBML symbol `losartan_cc`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_4': ('losartan_ent', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 4. Maps to bundled SBML symbol `losartan_ent`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_5': ('losartan_int', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 5. Maps to bundled SBML symbol `losartan_int`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'losartan_metabolite_e3174': ('E3174_out', 'native SBML value', 'Losartan metabolite E3174. Maps to SBML symbol `E3174_out`.'), 'losartan_metabolite_e3174_2': ('E3174_cc', 'native SBML value', 'Losartan metabolite E3174 2. Maps to SBML symbol `E3174_cc`.'), 'drug_metabolism_state_3': ('losartan_cc', 'native SBML value', 'Drug Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `losartan_cc`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_4': ('losartan_ent', 'native SBML value', 'Drug Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `losartan_ent`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_5': ('losartan_int', 'native SBML value', 'Drug Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `losartan_int`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2504020001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
