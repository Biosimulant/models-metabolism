# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Smallbone2013 - Metabolic Control Analysis - Example 1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2013MetabolicControlAnalysisExampleBiomd0000000454Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Smallbone2013 - Metabolic Control Analysis - Example 1."""

    _SBML_ID = 'BIOMD0000000454'
    _TITLE = 'Smallbone2013 - Metabolic Control Analysis - Example 1'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'x1': 'metabolic_pathway_state_1', 'x2': 'metabolic_pathway_state_2', 'x3': 'metabolic_pathway_state_3'}
    _OBSERVABLES = ['x1', 'x2', 'x3']
    _SPECIES_LABELS = {'x1': 'Metabolic Pathway state 1', 'x2': 'Metabolic Pathway state 2', 'x3': 'Metabolic Pathway state 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('x1', 0.05625738310526, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `x1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('x2', 0.76876151899652, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `x2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('x3', 4.23123848100348, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `x3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('x1', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `x1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('x2', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `x2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('x3', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `x3`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000454.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
