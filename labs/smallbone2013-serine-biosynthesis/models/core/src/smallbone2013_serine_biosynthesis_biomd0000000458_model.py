# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Smallbone2013 - Serine biosynthesis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smallbone2013SerineBiosynthesisBiomd0000000458Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Smallbone2013 - Serine biosynthesis."""

    _SBML_ID = 'BIOMD0000000458'
    _TITLE = 'Smallbone2013 - Serine biosynthesis'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'php': 'phosphohydroxypyruvate', 'pser': 'phosphoserine'}
    _OBSERVABLES = ['php', 'pser']
    _SPECIES_LABELS = {'php': 'Phosphohydroxypyruvate', 'pser': 'Phosphoserine'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_phosphohydroxypyruvate': ('php', 0.6, 'native SBML value', 'Initial condition for phosphohydroxypyruvate. Maps to bundled SBML symbol `php`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_phosphoserine': ('pser', 0.09, 'native SBML value', 'Initial condition for phosphoserine. Maps to bundled SBML symbol `pser`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'phosphohydroxypyruvate': ('php', 'native SBML value', 'Phosphohydroxypyruvate. Maps to SBML symbol `php`.'), 'phosphoserine': ('pser', 'native SBML value', 'Phosphoserine. Maps to SBML symbol `pser`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000458.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
