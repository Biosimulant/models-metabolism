# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Piedrafita2010_MR_System."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Piedrafita2010MrSystemBiomd0000000257Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Piedrafita2010_MR_System."""

    _SBML_ID = 'BIOMD0000000257'
    _TITLE = 'Piedrafita2010_MR_System'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'STU': 'metabolic_pathway_state_1', 'STUS': 'metabolic_pathway_state_2', 'STUST': 'metabolic_pathway_state_3', 'STUSU': 'metabolic_pathway_state_4', 'SU': 'metabolic_pathway_state_5', 'ST': 'metabolic_pathway_state_6', 'SUST': 'metabolic_pathway_state_7', 'SUSTU': 'metabolic_pathway_state_8'}
    _OBSERVABLES = ['STU', 'STUS', 'STUST', 'STUSU', 'SU', 'ST', 'SUST', 'SUSTU']
    _SPECIES_LABELS = {'STU': 'Metabolic Pathway state 1', 'STUS': 'Metabolic Pathway state 2', 'STUST': 'Metabolic Pathway state 3', 'STUSU': 'Metabolic Pathway state 4', 'SU': 'Metabolic Pathway state 5', 'ST': 'Metabolic Pathway state 6', 'SUST': 'Metabolic Pathway state 7', 'SUSTU': 'Metabolic Pathway state 8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('STU', 5.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `STU`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('STUS', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `STUS`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('STUST', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `STUST`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('STUSU', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `STUSU`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('SU', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `SU`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('STU', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `STU`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('STUS', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `STUS`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('STUST', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `STUST`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('STUSU', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `STUSU`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('SU', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `SU`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000257.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
