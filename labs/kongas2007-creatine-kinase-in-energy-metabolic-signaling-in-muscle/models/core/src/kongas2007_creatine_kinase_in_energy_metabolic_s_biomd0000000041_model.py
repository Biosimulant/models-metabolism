# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Kongas2007 - Creatine Kinase in energy metabolic signaling in muscle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kongas2007CreatineKinaseInEnergyMetabolicSBiomd0000000041Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Kongas2007 - Creatine Kinase in energy metabolic signaling in muscle."""

    _SBML_ID = 'BIOMD0000000041'
    _TITLE = 'Kongas2007 - Creatine Kinase in energy metabolic signaling in muscle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ADPi': 'intracellular_adp', 'ATPi': 'intracellular_atp', 'Cri': 'metabolic_pathway_state_3', 'PCri': 'metabolic_pathway_state_4', 'PCr': 'metabolic_pathway_state_5', 'ADP': 'adp', 'ATP': 'atp', 'Cr': 'metabolic_pathway_state_8', 'Pi': 'metabolic_pathway_state_9', 'P': 'metabolic_pathway_state_10'}
    _OBSERVABLES = ['ADPi', 'ATPi', 'Cri', 'PCri', 'PCr', 'ADP', 'ATP', 'Cr', 'Pi', 'P']
    _SPECIES_LABELS = {'ADPi': 'Intracellular ADP', 'ATPi': 'Intracellular ATP', 'Cri': 'Metabolic Pathway state 3', 'PCri': 'Metabolic Pathway state 4', 'PCr': 'Metabolic Pathway state 5', 'ADP': 'ADP', 'ATP': 'ATP', 'Cr': 'Metabolic Pathway state 8', 'Pi': 'Metabolic Pathway state 9', 'P': 'Metabolic Pathway state 10'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_adp': ('ADPi', 0.0, 'native SBML value', 'Initial condition for intracellular adp. Maps to bundled SBML symbol `ADPi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_intracellular_atp': ('ATPi', 0.0, 'native SBML value', 'Initial condition for intracellular atp. Maps to bundled SBML symbol `ATPi`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('Cri', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `Cri`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_4': ('PCri', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 4. Maps to bundled SBML symbol `PCri`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('PCr', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `PCr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'intracellular_adp': ('ADPi', 'native SBML value', 'Intracellular ADP. Maps to SBML symbol `ADPi`.'), 'intracellular_atp': ('ATPi', 'native SBML value', 'Intracellular ATP. Maps to SBML symbol `ATPi`.'), 'metabolic_pathway_state_3': ('Cri', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Cri`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_4': ('PCri', 'native SBML value', 'Metabolic Pathway state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PCri`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'metabolic_pathway_state_5': ('PCr', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PCr`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000041.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
