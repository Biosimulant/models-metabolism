# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Garde2020-Minimal model describing metabolic oscillations in Bacillus subtilis biofilms."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Garde2020MinimalModelDescribingMetabolicOscBiomd0000000932Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Garde2020-Minimal model describing metabolic oscillations in Bacillus subtilis biofilms."""

    _SBML_ID = 'BIOMD0000000932'
    _TITLE = 'Garde2020-Minimal model describing metabolic oscillations in Bacillus subtilis biofilms'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Gp': 'metabolic_pathway_state_1', 'Gi': 'metabolic_pathway_state_2', 'A': 'metabolic_pathway_state_3', 'B': 'metabolic_pathway_state_4'}
    _OBSERVABLES = ['Gp', 'Gi', 'A', 'B']
    _SPECIES_LABELS = {'Gp': 'Metabolic Pathway state 1', 'Gi': 'Metabolic Pathway state 2', 'A': 'Metabolic Pathway state 3', 'B': 'Metabolic Pathway state 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('Gp', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `Gp`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('Gi', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `Gi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('A', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `A`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('B', 100000000000.0, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `B`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('Gp', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Gp`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('Gi', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Gi`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('A', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `A`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('B', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `B`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000932.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
