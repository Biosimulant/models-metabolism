# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Pritchard2002_glycolysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pritchard2002GlycolysisBiomd0000000172Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Pritchard2002_glycolysis."""

    _SBML_ID = 'BIOMD0000000172'
    _TITLE = 'Pritchard2002_glycolysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'GLCi': 'intracellular_glucose', 'ATP': 'atp', 'G6P': 'glucose_6_phosphate', 'ADP': 'adp', 'F6P': 'fructose_6_phosphate', 'F16bP': 'glycolysis_state_6', 'AMP': 'amp', 'DHAP': 'glycerone_phosphate', 'GAP': 'gra3p', 'NAD': 'nad', 'BPG': 'glycolysis_state_11', 'NADH': 'nadh', 'P3G': 'gri3p', 'P2G': 'gri2p', 'PEP': 'phosphoenolpyruvate', 'PYR': 'pyruvate', 'AcAld': 'acetaldehyde'}
    _OBSERVABLES = ['GLCi', 'ATP', 'G6P', 'ADP', 'F6P', 'F16bP', 'AMP', 'DHAP', 'GAP', 'NAD', 'BPG', 'NADH', 'P3G', 'P2G', 'PEP', 'PYR', 'AcAld']
    _SPECIES_LABELS = {'GLCi': 'Intracellular Glucose', 'ATP': 'ATP', 'G6P': 'glucose 6 phosphate', 'ADP': 'ADP', 'F6P': 'Fructose 6 Phosphate', 'F16bP': 'Glycolysis state 6', 'AMP': 'AMP', 'DHAP': 'Glycerone Phosphate', 'GAP': 'Gra3p', 'NAD': 'NAD', 'BPG': 'Glycolysis state 11', 'NADH': 'NADH', 'P3G': 'Gri3p', 'P2G': 'Gri2p', 'PEP': 'Phosphoenolpyruvate', 'PYR': 'Pyruvate', 'AcAld': 'Acetaldehyde'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_glucose': ('GLCi', 0.097652231064563, 'native SBML value', 'Initial condition for intracellular glucose. Maps to bundled SBML symbol `GLCi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 2.52512746499271, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 2.67504014044787, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adp': ('ADP', 1.28198768168719, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('F6P', 0.624976405532373, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'intracellular_glucose': ('GLCi', 'native SBML value', 'Intracellular Glucose. Maps to SBML symbol `GLCi`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'glucose 6 phosphate. Maps to SBML symbol `G6P`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000172.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
