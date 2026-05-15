# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Nijhout2006_Hepatic_Folate_Metab."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nijhout2006HepaticFolateMetabModel1007200000Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Nijhout2006_Hepatic_Folate_Metab."""

    _SBML_ID = 'MODEL1007200000'
    _TITLE = 'Nijhout2006_Hepatic_Folate_Metab'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'c_thf': 'cytosolic_tetrahydrofolate', 'm_thf': 'mitochondrial_tetrahydrofolate', 'c_5mf': 'folate_metabolism_state_3', 'c_2cf': 'folate_metabolism_state_4', 'c_1cf': 'folate_metabolism_state_5', 'c_10f': 'folate_metabolism_state_6', 'dhf': 'dihydrofolate', 'm_2cf': 'folate_metabolism_state_8', 'm_1cf': 'folate_metabolism_state_9', 'm_10f': 'folate_metabolism_state_10', 'aic': 'folate_metabolism_state_11', 'c_gly': 'c_glycine', 'hcy': 'homocysteine', 'c_ser': 'cytosolic_serine', 'sah': 's_adenosylhomocysteine', 'sam': 's_adenosylmethionine', 'met': 'methionine', 'c_coo': 'c_formate', 'm_ser': 'm_serine', 'm_gly': 'mit_glycine', 'm_coo': 'm_formate', 'src': 'sarcosine', 'dmg': 'dimethylglycine'}
    _OBSERVABLES = ['c_thf', 'm_thf', 'c_5mf', 'c_2cf', 'c_1cf', 'c_10f', 'dhf', 'm_2cf', 'm_1cf', 'm_10f', 'aic', 'c_gly', 'hcy', 'c_ser', 'sah', 'sam', 'met', 'c_coo', 'm_ser', 'm_gly', 'm_coo', 'src', 'dmg']
    _SPECIES_LABELS = {'c_thf': 'Cytosolic Tetrahydrofolate', 'm_thf': 'Mitochondrial Tetrahydrofolate', 'c_5mf': 'Folate Metabolism state 3', 'c_2cf': 'Folate Metabolism state 4', 'c_1cf': 'Folate Metabolism state 5', 'c_10f': 'Folate Metabolism state 6', 'dhf': 'Dihydrofolate', 'm_2cf': 'Folate Metabolism state 8', 'm_1cf': 'Folate Metabolism state 9', 'm_10f': 'Folate Metabolism state 10', 'aic': 'Folate Metabolism state 11', 'c_gly': 'C Glycine', 'hcy': 'Homocysteine', 'c_ser': 'Cytosolic Serine', 'sah': 'S Adenosylhomocysteine', 'sam': 'S Adenosylmethionine', 'met': 'Methionine', 'c_coo': 'C Formate', 'm_ser': 'M Serine', 'm_gly': 'Mit Glycine', 'm_coo': 'M Formate', 'src': 'Sarcosine', 'dmg': 'Dimethylglycine'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cytosolic_tetrahydrofolate': ('c_thf', 13.333333333333334, 'native SBML value', 'Initial condition for cytosolic tetrahydrofolate. Maps to bundled SBML symbol `c_thf`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_mitochondrial_tetrahydrofolate': ('m_thf', 40.0, 'native SBML value', 'Initial condition for mitochondrial tetrahydrofolate. Maps to bundled SBML symbol `m_thf`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_folate_metabolism_state_3': ('c_5mf', 0.0, 'native SBML value', 'Initial condition for folate metabolism state 3. Maps to bundled SBML symbol `c_5mf`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_folate_metabolism_state_4': ('c_2cf', 0.0, 'native SBML value', 'Initial condition for folate metabolism state 4. Maps to bundled SBML symbol `c_2cf`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_folate_metabolism_state_5': ('c_1cf', 0.0, 'native SBML value', 'Initial condition for folate metabolism state 5. Maps to bundled SBML symbol `c_1cf`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'cytosolic_tetrahydrofolate': ('c_thf', 'native SBML value', 'Cytosolic Tetrahydrofolate. Maps to SBML symbol `c_thf`.'), 'mitochondrial_tetrahydrofolate': ('m_thf', 'native SBML value', 'Mitochondrial Tetrahydrofolate. Maps to SBML symbol `m_thf`.'), 'folate_metabolism_state_3': ('c_5mf', 'native SBML value', 'Folate Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `c_5mf`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'folate_metabolism_state_4': ('c_2cf', 'native SBML value', 'Folate Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `c_2cf`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'folate_metabolism_state_5': ('c_1cf', 'native SBML value', 'Folate Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `c_1cf`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL1007200000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
