# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for vanEunen2012 - Yeast Glycolysis (glucose upshift)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vaneunen2012YeastGlycolysisGlucoseUpshiftModel1403250001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for vanEunen2012 - Yeast Glycolysis (glucose upshift)."""

    _SBML_ID = 'MODEL1403250001'
    _TITLE = 'vanEunen2012 - Yeast Glycolysis (glucose upshift)'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'species_1': 'intracellular_glucose', 'species_2': 'glucose_6_phosphate', 'species_3': 'fructose_6_phosphate', 'species_4': 'fructose_1_6_bisphosphate', 'species_5': 'triose_phosphate', 'species_6': 'glycolysis_state_6', 'species_7': 'nad', 'species_8': 'nadh', 'species_9': 'p3g', 'species_10': 'p2g', 'species_11': 'phosphoenolpyruvate', 'species_12': 'pyruvate', 'species_13': 'glycolysis_state_13'}
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'species_5', 'species_6', 'species_7', 'species_8', 'species_9', 'species_10', 'species_11', 'species_12', 'species_13']
    _SPECIES_LABELS = {'species_1': 'intracellular glucose', 'species_2': 'glucose 6 phosphate', 'species_3': 'fructose 6 phosphate', 'species_4': 'fructose 1 6 bisphosphate', 'species_5': 'triose phosphate', 'species_6': 'Glycolysis state 6', 'species_7': 'NAD', 'species_8': 'NADH', 'species_9': 'P3g', 'species_10': 'P2g', 'species_11': 'phosphoenolpyruvate', 'species_12': 'pyruvate', 'species_13': 'Glycolysis state 13'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_glucose': ('species_1', 0.0576023, 'native SBML value', 'Initial condition for intracellular glucose. Maps to bundled SBML symbol `species_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('species_2', 0.121566, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `species_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_6_phosphate': ('species_3', 0.0263653, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `species_3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_1_6_bisphosphate': ('species_4', 0.0928847, 'native SBML value', 'Initial condition for fructose 1 6 bisphosphate. Maps to bundled SBML symbol `species_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_triose_phosphate': ('species_5', 0.336706, 'native SBML value', 'Initial condition for triose phosphate. Maps to bundled SBML symbol `species_5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'intracellular_glucose': ('species_1', 'native SBML value', 'intracellular glucose. Maps to SBML symbol `species_1`.'), 'glucose_6_phosphate': ('species_2', 'native SBML value', 'glucose 6 phosphate. Maps to SBML symbol `species_2`.'), 'fructose_6_phosphate': ('species_3', 'native SBML value', 'fructose 6 phosphate. Maps to SBML symbol `species_3`.'), 'fructose_1_6_bisphosphate': ('species_4', 'native SBML value', 'fructose 1 6 bisphosphate. Maps to SBML symbol `species_4`.'), 'triose_phosphate': ('species_5', 'native SBML value', 'triose phosphate. Maps to SBML symbol `species_5`.')}

    def __init__(self, model_path: str = 'data/MODEL1403250001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
