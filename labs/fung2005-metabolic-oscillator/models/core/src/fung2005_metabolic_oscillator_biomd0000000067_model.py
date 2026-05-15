# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Fung2005_Metabolic_Oscillator."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fung2005MetabolicOscillatorBiomd0000000067Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Fung2005_Metabolic_Oscillator."""

    _SBML_ID = 'BIOMD0000000067'
    _TITLE = 'Fung2005_Metabolic_Oscillator'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'AcCoA': 'metabolic_pathway_state_1', 'AcP': 'acetyl_phosphate', 'OAc': 'metabolic_pathway_state_3', 'HOAc': 'protonated_acetate', 'LacI': 'lactate_repressor', 'Acs': 'metabolic_pathway_state_6', 'Pta': 'phosphate_acetyl_transferase'}
    _OBSERVABLES = ['AcCoA', 'AcP', 'OAc', 'HOAc', 'LacI', 'Acs', 'Pta']
    _SPECIES_LABELS = {'AcCoA': 'Metabolic Pathway state 1', 'AcP': 'Acetyl Phosphate', 'OAc': 'Metabolic Pathway state 3', 'HOAc': 'Protonated Acetate', 'LacI': 'lactate Repressor', 'Acs': 'Metabolic Pathway state 6', 'Pta': 'Phosphate Acetyl Transferase'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('AcCoA', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `AcCoA`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_acetyl_phosphate': ('AcP', 0.0, 'native SBML value', 'Initial condition for acetyl phosphate. Maps to bundled SBML symbol `AcP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_3': ('OAc', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 3. Maps to bundled SBML symbol `OAc`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_protonated_acetate': ('HOAc', 0.0, 'native SBML value', 'Initial condition for protonated acetate. Maps to bundled SBML symbol `HOAc`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lactate_repressor': ('LacI', 0.0, 'native SBML value', 'Initial condition for lactate repressor. Maps to bundled SBML symbol `LacI`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('AcCoA', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `AcCoA`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'acetyl_phosphate': ('AcP', 'native SBML value', 'Acetyl Phosphate. Maps to SBML symbol `AcP`.'), 'metabolic_pathway_state_3': ('OAc', 'native SBML value', 'Metabolic Pathway state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `OAc`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'protonated_acetate': ('HOAc', 'native SBML value', 'Protonated Acetate. Maps to SBML symbol `HOAc`.'), 'lactate_repressor': ('LacI', 'native SBML value', 'lactate Repressor. Maps to SBML symbol `LacI`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000067.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
