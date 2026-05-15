# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Teusink2000_Glycolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Teusink2000GlycolysisBiomd0000000064Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Teusink2000_Glycolysis."""

    _SBML_ID = 'BIOMD0000000064'
    _TITLE = 'Teusink2000_Glycolysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'GLCi': 'glucose_in_cytosol', 'G6P': 'glucose_6_phosphate', 'F6P': 'fructose_6_phosphate', 'F16P': 'fructose_1_6_bisphosphate', 'TRIO': 'triose_phosphate', 'BPG': 'observable_1_3_bisphosphoglycerate', 'P3G': 'observable_3_phosphoglycerate', 'P2G': 'observable_2_phosphoglycerate', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'ACE': 'acetaldehyde', 'P': 'high_energy_phosphates', 'NAD': 'nad', 'NADH': 'nadh', 'ATP': 'atp_concentration', 'ADP': 'adp_concentration', 'AMP': 'amp_concentration'}
    _OBSERVABLES = ['GLCi', 'G6P', 'F6P', 'F16P', 'TRIO', 'BPG', 'P3G', 'P2G', 'PEP', 'PYR', 'ACE', 'P', 'NAD', 'NADH', 'ATP', 'ADP', 'AMP']
    _SPECIES_LABELS = {'GLCi': 'Glucose In Cytosol', 'G6P': 'Glucose 6 Phosphate', 'F6P': 'Fructose 6 Phosphate', 'F16P': 'Fructose 1 6 Bisphosphate', 'TRIO': 'Triose Phosphate', 'BPG': '1 3 Bisphosphoglycerate', 'P3G': '3 Phosphoglycerate', 'P2G': '2 Phosphoglycerate', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate', 'ACE': 'Acetaldehyde', 'P': 'High Energy Phosphates', 'NAD': 'NAD', 'NADH': 'NADH', 'ATP': 'ATP Concentration', 'ADP': 'ADP Concentration', 'AMP': 'AMP Concentration'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_in_cytosol': ('GLCi', 0.087, 'native SBML value', 'Initial condition for glucose in cytosol. Maps to bundled SBML symbol `GLCi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 2.45, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('F6P', 0.62, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_1_6_bisphosphate': ('F16P', 5.51, 'native SBML value', 'Initial condition for fructose 1 6 bisphosphate. Maps to bundled SBML symbol `F16P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_triose_phosphate': ('TRIO', 0.96, 'native SBML value', 'Initial condition for triose phosphate. Maps to bundled SBML symbol `TRIO`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glucose_in_cytosol': ('GLCi', 'native SBML value', 'Glucose In Cytosol. Maps to SBML symbol `GLCi`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.'), 'fructose_1_6_bisphosphate': ('F16P', 'native SBML value', 'Fructose 1 6 Bisphosphate. Maps to SBML symbol `F16P`.'), 'triose_phosphate': ('TRIO', 'native SBML value', 'Triose Phosphate. Maps to SBML symbol `TRIO`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000064.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
