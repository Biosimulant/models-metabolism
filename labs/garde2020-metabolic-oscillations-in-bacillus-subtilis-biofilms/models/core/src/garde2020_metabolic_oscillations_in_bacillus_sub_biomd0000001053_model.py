# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Garde2020 - metabolic oscillations in Bacillus subtilis biofilms."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Garde2020MetabolicOscillationsInBacillusSubBiomd0000001053Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Garde2020 - metabolic oscillations in Bacillus subtilis biofilms."""

    _SBML_ID = 'BIOMD0000001053'
    _TITLE = 'Garde2020 - metabolic oscillations in Bacillus subtilis biofilms'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Gp': 'metabolic_pathway_state_1', 'Ai': 'metabolic_pathway_state_2', 'Am': 'metabolic_pathway_state_3', 'Ap': 'metabolic_pathway_state_4', 'Gm': 'metabolic_pathway_state_5', 'Gi': 'metabolic_pathway_state_6'}
    _OBSERVABLES = ['Gp', 'Ai', 'Am', 'Ap', 'Gm', 'Gi']
    _SPECIES_LABELS = {'Gp': 'Metabolic Pathway state 1', 'Ai': 'Metabolic Pathway state 2', 'Am': 'Metabolic Pathway state 3', 'Ap': 'Metabolic Pathway state 4', 'Gm': 'Metabolic Pathway state 5', 'Gi': 'Metabolic Pathway state 6'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('Gp', 0.999999999999999, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `Gp`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('Ai', 0.999999999999999, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `Ai`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('Am', 0.999999999999999, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `Am`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('Ap', 0.999999999999999, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `Ap`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('Gm', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `Gm`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('Gp', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Gp`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('Ai', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Ai`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('Am', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Am`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('Ap', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Ap`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('Gm', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Gm`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000001053.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
