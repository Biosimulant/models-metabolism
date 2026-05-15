# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Lai2007_O2_Transport_Metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lai2007O2TransportMetabolismBiomd0000000248Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Lai2007_O2_Transport_Metabolism."""

    _SBML_ID = 'BIOMD0000000248'
    _TITLE = 'Lai2007_O2_Transport_Metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ATP': 'atp', 'PCr': 'metabolic_pathway_state_2', 'ADP': 'adp', 'Cr': 'metabolic_pathway_state_4', 'Pi': 'metabolic_pathway_state_5', 'CTcap': 'metabolic_pathway_state_6', 'CTtis': 'metabolic_pathway_state_7'}
    _OBSERVABLES = ['ATP', 'PCr', 'ADP', 'Cr', 'Pi', 'CTcap', 'CTtis']
    _SPECIES_LABELS = {'ATP': 'ATP', 'PCr': 'Metabolic Pathway state 2', 'ADP': 'ADP', 'Cr': 'Metabolic Pathway state 4', 'Pi': 'Metabolic Pathway state 5', 'CTcap': 'Metabolic Pathway state 6', 'CTtis': 'Metabolic Pathway state 7'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atp': ('ATP', 8.198857, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_2': ('PCr', 40.98942, 'native SBML value', 'Initial condition for metabolic pathway state 2. Maps to bundled SBML symbol `PCr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adp': ('ADP', 0.001142, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('Cr', 1.01056, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `Cr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('Pi', 0.5, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `Pi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'metabolic_pathway_state_2': ('PCr', 'native SBML value', 'Metabolic Pathway state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PCr`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'metabolic_pathway_state_4': ('Cr', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Cr`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('Pi', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Pi`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000248.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
