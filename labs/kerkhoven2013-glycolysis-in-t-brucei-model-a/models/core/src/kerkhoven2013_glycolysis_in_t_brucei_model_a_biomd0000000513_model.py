# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Kerkhoven2013 - Glycolysis in T.brucei - MODEL A."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kerkhoven2013GlycolysisInTBruceiModelABiomd0000000513Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Kerkhoven2013 - Glycolysis in T.brucei - MODEL A."""

    _SBML_ID = 'BIOMD0000000513'
    _TITLE = 'Kerkhoven2013 - Glycolysis in T.brucei - MODEL A'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'_2PGA_c': 'glycolysis_state_1', 'DHAP_c': 'glycolysis_state_2', 'ATP_g': 'glycolysis_state_3', 'DHAP_g': 'glycolysis_state_4', 'ADP_g': 'glycolysis_state_5', 'Glc6P_g': 'glycolysis_state_6', 'ADP_c': 'cytosolic_adp', '_3PGA_c': 'glycolysis_state_8', 'Fru6P_g': 'glycolysis_state_9', 'ATP_c': 'cytosolic_atp', '_13BPGA_g': 'glycolysis_state_11', 'Glc_c': 'cytosolic_glucose', 'Glc_g': 'glycolysis_state_13', 'Pyr_c': 'cytosolic_pyruvate', 'NAD_g': 'glycolysis_state_15', 'Fru16BP_g': 'glycolysis_state_16', 'GA3P_g': 'glycolysis_state_17', 'Gly3P_c': 'glycolysis_state_18', 'Gly3P_g': 'glycolysis_state_19', 'PEP_c': 'cytosolic_phosphoenolpyruvate', 'AMP_g': 'glycolysis_state_21', '_3PGA_g': 'glycolysis_state_22', 'AMP_c': 'cytosolic_amp', 'NADH_g': 'glycolysis_state_24'}
    _OBSERVABLES = ['_2PGA_c', 'DHAP_c', 'ATP_g', 'DHAP_g', 'ADP_g', 'Glc6P_g', 'ADP_c', '_3PGA_c', 'Fru6P_g', 'ATP_c', '_13BPGA_g', 'Glc_c', 'Glc_g', 'Pyr_c', 'NAD_g', 'Fru16BP_g', 'GA3P_g', 'Gly3P_c', 'Gly3P_g', 'PEP_c', 'AMP_g', '_3PGA_g', 'AMP_c', 'NADH_g']
    _SPECIES_LABELS = {'_2PGA_c': 'Glycolysis state 1', 'DHAP_c': 'Glycolysis state 2', 'ATP_g': 'Glycolysis state 3', 'DHAP_g': 'Glycolysis state 4', 'ADP_g': 'Glycolysis state 5', 'Glc6P_g': 'Glycolysis state 6', 'ADP_c': 'Cytosolic ADP', '_3PGA_c': 'Glycolysis state 8', 'Fru6P_g': 'Glycolysis state 9', 'ATP_c': 'Cytosolic ATP', '_13BPGA_g': 'Glycolysis state 11', 'Glc_c': 'Cytosolic Glucose', 'Glc_g': 'Glycolysis state 13', 'Pyr_c': 'Cytosolic Pyruvate', 'NAD_g': 'Glycolysis state 15', 'Fru16BP_g': 'Glycolysis state 16', 'GA3P_g': 'Glycolysis state 17', 'Gly3P_c': 'Glycolysis state 18', 'Gly3P_g': 'Glycolysis state 19', 'PEP_c': 'Cytosolic Phosphoenolpyruvate', 'AMP_g': 'Glycolysis state 21', '_3PGA_g': 'Glycolysis state 22', 'AMP_c': 'Cytosolic AMP', 'NADH_g': 'Glycolysis state 24'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glycolysis_state_1': ('_2PGA_c', 0.1, 'native SBML value', 'Initial condition for glycolysis state 1. Maps to bundled SBML symbol `_2PGA_c`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_2': ('DHAP_c', 2.23132912, 'native SBML value', 'Initial condition for glycolysis state 2. Maps to bundled SBML symbol `DHAP_c`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_3': ('ATP_g', 0.2405, 'native SBML value', 'Initial condition for glycolysis state 3. Maps to bundled SBML symbol `ATP_g`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_4': ('DHAP_g', 8.483130623, 'native SBML value', 'Initial condition for glycolysis state 4. Maps to bundled SBML symbol `DHAP_g`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_5': ('ADP_g', 1.519, 'native SBML value', 'Initial condition for glycolysis state 5. Maps to bundled SBML symbol `ADP_g`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glycolysis_state_1': ('_2PGA_c', 'native SBML value', 'Glycolysis state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `_2PGA_c`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_2': ('DHAP_c', 'native SBML value', 'Glycolysis state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `DHAP_c`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_3': ('ATP_g', 'native SBML value', 'Glycolysis state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `ATP_g`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_4': ('DHAP_g', 'native SBML value', 'Glycolysis state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `DHAP_g`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_5': ('ADP_g', 'native SBML value', 'Glycolysis state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `ADP_g`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000513.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
