# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Hynne2001_Glycolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hynne2001GlycolysisBiomd0000000061Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Hynne2001_Glycolysis."""

    _SBML_ID = 'BIOMD0000000061'
    _TITLE = 'Hynne2001_Glycolysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'GlcX': 'extracellular_glucose', 'Glc': 'cytosolic_glucose', 'ATP': 'atp', 'G6P': 'glucose_6_phosphate', 'ADP': 'adp', 'F6P': 'fructose_6_phosphate', 'FBP': 'fructose_1_6_bisphosphate', 'GAP': 'glyceraldehyde_3_phosphate', 'DHAP': 'dihydroxyacetone_phosphate', 'NAD': 'nad', 'BPG': 'observable_1_3_bisphosphoglycerate', 'NADH': 'nadh', 'PEP': 'phosphoenolpyruvate', 'Pyr': 'pyruvate', 'ACA': 'acetaldehyde', 'EtOH': 'glycolysis_state_16', 'EtOHX': 'extracellular_ethanol', 'Glyc': 'glycolysis_state_18', 'GlycX': 'extracellular_glycerol', 'ACAX': 'extracellular_acetaldehyde', 'CNX': 'extracellular_cyanide', 'AMP': 'amp'}
    _OBSERVABLES = ['GlcX', 'Glc', 'ATP', 'G6P', 'ADP', 'F6P', 'FBP', 'GAP', 'DHAP', 'NAD', 'BPG', 'NADH', 'PEP', 'Pyr', 'ACA', 'EtOH', 'EtOHX', 'Glyc', 'GlycX', 'ACAX', 'CNX', 'AMP']
    _SPECIES_LABELS = {'GlcX': 'Extracellular Glucose', 'Glc': 'Cytosolic Glucose', 'ATP': 'ATP', 'G6P': 'Glucose 6 Phosphate', 'ADP': 'ADP', 'F6P': 'Fructose 6 Phosphate', 'FBP': 'Fructose 1 6 Bisphosphate', 'GAP': 'Glyceraldehyde 3 Phosphate', 'DHAP': 'Dihydroxyacetone Phosphate', 'NAD': 'NAD', 'BPG': '1 3 Bisphosphoglycerate', 'NADH': 'NADH', 'PEP': 'Phosphoenolpyruvate', 'Pyr': 'Pyruvate', 'ACA': 'Acetaldehyde', 'EtOH': 'Glycolysis state 16', 'EtOHX': 'Extracellular Ethanol', 'Glyc': 'Glycolysis state 18', 'GlycX': 'Extracellular Glycerol', 'ACAX': 'Extracellular Acetaldehyde', 'CNX': 'Extracellular Cyanide', 'AMP': 'AMP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_extracellular_glucose': ('GlcX', 6.7, 'native SBML value', 'Initial condition for extracellular glucose. Maps to bundled SBML symbol `GlcX`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_cytosolic_glucose': ('Glc', 0.573074, 'native SBML value', 'Initial condition for cytosolic glucose. Maps to bundled SBML symbol `Glc`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 2.1, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 4.2, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adp': ('ADP', 1.5, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'extracellular_glucose': ('GlcX', 'native SBML value', 'Extracellular Glucose. Maps to SBML symbol `GlcX`.'), 'cytosolic_glucose': ('Glc', 'native SBML value', 'Cytosolic Glucose. Maps to SBML symbol `Glc`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000061.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
