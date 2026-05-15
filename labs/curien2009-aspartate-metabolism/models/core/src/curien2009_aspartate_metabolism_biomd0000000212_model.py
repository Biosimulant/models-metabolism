# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Curien2009_Aspartate_Metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Curien2009AspartateMetabolismBiomd0000000212Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Curien2009_Aspartate_Metabolism."""

    _SBML_ID = 'BIOMD0000000212'
    _TITLE = 'Curien2009_Aspartate_Metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Lys': 'metabolic_pathway_state_1', 'AspP': 'aspartyl_p', 'Thr': 'threonine', 'ASA': 'aspartate_semialdehyde', 'Hser': 'homoserine', 'PHser': 'phosphohomoserine', 'TS1': 'metabolic_pathway_state_7', 'Ile': 'isoleucine'}
    _OBSERVABLES = ['Lys', 'AspP', 'Thr', 'ASA', 'Hser', 'PHser', 'TS1', 'Ile']
    _SPECIES_LABELS = {'Lys': 'Metabolic Pathway state 1', 'AspP': 'Aspartyl P', 'Thr': 'Threonine', 'ASA': 'Aspartate Semialdehyde', 'Hser': 'Homoserine', 'PHser': 'Phosphohomoserine', 'TS1': 'Metabolic Pathway state 7', 'Ile': 'Isoleucine'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_metabolic_pathway_state_1': ('Lys', 0.0, 'native SBML value', 'Initial condition for metabolic pathway state 1. Maps to bundled SBML symbol `Lys`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_aspartyl_p': ('AspP', 0.0, 'native SBML value', 'Initial condition for aspartyl p. Maps to bundled SBML symbol `AspP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_threonine': ('Thr', 0.0, 'native SBML value', 'Initial condition for threonine. Maps to bundled SBML symbol `Thr`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_aspartate_semialdehyde': ('ASA', 0.0, 'native SBML value', 'Initial condition for aspartate semialdehyde. Maps to bundled SBML symbol `ASA`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_homoserine': ('Hser', 0.0, 'native SBML value', 'Initial condition for homoserine. Maps to bundled SBML symbol `Hser`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'metabolic_pathway_state_1': ('Lys', 'native SBML value', 'Metabolic Pathway state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Lys`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'aspartyl_p': ('AspP', 'native SBML value', 'Aspartyl P. Maps to SBML symbol `AspP`.'), 'threonine': ('Thr', 'native SBML value', 'Threonine. Maps to SBML symbol `Thr`.'), 'aspartate_semialdehyde': ('ASA', 'native SBML value', 'Aspartate Semialdehyde. Maps to SBML symbol `ASA`.'), 'homoserine': ('Hser', 'native SBML value', 'Homoserine. Maps to SBML symbol `Hser`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000212.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
