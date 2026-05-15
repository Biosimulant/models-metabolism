# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Tiveci2005 - Calcium dynamics in brain energy metabolism and Alzheimer's disease."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tiveci2005CalciumDynamicsInBrainEnergyMetaModel1409240003Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Tiveci2005 - Calcium dynamics in brain energy metabolism and Alzheimer's disease."""

    _SBML_ID = 'MODEL1409240003'
    _TITLE = "Tiveci2005 - Calcium dynamics in brain energy metabolism and Alzheimer's disease"
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'NAD': 'nad'}
    _OBSERVABLES = ['NAD']
    _SPECIES_LABELS = {'NAD': 'NAD'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_nad': ('NAD', 1.0, 'native SBML value', 'Initial condition for nad. Maps to bundled SBML symbol `NAD`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.')}

    def __init__(self, model_path: str = 'data/MODEL1409240003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
