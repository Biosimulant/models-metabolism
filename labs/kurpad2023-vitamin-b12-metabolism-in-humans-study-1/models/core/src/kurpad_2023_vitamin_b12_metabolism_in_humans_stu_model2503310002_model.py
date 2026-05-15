# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Kurpad 2023 - vitamin B12 metabolism in humans [study 1]."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kurpad2023VitaminB12MetabolismInHumansStuModel2503310002Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Kurpad 2023 - vitamin B12 metabolism in humans [study 1]."""

    _SBML_ID = 'MODEL2503310002'
    _TITLE = 'Kurpad 2023 - vitamin B12 metabolism in humans [study 1]'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'C_0': 'metabolic_pathway_state_1', 'C_1': 'metabolic_pathway_state_2', 'C_2': 'metabolic_pathway_state_3'}
    _OBSERVABLES = ['C_0', 'C_1', 'C_2']
    _SPECIES_LABELS = {'C_0': 'Metabolic Pathway state 1', 'C_1': 'Metabolic Pathway state 2', 'C_2': 'Metabolic Pathway state 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('C_0', 1738.3, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `C_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('C_1', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `C_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('C_2', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `C_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('C_0', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `C_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('C_1', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `C_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('C_2', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `C_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2503310002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
