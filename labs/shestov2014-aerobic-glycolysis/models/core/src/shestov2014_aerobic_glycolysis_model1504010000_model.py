# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Shestov2014 - aerobic glycolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shestov2014AerobicGlycolysisModel1504010000Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Shestov2014 - aerobic glycolysis."""

    _SBML_ID = 'MODEL1504010000'
    _TITLE = 'Shestov2014 - aerobic glycolysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'GLU': 'glycolysis_state_1', 'G6P': 'glucose_6_phosphate', 'F6P': 'fructose_6_phosphate', 'FBP': 'fructose_bisphosphate', 'DHAP': 'glycolysis_state_5', 'GAP': 'glyceraldehyde_3_phosphate', 'BPG': 'glycolysis_state_7', '_3PG': 'glycolysis_state_8', '_2PG': 'glycolysis_state_9', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'LAC': 'lactate', 'ATP': 'atp', 'ADP': 'adp', 'AMP': 'amp', 'P': 'glycolysis_state_16', 'NADH': 'nadh', 'NAD': 'nad', 'PCR': 'glycolysis_state_19', 'CR': 'glycolysis_state_20', 'O2': 'glycolysis_state_21'}
    _OBSERVABLES = ['GLU', 'G6P', 'F6P', 'FBP', 'DHAP', 'GAP', 'BPG', '_3PG', '_2PG', 'PEP', 'PYR', 'LAC', 'ATP', 'ADP', 'AMP', 'P', 'NADH', 'NAD', 'PCR', 'CR', 'O2']
    _SPECIES_LABELS = {'GLU': 'Glycolysis state 1', 'G6P': 'Glucose 6 Phosphate', 'F6P': 'Fructose 6 Phosphate', 'FBP': 'Fructose Bisphosphate', 'DHAP': 'Glycolysis state 5', 'GAP': 'Glyceraldehyde 3 Phosphate', 'BPG': 'Glycolysis state 7', '_3PG': 'Glycolysis state 8', '_2PG': 'Glycolysis state 9', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate', 'LAC': 'Lactate', 'ATP': 'ATP', 'ADP': 'ADP', 'AMP': 'AMP', 'P': 'Glycolysis state 16', 'NADH': 'NADH', 'NAD': 'NAD', 'PCR': 'Glycolysis state 19', 'CR': 'Glycolysis state 20', 'O2': 'O2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glycolysis_state_1': ('GLU', 2.5909, 'native SBML value', 'Initial condition for glycolysis state 1. Maps to bundled SBML symbol `GLU`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 0.2263, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('F6P', 0.0701, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_bisphosphate': ('FBP', 0.45, 'native SBML value', 'Initial condition for fructose bisphosphate. Maps to bundled SBML symbol `FBP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_5': ('DHAP', 0.0244, 'native SBML value', 'Initial condition for glycolysis state 5. Maps to bundled SBML symbol `DHAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glycolysis_state_1': ('GLU', 'native SBML value', 'Glycolysis state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `GLU`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.'), 'fructose_bisphosphate': ('FBP', 'native SBML value', 'Fructose Bisphosphate. Maps to SBML symbol `FBP`.'), 'glycolysis_state_5': ('DHAP', 'native SBML value', 'Glycolysis state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `DHAP`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL1504010000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
