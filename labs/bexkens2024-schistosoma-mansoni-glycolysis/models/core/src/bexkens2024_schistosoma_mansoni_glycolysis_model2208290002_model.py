# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Bexkens2024 - Schistosoma mansoni glycolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bexkens2024SchistosomaMansoniGlycolysisModel2208290002Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Bexkens2024 - Schistosoma mansoni glycolysis."""

    _SBML_ID = 'MODEL2208290002'
    _TITLE = 'Bexkens2024 - Schistosoma mansoni glycolysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ATP': 'atp', 'GLCi': 'intracellular_glucose', 'ADP': 'adp', 'G6P': 'glucose_6_phosphate', 'F6P': 'fructose_6_phosphate', 'F16BP': 'glycolysis_state_6', 'TRIO': 'triose_phosphate', 'NAD': 'nad', 'BPG': 'glycolysis_state_9', 'NADH': 'nadh', 'P3G': 'glycolysis_state_11', 'P2G': 'glycolysis_state_12', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'AMP': 'amp'}
    _OBSERVABLES = ['ATP', 'GLCi', 'ADP', 'G6P', 'F6P', 'F16BP', 'TRIO', 'NAD', 'BPG', 'NADH', 'P3G', 'P2G', 'PEP', 'PYR', 'AMP']
    _SPECIES_LABELS = {'ATP': 'ATP', 'GLCi': 'Intracellular Glucose', 'ADP': 'ADP', 'G6P': 'Glucose 6 Phosphate', 'F6P': 'Fructose 6 Phosphate', 'F16BP': 'Glycolysis state 6', 'TRIO': 'Triose Phosphate', 'NAD': 'NAD', 'BPG': 'Glycolysis state 9', 'NADH': 'NADH', 'P3G': 'Glycolysis state 11', 'P2G': 'Glycolysis state 12', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate', 'AMP': 'AMP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atp': ('ATP', 1.18, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_intracellular_glucose': ('GLCi', 0.0, 'native SBML value', 'Initial condition for intracellular glucose. Maps to bundled SBML symbol `GLCi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adp': ('ADP', 1.74, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 0.00384, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('F6P', 0.00118, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'intracellular_glucose': ('GLCi', 'native SBML value', 'Intracellular Glucose. Maps to SBML symbol `GLCi`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.')}

    def __init__(self, model_path: str = 'data/MODEL2208290002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
