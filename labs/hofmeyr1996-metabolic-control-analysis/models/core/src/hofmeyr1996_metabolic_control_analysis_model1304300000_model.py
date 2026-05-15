# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Hofmeyr1996 - metabolic control analysis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hofmeyr1996MetabolicControlAnalysisModel1304300000Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Hofmeyr1996 - metabolic control analysis."""

    _SBML_ID = 'MODEL1304300000'
    _TITLE = 'Hofmeyr1996 - metabolic control analysis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'s1': 'metabolic_pathway_state_1', 's2': 'metabolic_pathway_state_2', 's3': 'metabolic_pathway_state_3'}
    _OBSERVABLES = ['s1', 's2', 's3']
    _SPECIES_LABELS = {'s1': 'Metabolic Pathway state 1', 's2': 'Metabolic Pathway state 2', 's3': 'Metabolic Pathway state 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('s1', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `s1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('s2', 2.5, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `s2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('s3', 2.5, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `s3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('s1', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `s1`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('s2', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `s2`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('s3', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `s3`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL1304300000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
