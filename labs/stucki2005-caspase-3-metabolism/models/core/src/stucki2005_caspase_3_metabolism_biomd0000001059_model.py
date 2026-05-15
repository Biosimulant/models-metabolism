# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Stucki2005 - caspase-3 metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Stucki2005Caspase3MetabolismBiomd0000001059Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Stucki2005 - caspase-3 metabolism."""

    _SBML_ID = 'BIOMD0000001059'
    _TITLE = 'Stucki2005 - caspase-3 metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'pc3': 'metabolic_pathway_state_1', 'c3': 'metabolic_pathway_state_2', 'iap': 'metabolic_pathway_state_3', 'survivin': 'metabolic_pathway_state_4', 'cascade': 'metabolic_pathway_state_5', 'iapc3': 'metabolic_pathway_state_6', 'iapsmac': 'metabolic_pathway_state_7', 'sursmac': 'metabolic_pathway_state_8', 'smacmit': 'metabolic_pathway_state_9', 'smac': 'metabolic_pathway_state_10'}
    _OBSERVABLES = ['pc3', 'c3', 'iap', 'survivin', 'cascade', 'iapc3', 'iapsmac', 'sursmac', 'smacmit', 'smac']
    _SPECIES_LABELS = {'pc3': 'Metabolic Pathway state 1', 'c3': 'Metabolic Pathway state 2', 'iap': 'Metabolic Pathway state 3', 'survivin': 'Metabolic Pathway state 4', 'cascade': 'Metabolic Pathway state 5', 'iapc3': 'Metabolic Pathway state 6', 'iapsmac': 'Metabolic Pathway state 7', 'sursmac': 'Metabolic Pathway state 8', 'smacmit': 'Metabolic Pathway state 9', 'smac': 'Metabolic Pathway state 10'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('pc3', 0.1, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `pc3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('c3', 0.710362, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `c3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('iap', 0.3, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `iap`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('survivin', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `survivin`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('cascade', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `cascade`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('pc3', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `pc3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('c3', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `c3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('iap', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `iap`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('survivin', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `survivin`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('cascade', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `cascade`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000001059.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
