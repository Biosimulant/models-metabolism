# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Nazaret2008_Dynnik1980_CarbohydrateEnergyMetabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nazaret2008Dynnik1980CarbohydrateenergymetabolModel1202170000Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Nazaret2008_Dynnik1980_CarbohydrateEnergyMetabolism."""

    _SBML_ID = 'MODEL1202170000'
    _TITLE = 'Nazaret2008_Dynnik1980_CarbohydrateEnergyMetabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'s1': 'glyceraldehyde_3_phosphate', 's2_e1': 'metabolic_pathway_state_2', 's3_e2': 'observable_13dpg', 's4_e3': 'pyruvate', 's5_e4': 'lactate', 'a3_e5': 'atp', 'a1_e5': 'amp', 'r1_e6': 'metabolic_pathway_state_8', 'n2_e7': 'metabolic_pathway_state_9', 'i1_e8': 'metabolic_pathway_state_10', 'i2_e8': 'metabolic_pathway_state_11', 'c2_e9': 'metabolic_pathway_state_12'}
    _OBSERVABLES = ['s1', 's2_e1', 's3_e2', 's4_e3', 's5_e4', 'a3_e5', 'a1_e5', 'r1_e6', 'n2_e7', 'i1_e8', 'i2_e8', 'c2_e9']
    _SPECIES_LABELS = {'s1': 'glyceraldehyde 3 phosphate', 's2_e1': 'Metabolic Pathway state 2', 's3_e2': '13dpg', 's4_e3': 'pyruvate', 's5_e4': 'lactate', 'a3_e5': 'ATP', 'a1_e5': 'AMP', 'r1_e6': 'Metabolic Pathway state 8', 'n2_e7': 'Metabolic Pathway state 9', 'i1_e8': 'Metabolic Pathway state 10', 'i2_e8': 'Metabolic Pathway state 11', 'c2_e9': 'Metabolic Pathway state 12'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glyceraldehyde_3_phosphate': ('s1', 0.1, 'native SBML value', 'Initial condition for glyceraldehyde 3 phosphate. Maps to bundled SBML symbol `s1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('s2_e1', 0.5, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `s2_e1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_observable_13dpg': ('s3_e2', 0.5, 'native SBML value', 'Initial condition for observable 13dpg. Maps to bundled SBML symbol `s3_e2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pyruvate': ('s4_e3', 0.01, 'native SBML value', 'Initial condition for pyruvate. Maps to bundled SBML symbol `s4_e3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lactate': ('s5_e4', 0.01, 'native SBML value', 'Initial condition for lactate. Maps to bundled SBML symbol `s5_e4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glyceraldehyde_3_phosphate': ('s1', 'native SBML value', 'glyceraldehyde 3 phosphate. Maps to SBML symbol `s1`.'), 'metabolic_pathway_state_2': ('s2_e1', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `s2_e1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'observable_13dpg': ('s3_e2', 'native SBML value', '13dpg. Maps to SBML symbol `s3_e2`.'), 'pyruvate': ('s4_e3', 'native SBML value', 'pyruvate. Maps to SBML symbol `s4_e3`.'), 'lactate': ('s5_e4', 'native SBML value', 'lactate. Maps to SBML symbol `s5_e4`.')}

    def __init__(self, model_path: str = 'data/MODEL1202170000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
