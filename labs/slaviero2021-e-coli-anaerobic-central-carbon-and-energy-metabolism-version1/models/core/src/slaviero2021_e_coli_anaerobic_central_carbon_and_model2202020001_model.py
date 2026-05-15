# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Slaviero2021 - E. coli anaerobic central carbon and energy metabolism_Version1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Slaviero2021EColiAnaerobicCentralCarbonAndModel2202020001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Slaviero2021 - E. coli anaerobic central carbon and energy metabolism_Version1."""

    _SBML_ID = 'MODEL2202020001'
    _TITLE = 'Slaviero2021 - E. coli anaerobic central carbon and energy metabolism_Version1'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'G6P': 'glucose_6_phosphate', 'FBP': 'fructose_bisphosphate', 'GAP': 'glyceraldehyde_3_phosphate', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'ATP': 'atp', 'ADP': 'adp', 'Biomass': 'glycolysis_state_8', 'F6P': 'fructose_6_phosphate', 'AcCoA': 'glycolysis_state_10', 'FOR': 'glycolysis_state_11', 'LAC': 'lactate', 'OAA': 'glycolysis_state_13', 'AKG': 'glycolysis_state_14', 'SUCin': 'glycolysis_state_15', 'SUC': 'glycolysis_state_16', 'NADH': 'nadh', 'ACE': 'ace', 'ETH': 'glycolysis_state_19', 'D3PG': 'glycolysis_state_20', 'BPG': 'glycolysis_state_21', 'LACin': 'intracellular_lactate', 'FORin': 'glycolysis_state_23', 'ETHin': 'glycolysis_state_24', 'ACEin': 'intracellular_ace', 'FUM': 'glycolysis_state_26', 'ACTLD': 'glycolysis_state_27'}
    _OBSERVABLES = ['G6P', 'FBP', 'GAP', 'PEP', 'PYR', 'ATP', 'ADP', 'Biomass', 'F6P', 'AcCoA', 'FOR', 'LAC', 'OAA', 'AKG', 'SUCin', 'SUC', 'NADH', 'ACE', 'ETH', 'D3PG', 'BPG', 'LACin', 'FORin', 'ETHin', 'ACEin', 'FUM', 'ACTLD']
    _SPECIES_LABELS = {'G6P': 'Glucose 6 Phosphate', 'FBP': 'Fructose Bisphosphate', 'GAP': 'Glyceraldehyde 3 Phosphate', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate', 'ATP': 'ATP', 'ADP': 'ADP', 'Biomass': 'Glycolysis state 8', 'F6P': 'Fructose 6 Phosphate', 'AcCoA': 'Glycolysis state 10', 'FOR': 'Glycolysis state 11', 'LAC': 'Lactate', 'OAA': 'Glycolysis state 13', 'AKG': 'Glycolysis state 14', 'SUCin': 'Glycolysis state 15', 'SUC': 'Glycolysis state 16', 'NADH': 'NADH', 'ACE': 'ACE', 'ETH': 'Glycolysis state 19', 'D3PG': 'Glycolysis state 20', 'BPG': 'Glycolysis state 21', 'LACin': 'Intracellular Lactate', 'FORin': 'Glycolysis state 23', 'ETHin': 'Glycolysis state 24', 'ACEin': 'Intracellular ACE', 'FUM': 'Glycolysis state 26', 'ACTLD': 'Glycolysis state 27'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_6_phosphate': ('G6P', 2.0, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_bisphosphate': ('FBP', 3.0, 'native SBML value', 'Initial condition for fructose bisphosphate. Maps to bundled SBML symbol `FBP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glyceraldehyde_3_phosphate': ('GAP', 0.5, 'native SBML value', 'Initial condition for glyceraldehyde 3 phosphate. Maps to bundled SBML symbol `GAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_phosphoenolpyruvate': ('PEP', 1.0, 'native SBML value', 'Initial condition for phosphoenolpyruvate. Maps to bundled SBML symbol `PEP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pyruvate': ('PYR', 1.0, 'native SBML value', 'Initial condition for pyruvate. Maps to bundled SBML symbol `PYR`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'fructose_bisphosphate': ('FBP', 'native SBML value', 'Fructose Bisphosphate. Maps to SBML symbol `FBP`.'), 'glyceraldehyde_3_phosphate': ('GAP', 'native SBML value', 'Glyceraldehyde 3 Phosphate. Maps to SBML symbol `GAP`.'), 'phosphoenolpyruvate': ('PEP', 'native SBML value', 'Phosphoenolpyruvate. Maps to SBML symbol `PEP`.'), 'pyruvate': ('PYR', 'native SBML value', 'Pyruvate. Maps to SBML symbol `PYR`.')}

    def __init__(self, model_path: str = 'data/MODEL2202020001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
