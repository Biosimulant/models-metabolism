# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Poolman2004_CalvinCycle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Poolman2004CalvincycleBiomd0000000013Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Poolman2004_CalvinCycle."""

    _SBML_ID = 'BIOMD0000000013'
    _TITLE = 'Poolman2004_CalvinCycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'RuBP_ch': 'metabolic_pathway_state_1', 'PGA_ch': 'metabolic_pathway_state_2', 'ATP_ch': 'metabolic_pathway_state_3', 'BPGA_ch': 'metabolic_pathway_state_4', 'GAP_ch': 'metabolic_pathway_state_5', 'Pi_ch': 'metabolic_pathway_state_6', 'DHAP_ch': 'metabolic_pathway_state_7', 'FBP_ch': 'metabolic_pathway_state_8', 'F6P_ch': 'metabolic_pathway_state_9', 'E4P_ch': 'metabolic_pathway_state_10', 'X5P_ch': 'metabolic_pathway_state_11', 'SBP_ch': 'metabolic_pathway_state_12', 'S7P_ch': 'metabolic_pathway_state_13', 'R5P_ch': 'metabolic_pathway_state_14', 'Ru5P_ch': 'metabolic_pathway_state_15', 'G6P_ch': 'metabolic_pathway_state_16', 'ADP_ch': 'metabolic_pathway_state_17', 'G1P_ch': 'metabolic_pathway_state_18'}
    _OBSERVABLES = ['RuBP_ch', 'PGA_ch', 'ATP_ch', 'BPGA_ch', 'GAP_ch', 'Pi_ch', 'DHAP_ch', 'FBP_ch', 'F6P_ch', 'E4P_ch', 'X5P_ch', 'SBP_ch', 'S7P_ch', 'R5P_ch', 'Ru5P_ch', 'G6P_ch', 'ADP_ch', 'G1P_ch']
    _SPECIES_LABELS = {'RuBP_ch': 'Metabolic Pathway state 1', 'PGA_ch': 'Metabolic Pathway state 2', 'ATP_ch': 'Metabolic Pathway state 3', 'BPGA_ch': 'Metabolic Pathway state 4', 'GAP_ch': 'Metabolic Pathway state 5', 'Pi_ch': 'Metabolic Pathway state 6', 'DHAP_ch': 'Metabolic Pathway state 7', 'FBP_ch': 'Metabolic Pathway state 8', 'F6P_ch': 'Metabolic Pathway state 9', 'E4P_ch': 'Metabolic Pathway state 10', 'X5P_ch': 'Metabolic Pathway state 11', 'SBP_ch': 'Metabolic Pathway state 12', 'S7P_ch': 'Metabolic Pathway state 13', 'R5P_ch': 'Metabolic Pathway state 14', 'Ru5P_ch': 'Metabolic Pathway state 15', 'G6P_ch': 'Metabolic Pathway state 16', 'ADP_ch': 'Metabolic Pathway state 17', 'G1P_ch': 'Metabolic Pathway state 18'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('RuBP_ch', 0.33644, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `RuBP_ch`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('PGA_ch', 3.35479, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `PGA_ch`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('ATP_ch', 0.49806, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `ATP_ch`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('BPGA_ch', 0.14825, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `BPGA_ch`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('GAP_ch', 0.01334, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `GAP_ch`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('RuBP_ch', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `RuBP_ch`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('PGA_ch', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PGA_ch`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('ATP_ch', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `ATP_ch`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('BPGA_ch', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `BPGA_ch`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('GAP_ch', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `GAP_ch`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000013.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
