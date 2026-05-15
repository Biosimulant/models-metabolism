# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Lee2017 - Paracetamol first-pass metabolism PK model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2017ParacetamolFirstPassMetabolismPkModBiomd0000000947Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Lee2017 - Paracetamol first-pass metabolism PK model."""

    _SBML_ID = 'BIOMD0000000947'
    _TITLE = 'Lee2017 - Paracetamol first-pass metabolism PK model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'V_api': 'drug_metabolism_state_1', 'V_caco': 'drug_metabolism_state_2', 'V_basol': 'drug_metabolism_state_3', 'C_para_Apical': 'drug_metabolism_state_4', 'C_para_Caco_2': 'drug_metabolism_state_5', 'C_para__Basolateral___HepG2_': 'drug_metabolism_state_6', 'C_sulf_Apical': 'drug_metabolism_state_7', 'C_sulf_Caco_2': 'drug_metabolism_state_8', 'C_sulf__Basolateral___HepG2_': 'drug_metabolism_state_9', 'C_glu_Apical': 'drug_metabolism_state_10', 'C_glu_Caco_2': 'drug_metabolism_state_11', 'C_glu__Basolateral___HepG2_': 'drug_metabolism_state_12'}
    _OBSERVABLES = ['V_api', 'V_caco', 'V_basol', 'C_para_Apical', 'C_para_Caco_2', 'C_para__Basolateral___HepG2_', 'C_sulf_Apical', 'C_sulf_Caco_2', 'C_sulf__Basolateral___HepG2_', 'C_glu_Apical', 'C_glu_Caco_2', 'C_glu__Basolateral___HepG2_']
    _SPECIES_LABELS = {'V_api': 'Drug Metabolism state 1', 'V_caco': 'Drug Metabolism state 2', 'V_basol': 'Drug Metabolism state 3', 'C_para_Apical': 'Drug Metabolism state 4', 'C_para_Caco_2': 'Drug Metabolism state 5', 'C_para__Basolateral___HepG2_': 'Drug Metabolism state 6', 'C_sulf_Apical': 'Drug Metabolism state 7', 'C_sulf_Caco_2': 'Drug Metabolism state 8', 'C_sulf__Basolateral___HepG2_': 'Drug Metabolism state 9', 'C_glu_Apical': 'Drug Metabolism state 10', 'C_glu_Caco_2': 'Drug Metabolism state 11', 'C_glu__Basolateral___HepG2_': 'Drug Metabolism state 12'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_drug_metabolism_state_1': ('V_api', 500.0, 'native SBML value', 'Initial condition for drug metabolism state 1. Maps to bundled SBML symbol `V_api`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_2': ('V_caco', 0.33, 'native SBML value', 'Initial condition for drug metabolism state 2. Maps to bundled SBML symbol `V_caco`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_3': ('V_basol', 380.0, 'native SBML value', 'Initial condition for drug metabolism state 3. Maps to bundled SBML symbol `V_basol`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_4': ('C_para_Apical', 2500.0, 'native SBML value', 'Initial condition for drug metabolism state 4. Maps to bundled SBML symbol `C_para_Apical`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_5': ('C_para_Caco_2', 1e-15, 'native SBML value', 'Initial condition for drug metabolism state 5. Maps to bundled SBML symbol `C_para_Caco_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'drug_metabolism_state_1': ('V_api', 'native SBML value', 'Drug Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `V_api`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_2': ('V_caco', 'native SBML value', 'Drug Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `V_caco`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_3': ('V_basol', 'native SBML value', 'Drug Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `V_basol`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_4': ('C_para_Apical', 'native SBML value', 'Drug Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `C_para_Apical`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_5': ('C_para_Caco_2', 'native SBML value', 'Drug Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `C_para_Caco_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000947.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
