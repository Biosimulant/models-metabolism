# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Larbat2016.2 - Modeling the diversion of primary carbon flux into secondary metabolism under variable nitrate and light or dark conditions (Light Dark Cycles)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Larbat20162ModelingTheDiversionOfPrimaryCBiomd0000000858Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Larbat2016.2 - Modeling the diversion of primary carbon flux into secondary metabolism under variable nitrate and light or dark conditions (Light Dark Cycles)."""

    _SBML_ID = 'BIOMD0000000858'
    _TITLE = 'Larbat2016.2 - Modeling the diversion of primary carbon flux into secondary metabolism under variable nitrate and light or dark conditions (Light Dark Cycles)'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'sucr': 'metabolic_pathway_state_1', 'EtrioseP': 'metabolic_pathway_state_2', 'Ephe': 'metabolic_pathway_state_3', 'N': 'metabolic_pathway_state_4', 'starch': 'metabolic_pathway_state_5', 'Enitrate': 'metabolic_pathway_state_6', 'trioseP': 'metabolic_pathway_state_7', 'Estarch': 'metabolic_pathway_state_8'}
    _OBSERVABLES = ['sucr', 'EtrioseP', 'Ephe', 'N', 'starch', 'Enitrate', 'trioseP', 'Estarch']
    _SPECIES_LABELS = {'sucr': 'Metabolic Pathway state 1', 'EtrioseP': 'Metabolic Pathway state 2', 'Ephe': 'Metabolic Pathway state 3', 'N': 'Metabolic Pathway state 4', 'starch': 'Metabolic Pathway state 5', 'Enitrate': 'Metabolic Pathway state 6', 'trioseP': 'Metabolic Pathway state 7', 'Estarch': 'Metabolic Pathway state 8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('sucr', 0.748, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `sucr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('EtrioseP', 2.825, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `EtrioseP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('Ephe', 9.751e-07, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `Ephe`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('N', 4.998, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `N`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('starch', 6.041, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `starch`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('sucr', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `sucr`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_2': ('EtrioseP', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `EtrioseP`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_3': ('Ephe', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Ephe`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('N', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `N`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('starch', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `starch`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000858.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
