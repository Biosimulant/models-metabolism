# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Costa2015 - Central metabolism of E. coli, regulated linlog model (with allosteric regulations)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Costa2015CentralMetabolismOfEColiRegulatedModel1504080004Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Costa2015 - Central metabolism of E. coli, regulated linlog model (with allosteric regulations)."""

    _SBML_ID = 'MODEL1504080004'
    _TITLE = 'Costa2015 - Central metabolism of E. coli, regulated linlog model (with allosteric regulations)'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'cpep': 'phosphoenol_pyruvate', 'cglcex': 'extracellular_glucose', 'cg6p': 'glucose_6_phosphate', 'cpyr': 'microbial_metabolism_state_4', 'cf6p': 'fructose_6_phosphate', 'cg1p': 'glucose_1_phosphate', 'cpg': 'observable_6_phosphogluconate', 'cfdp': 'fructose_1_6_bisphosphate', 'csed7p': 'sedoheptulose_7_phosphate', 'cgap': 'glyceraldehyde_3_phosphate', 'ce4p': 'erythrose_4_phosphate', 'cxyl5p': 'xylulose_5_phosphate', 'crib5p': 'ribose_5_phosphate', 'cdhap': 'dihydroxyacetonephosphate', 'cpgp': 'observable_1_3_diphosphosphoglycerate', 'cpg3': 'observable_3_phosphoglycerate', 'cpg2': 'observable_2_phosphoglycerate', 'cribu5p': 'ribulose_5_phosphate'}
    _OBSERVABLES = ['cpep', 'cglcex', 'cg6p', 'cpyr', 'cf6p', 'cg1p', 'cpg', 'cfdp', 'csed7p', 'cgap', 'ce4p', 'cxyl5p', 'crib5p', 'cdhap', 'cpgp', 'cpg3', 'cpg2', 'cribu5p']
    _SPECIES_LABELS = {'cpep': 'Phosphoenol Pyruvate', 'cglcex': 'Extracellular Glucose', 'cg6p': 'Glucose 6 Phosphate', 'cpyr': 'Microbial Metabolism state 4', 'cf6p': 'Fructose 6 Phosphate', 'cg1p': 'Glucose 1 Phosphate', 'cpg': '6 Phosphogluconate', 'cfdp': 'Fructose 1 6 Bisphosphate', 'csed7p': 'Sedoheptulose 7 Phosphate', 'cgap': 'Glyceraldehyde 3 Phosphate', 'ce4p': 'Erythrose 4 Phosphate', 'cxyl5p': 'Xylulose 5 Phosphate', 'crib5p': 'Ribose 5 Phosphate', 'cdhap': 'Dihydroxyacetonephosphate', 'cpgp': '1 3 Diphosphosphoglycerate', 'cpg3': '3 Phosphoglycerate', 'cpg2': '2 Phosphoglycerate', 'cribu5p': 'Ribulose 5 Phosphate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_phosphoenol_pyruvate': ('cpep', 2.67, 'native SBML value', 'Initial condition for phosphoenol pyruvate. Maps to bundled SBML symbol `cpep`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_extracellular_glucose': ('cglcex', 0.0556, 'native SBML value', 'Initial condition for extracellular glucose. Maps to bundled SBML symbol `cglcex`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('cg6p', 3.48, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `cg6p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_4': ('cpyr', 2.67, 'native SBML value', 'Initial condition for microbial metabolism state 4. Maps to bundled SBML symbol `cpyr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('cf6p', 0.6, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `cf6p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'phosphoenol_pyruvate': ('cpep', 'native SBML value', 'Phosphoenol Pyruvate. Maps to SBML symbol `cpep`.'), 'extracellular_glucose': ('cglcex', 'native SBML value', 'Extracellular Glucose. Maps to SBML symbol `cglcex`.'), 'glucose_6_phosphate': ('cg6p', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `cg6p`.'), 'microbial_metabolism_state_4': ('cpyr', 'native SBML value', 'Microbial Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `cpyr`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'fructose_6_phosphate': ('cf6p', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `cf6p`.')}

    def __init__(self, model_path: str = 'data/MODEL1504080004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
