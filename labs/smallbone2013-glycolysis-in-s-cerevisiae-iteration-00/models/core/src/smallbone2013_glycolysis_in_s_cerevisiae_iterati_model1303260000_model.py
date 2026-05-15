# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Smallbone2013 - Glycolysis in S.cerevisiae - Iteration 00."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2013GlycolysisInSCerevisiaeIteratiModel1303260000Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Smallbone2013 - Glycolysis in S.cerevisiae - Iteration 00."""

    _SBML_ID = 'MODEL1303260000'
    _TITLE = 'Smallbone2013 - Glycolysis in S.cerevisiae - Iteration 00'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ADP': 'adp', 'ATP': 'atp', 'AcAld': 'acetaldehyde', 'BPG': 'observable_1_3_bisphosphoglycerate', 'DHAP': 'dihydroxyacetone_phosphate', 'F16bP': 'fructose_1_6_bisphosphate', 'F6P': 'fructose_6_phosphate', 'G6P': 'glucose_6_phosphate', 'GAP': 'glyceraldehyde_3_phosphate', 'GLC': 'glucose', 'NAD': 'nad', 'P2G': 'observable_2_phosphoglycerate', 'P3G': 'observable_3_phosphoglycerate', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate'}
    _OBSERVABLES = ['ADP', 'ATP', 'AcAld', 'BPG', 'DHAP', 'F16bP', 'F6P', 'G6P', 'GAP', 'GLC', 'NAD', 'P2G', 'P3G', 'PEP', 'PYR']
    _SPECIES_LABELS = {'ADP': 'ADP', 'ATP': 'ATP', 'AcAld': 'Acetaldehyde', 'BPG': '1 3 Bisphosphoglycerate', 'DHAP': 'Dihydroxyacetone Phosphate', 'F16bP': 'Fructose 1 6 Bisphosphate', 'F6P': 'Fructose 6 Phosphate', 'G6P': 'Glucose 6 Phosphate', 'GAP': 'Glyceraldehyde 3 Phosphate', 'GLC': 'Glucose', 'NAD': 'NAD', 'P2G': '2 Phosphoglycerate', 'P3G': '3 Phosphoglycerate', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('ADP', 1.29, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 4.29, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_acetaldehyde': ('AcAld', 0.178140579850657, 'native SBML value', 'Initial condition for acetaldehyde. Maps to bundled SBML symbol `AcAld`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_observable_1_3_bisphosphoglycerate': ('BPG', 0.000736873499865602, 'native SBML value', 'Initial condition for observable 1 3 bisphosphoglycerate. Maps to bundled SBML symbol `BPG`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_dihydroxyacetone_phosphate': ('DHAP', 0.290344213186674, 'native SBML value', 'Initial condition for dihydroxyacetone phosphate. Maps to bundled SBML symbol `DHAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'acetaldehyde': ('AcAld', 'native SBML value', 'Acetaldehyde. Maps to SBML symbol `AcAld`.'), 'observable_1_3_bisphosphoglycerate': ('BPG', 'native SBML value', '1 3 Bisphosphoglycerate. Maps to SBML symbol `BPG`.'), 'dihydroxyacetone_phosphate': ('DHAP', 'native SBML value', 'Dihydroxyacetone Phosphate. Maps to SBML symbol `DHAP`.')}

    def __init__(self, model_path: str = 'data/MODEL1303260000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
