# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Tran2009_CardiacActiveForceGeneration."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tran2009CardiacactiveforcegenerationModel1006230116Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Tran2009_CardiacActiveForceGeneration."""

    _SBML_ID = 'MODEL1006230116'
    _TITLE = 'Tran2009_CardiacActiveForceGeneration'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Ca_sr': 'metabolic_pathway_state_1', 'T_Cai': 'metabolic_pathway_state_2', 'T_Casr': 'metabolic_pathway_state_3', 'T_H1': 'metabolic_pathway_state_4', 'T_Hi': 'metabolic_pathway_state_5', 'T_Hsr': 'metabolic_pathway_state_6', 'T_H': 'metabolic_pathway_state_7', 'a_p1': 'metabolic_pathway_state_8', 'a_p2': 'metabolic_pathway_state_9', 'a_p3': 'metabolic_pathway_state_10', 'a_m1': 'metabolic_pathway_state_11', 'a_m2': 'metabolic_pathway_state_12', 'a_m3': 'metabolic_pathway_state_13', 's1': 'metabolic_pathway_state_14', 's2': 'metabolic_pathway_state_15', 's3': 'metabolic_pathway_state_16', 'v_cycle': 'metabolic_pathway_state_17'}
    _OBSERVABLES = ['Ca_sr', 'T_Cai', 'T_Casr', 'T_H1', 'T_Hi', 'T_Hsr', 'T_H', 'a_p1', 'a_p2', 'a_p3', 'a_m1', 'a_m2', 'a_m3', 's1', 's2', 's3', 'v_cycle']
    _SPECIES_LABELS = {'Ca_sr': 'Metabolic Pathway state 1', 'T_Cai': 'Metabolic Pathway state 2', 'T_Casr': 'Metabolic Pathway state 3', 'T_H1': 'Metabolic Pathway state 4', 'T_Hi': 'Metabolic Pathway state 5', 'T_Hsr': 'Metabolic Pathway state 6', 'T_H': 'Metabolic Pathway state 7', 'a_p1': 'Metabolic Pathway state 8', 'a_p2': 'Metabolic Pathway state 9', 'a_p3': 'Metabolic Pathway state 10', 'a_m1': 'Metabolic Pathway state 11', 'a_m2': 'Metabolic Pathway state 12', 'a_m3': 'Metabolic Pathway state 13', 's1': 'Metabolic Pathway state 14', 's2': 'Metabolic Pathway state 15', 's3': 'Metabolic Pathway state 16', 'v_cycle': 'Metabolic Pathway state 17'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('Ca_sr', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `Ca_sr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('T_Cai', 0.00016666666666666666, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `T_Cai`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('T_Casr', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `T_Casr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('T_H1', 9.174311926605505, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `T_H1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('T_Hi', 2.824858757062147e-06, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `T_Hi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('Ca_sr', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Ca_sr`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('T_Cai', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `T_Cai`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('T_Casr', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `T_Casr`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('T_H1', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `T_H1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('T_Hi', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `T_Hi`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL1006230116.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
