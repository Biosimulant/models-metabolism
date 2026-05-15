# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Adams2019 - The regulatory role of shikimate in plant phenylalanine metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Adams2019TheRegulatoryRoleOfShikimateInPlBiomd0000000847Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Adams2019 - The regulatory role of shikimate in plant phenylalanine metabolism."""

    _SBML_ID = 'BIOMD0000000847'
    _TITLE = 'Adams2019 - The regulatory role of shikimate in plant phenylalanine metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'X_1': 'phenylalanine_pathway_state_1', 'X_2': 'phenylalanine_pathway_state_2', 'X_3': 'phenylalanine_pathway_state_3', 'X_4': 'phenylalanine_pathway_state_4'}
    _OBSERVABLES = ['X_1', 'X_2', 'X_3', 'X_4']
    _SPECIES_LABELS = {'X_1': 'Phenylalanine Pathway state 1', 'X_2': 'Phenylalanine Pathway state 2', 'X_3': 'Phenylalanine Pathway state 3', 'X_4': 'Phenylalanine Pathway state 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_phenylalanine_pathway_state_1': ('X_1', 0.0, 'native SBML value', 'Initial condition for phenylalanine pathway state 1. Maps to bundled SBML symbol `X_1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_phenylalanine_pathway_state_2': ('X_2', 0.0, 'native SBML value', 'Initial condition for phenylalanine pathway state 2. Maps to bundled SBML symbol `X_2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_phenylalanine_pathway_state_3': ('X_3', 0.0, 'native SBML value', 'Initial condition for phenylalanine pathway state 3. Maps to bundled SBML symbol `X_3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_phenylalanine_pathway_state_4': ('X_4', 0.0, 'native SBML value', 'Initial condition for phenylalanine pathway state 4. Maps to bundled SBML symbol `X_4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'phenylalanine_pathway_state_1': ('X_1', 'native SBML value', 'Phenylalanine Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `X_1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'phenylalanine_pathway_state_2': ('X_2', 'native SBML value', 'Phenylalanine Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `X_2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'phenylalanine_pathway_state_3': ('X_3', 'native SBML value', 'Phenylalanine Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `X_3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'phenylalanine_pathway_state_4': ('X_4', 'native SBML value', 'Phenylalanine Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `X_4`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000847.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
