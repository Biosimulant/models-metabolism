# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Simon2025 - Neuroblastoma energy metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Simon2025NeuroblastomaEnergyMetabolismModel2502190001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Simon2025 - Neuroblastoma energy metabolism."""

    _SBML_ID = 'MODEL2502190001'
    _TITLE = 'Simon2025 - Neuroblastoma energy metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'glc': 'glucose', 'adp': 'adp', 'atp': 'atp', 'glc6p': 'metabolic_pathway_state_4', 'fru6p': 'fructose_6_phosphate', 'dhap': 'metabolic_pathway_state_6', 'fru16bp': 'metabolic_pathway_state_7', 'gap': 'glyceraldehyde_3_phosphate', 'bpg': 'metabolic_pathway_state_9', 'nad': 'nad', 'nadh': 'nadh', 'p_i': 'metabolic_pathway_state_12', 'pg3': 'metabolic_pathway_state_13', 'pg2': 'metabolic_pathway_state_14', 'pep': 'phosphoenolpyruvate', 'pyr': 'pyruvate', 'lac': 'lactate', 'acoa': 'metabolic_pathway_state_18', 'o2': 'metabolic_pathway_state_19'}
    _OBSERVABLES = ['glc', 'adp', 'atp', 'glc6p', 'fru6p', 'dhap', 'fru16bp', 'gap', 'bpg', 'nad', 'nadh', 'p_i', 'pg3', 'pg2', 'pep', 'pyr', 'lac', 'acoa', 'o2']
    _SPECIES_LABELS = {'glc': 'Glucose', 'adp': 'ADP', 'atp': 'ATP', 'glc6p': 'Metabolic Pathway state 4', 'fru6p': 'Fructose 6 Phosphate', 'dhap': 'Metabolic Pathway state 6', 'fru16bp': 'Metabolic Pathway state 7', 'gap': 'Glyceraldehyde 3 Phosphate', 'bpg': 'Metabolic Pathway state 9', 'nad': 'NAD', 'nadh': 'NADH', 'p_i': 'Metabolic Pathway state 12', 'pg3': 'Metabolic Pathway state 13', 'pg2': 'Metabolic Pathway state 14', 'pep': 'Phosphoenolpyruvate', 'pyr': 'Pyruvate', 'lac': 'Lactate', 'acoa': 'Metabolic Pathway state 18', 'o2': 'O2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose': ('glc', 2.72988078351158, 'native SBML value', 'Initial condition for glucose. Maps to bundled SBML symbol `glc`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adp': ('adp', 4.79944686874058, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `adp`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('atp', 8.14466765495666, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `atp`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('glc6p', 0.601679350245062, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `glc6p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('fru6p', 0.0499563769212773, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `fru6p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glucose': ('glc', 'native SBML value', 'Glucose. Maps to SBML symbol `glc`.'), 'adp': ('adp', 'native SBML value', 'ADP. Maps to SBML symbol `adp`.'), 'atp': ('atp', 'native SBML value', 'ATP. Maps to SBML symbol `atp`.'), 'metabolic_pathway_state_4': ('glc6p', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `glc6p`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'fructose_6_phosphate': ('fru6p', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `fru6p`.')}

    def __init__(self, model_path: str = 'data/MODEL2502190001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
