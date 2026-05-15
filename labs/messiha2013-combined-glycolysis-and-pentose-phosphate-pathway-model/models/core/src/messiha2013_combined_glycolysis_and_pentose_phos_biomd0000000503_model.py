# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Messiha2013 - combined glycolysis and pentose phosphate pathway model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Messiha2013CombinedGlycolysisAndPentosePhosBiomd0000000503Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Messiha2013 - combined glycolysis and pentose phosphate pathway model."""

    _SBML_ID = 'BIOMD0000000503'
    _TITLE = 'Messiha2013 - combined glycolysis and pentose phosphate pathway model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ADP': 'adp', 'ATP': 'atp', 'AcAld': 'glycolysis_state_3', 'BPG': 'glycolysis_state_4', 'DHAP': 'glycolysis_state_5', 'F16bP': 'glycolysis_state_6', 'F6P': 'fructose_6_phosphate', 'G1P': 'glycolysis_state_8', 'G3P': 'glycolysis_state_9', 'G6P': 'glucose_6_phosphate', 'GAP': 'glyceraldehyde_3_phosphate', 'GLC': 'glucose', 'NAD': 'nad', 'P2G': 'glycolysis_state_14', 'P3G': 'glycolysis_state_15', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'T6P': 'glycolysis_state_18', 'UDP': 'glycolysis_state_19', 'UTP': 'glycolysis_state_20', 'E4P': 'glycolysis_state_21', 'G6L': 'glycolysis_state_22', 'NADPH': 'nadph', 'P6G': 'glycolysis_state_24', 'R5P': 'glycolysis_state_25', 'Ru5P': 'glycolysis_state_26', 'S7P': 'glycolysis_state_27', 'X5P': 'glycolysis_state_28'}
    _OBSERVABLES = ['ADP', 'ATP', 'AcAld', 'BPG', 'DHAP', 'F16bP', 'F6P', 'G1P', 'G3P', 'G6P', 'GAP', 'GLC', 'NAD', 'P2G', 'P3G', 'PEP', 'PYR', 'T6P', 'UDP', 'UTP', 'E4P', 'G6L', 'NADPH', 'P6G', 'R5P', 'Ru5P', 'S7P', 'X5P']
    _SPECIES_LABELS = {'ADP': 'ADP', 'ATP': 'ATP', 'AcAld': 'Glycolysis state 3', 'BPG': 'Glycolysis state 4', 'DHAP': 'Glycolysis state 5', 'F16bP': 'Glycolysis state 6', 'F6P': 'Fructose 6 Phosphate', 'G1P': 'Glycolysis state 8', 'G3P': 'Glycolysis state 9', 'G6P': 'Glucose 6 Phosphate', 'GAP': 'Glyceraldehyde 3 Phosphate', 'GLC': 'Glucose', 'NAD': 'NAD', 'P2G': 'Glycolysis state 14', 'P3G': 'Glycolysis state 15', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate', 'T6P': 'Glycolysis state 18', 'UDP': 'Glycolysis state 19', 'UTP': 'Glycolysis state 20', 'E4P': 'Glycolysis state 21', 'G6L': 'Glycolysis state 22', 'NADPH': 'NADPH', 'P6G': 'Glycolysis state 24', 'R5P': 'Glycolysis state 25', 'Ru5P': 'Glycolysis state 26', 'S7P': 'Glycolysis state 27', 'X5P': 'Glycolysis state 28'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('ADP', 1.29, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 4.29, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_3': ('AcAld', 0.178140579850657, 'native SBML value', 'Initial condition for glycolysis state 3. Maps to bundled SBML symbol `AcAld`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_4': ('BPG', 0.000736873499865602, 'native SBML value', 'Initial condition for glycolysis state 4. Maps to bundled SBML symbol `BPG`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_5': ('DHAP', 1.1613768527467, 'native SBML value', 'Initial condition for glycolysis state 5. Maps to bundled SBML symbol `DHAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glycolysis_state_3': ('AcAld', 'native SBML value', 'Glycolysis state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `AcAld`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_4': ('BPG', 'native SBML value', 'Glycolysis state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `BPG`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_5': ('DHAP', 'native SBML value', 'Glycolysis state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `DHAP`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000503.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
