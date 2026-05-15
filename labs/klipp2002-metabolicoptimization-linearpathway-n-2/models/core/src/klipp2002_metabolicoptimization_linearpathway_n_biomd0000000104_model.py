# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Klipp2002_MetabolicOptimization_linearPathway(n=2)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Klipp2002MetabolicoptimizationLinearpathwayNBiomd0000000104Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Klipp2002_MetabolicOptimization_linearPathway(n=2)."""

    _SBML_ID = 'BIOMD0000000104'
    _TITLE = 'Klipp2002_MetabolicOptimization_linearPathway(n=2)'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'species_0': 'metabolic_pathway_state_1', 'species_1': 'metabolic_pathway_state_2', 'species_2': 'metabolic_pathway_state_3', 'species_3': 'metabolic_pathway_state_4', 'species_4': 'metabolic_pathway_state_5'}
    _OBSERVABLES = ['species_0', 'species_1', 'species_2', 'species_3', 'species_4']
    _SPECIES_LABELS = {'species_0': 'Metabolic Pathway state 1', 'species_1': 'Metabolic Pathway state 2', 'species_2': 'Metabolic Pathway state 3', 'species_3': 'Metabolic Pathway state 4', 'species_4': 'Metabolic Pathway state 5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('species_0', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `species_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('species_1', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `species_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('species_2', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `species_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('species_3', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `species_3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('species_4', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `species_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('species_0', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('species_1', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('species_2', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('species_3', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('species_4', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `species_4`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000104.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
