# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Galazzo1990_FermentationPathwayKinetics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Galazzo1990FermentationpathwaykineticsBiomd0000000063Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Galazzo1990_FermentationPathwayKinetics."""

    _SBML_ID = 'BIOMD0000000063'
    _TITLE = 'Galazzo1990_FermentationPathwayKinetics'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Glci': 'glucose_inside_the_cell', 'ATP': 'atp', 'G6P': 'glucose_6_phosphate', 'FDP': 'fructose_1_6_phosphate', 'PEP': 'phosphoenol_pyruvate'}
    _OBSERVABLES = ['Glci', 'ATP', 'G6P', 'FDP', 'PEP']
    _SPECIES_LABELS = {'Glci': 'Glucose Inside The Cell', 'ATP': 'ATP', 'G6P': 'Glucose 6 Phosphate', 'FDP': 'Fructose 1 6 Phosphate', 'PEP': 'Phosphoenol Pyruvate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_inside_the_cell': ('Glci', 0.0345, 'native SBML value', 'Initial condition for glucose inside the cell. Maps to bundled SBML symbol `Glci`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 1.19, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glucose_6_phosphate': ('G6P', 1.011, 'native SBML value', 'Initial condition for glucose 6 phosphate. Maps to bundled SBML symbol `G6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_1_6_phosphate': ('FDP', 9.144, 'native SBML value', 'Initial condition for fructose 1 6 phosphate. Maps to bundled SBML symbol `FDP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_phosphoenol_pyruvate': ('PEP', 0.0095, 'native SBML value', 'Initial condition for phosphoenol pyruvate. Maps to bundled SBML symbol `PEP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glucose_inside_the_cell': ('Glci', 'native SBML value', 'Glucose Inside The Cell. Maps to SBML symbol `Glci`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'Glucose 6 Phosphate. Maps to SBML symbol `G6P`.'), 'fructose_1_6_phosphate': ('FDP', 'native SBML value', 'Fructose 1 6 Phosphate. Maps to SBML symbol `FDP`.'), 'phosphoenol_pyruvate': ('PEP', 'native SBML value', 'Phosphoenol Pyruvate. Maps to SBML symbol `PEP`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000063.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
