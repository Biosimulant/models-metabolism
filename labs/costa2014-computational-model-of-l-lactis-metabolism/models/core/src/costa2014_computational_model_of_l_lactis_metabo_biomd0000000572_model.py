# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Costa2014 - Computational Model of L. lactis Metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Costa2014ComputationalModelOfLLactisMetaboBiomd0000000572Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Costa2014 - Computational Model of L. lactis Metabolism."""

    _SBML_ID = 'BIOMD0000000572'
    _TITLE = 'Costa2014 - Computational Model of L. lactis Metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'G6P': 'glucose_6_phosphate', 'ATP': 'atp', 'ADP': 'adp', 'Pint': 'inorganic_phosphate', 'F6P': 'fructose_6_phosphate', 'FBP': 'fructose_bisphosphate', 'G3P': 'microbial_metabolism_state_7', 'BPG': 'microbial_metabolism_state_8', 'PEP': 'phosphoenolpyruvate', 'NAD': 'nad', 'NADH': 'nadh', 'PYR': 'pyruvate', 'AcetCoA': 'microbial_metabolism_state_13', 'Acetoin': 'microbial_metabolism_state_14', 'Mannitol': 'microbial_metabolism_state_15', 'Mannitol1Phosphate': 'microbial_metabolism_state_16', 'CoA': 'coa', 'Pext': 'microbial_metabolism_state_18', 'Lactate': 'microbial_metabolism_state_19', 'Ethanol': 'microbial_metabolism_state_20', 'Acetate': 'microbial_metabolism_state_21', 'Butanediol': 'microbial_metabolism_state_22', 'Glucose': 'microbial_metabolism_state_23', 'Acetoin_Ext': 'microbial_metabolism_state_24_extracellular', 'Mannitol_Ext': 'microbial_metabolism_state_25_extracellular', 'Formate': 'microbial_metabolism_state_26'}
    _OBSERVABLES = ['G6P', 'ATP', 'ADP', 'Pint', 'F6P', 'FBP', 'G3P', 'BPG', 'PEP', 'NAD', 'NADH', 'PYR', 'AcetCoA', 'Acetoin', 'Mannitol', 'Mannitol1Phosphate', 'CoA', 'Pext', 'Lactate', 'Ethanol', 'Acetate', 'Butanediol', 'Glucose', 'Acetoin_Ext', 'Mannitol_Ext', 'Formate']
    _SPECIES_LABELS = {'G6P': 'Glucose 6 Phosphate', 'ATP': 'ATP', 'ADP': 'ADP', 'Pint': 'Inorganic Phosphate', 'F6P': 'Fructose 6 Phosphate', 'FBP': 'Fructose Bisphosphate', 'G3P': 'Microbial Metabolism state 7', 'BPG': 'Microbial Metabolism state 8', 'PEP': 'Phosphoenolpyruvate', 'NAD': 'NAD', 'NADH': 'NADH', 'PYR': 'Pyruvate', 'AcetCoA': 'Microbial Metabolism state 13', 'Acetoin': 'Microbial Metabolism state 14', 'Mannitol': 'Microbial Metabolism state 15', 'Mannitol1Phosphate': 'Microbial Metabolism state 16', 'CoA': 'CoA', 'Pext': 'Microbial Metabolism state 18', 'Lactate': 'Microbial Metabolism state 19', 'Ethanol': 'Microbial Metabolism state 20', 'Acetate': 'Microbial Metabolism state 21', 'Butanediol': 'Microbial Metabolism state 22', 'Glucose': 'Microbial Metabolism state 23', 'Acetoin_Ext': 'Microbial Metabolism state 24 extracellular', 'Mannitol_Ext': 'Microbial Metabolism state 25 extracellular', 'Formate': 'Microbial Metabolism state 26'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_6_phosphate': ('G6P', 0.0, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 4.88632508879394, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adp': ('ADP', 20.3856905308319, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_inorganic_phosphate': ('Pint', 38.26, 'native SBML value', 'Initial condition for inorganic phosphate. Maps to bundled SBML symbol `Pint`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('F6P', 0.0, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'inorganic_phosphate': ('Pint', 'native SBML value', 'Inorganic Phosphate. Maps to SBML symbol `Pint`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000572.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
