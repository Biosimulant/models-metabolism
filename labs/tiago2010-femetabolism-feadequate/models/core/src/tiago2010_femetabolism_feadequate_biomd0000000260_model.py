# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Tiago2010_FeMetabolism_FeAdequate."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tiago2010FemetabolismFeadequateBiomd0000000260Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Tiago2010_FeMetabolism_FeAdequate."""

    _SBML_ID = 'BIOMD0000000260'
    _TITLE = 'Tiago2010_FeMetabolism_FeAdequate'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'s1': 'iron_in_plasma', 's2': 'iron_in_bone_marrow', 's3': 'iron_metabolism_state_3', 's4': 'iron_in_spleen', 's5': 'iron_in_liver', 's6': 'iron_in_muscle', 's7': 'iron_in_duodenum', 's8': 'iron_in_integument', 's9': 'iron_in_intestine', 's10': 'iron_ions_outside', 's11': 'iron_in_heart', 's12': 'iron_in_lungs', 's13': 'iron_in_kidneys', 's14': 'iron_in_testes', 's15': 'iron_in_stomach', 's16': 'iron_metabolism_state_16', 's17': 'iron_in_brain'}
    _OBSERVABLES = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17']
    _SPECIES_LABELS = {'s1': 'Iron In Plasma', 's2': 'Iron In Bone Marrow', 's3': 'Iron Metabolism state 3', 's4': 'Iron In Spleen', 's5': 'Iron In Liver', 's6': 'Iron In Muscle', 's7': 'Iron In Duodenum', 's8': 'Iron In Integument', 's9': 'Iron In Intestine', 's10': 'Iron Ions Outside', 's11': 'Iron In Heart', 's12': 'Iron In Lungs', 's13': 'Iron In Kidneys', 's14': 'Iron In Testes', 's15': 'Iron In Stomach', 's16': 'Iron Metabolism state 16', 's17': 'Iron In Brain'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_iron_in_plasma': ('s1', 100.0, 'native SBML value', 'Initial condition for iron in plasma. Maps to bundled SBML symbol `s1`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_in_bone_marrow': ('s2', 0.0, 'native SBML value', 'Initial condition for iron in bone marrow. Maps to bundled SBML symbol `s2`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_metabolism_state_3': ('s3', 0.0, 'native SBML value', 'Initial condition for iron metabolism state 3. Maps to bundled SBML symbol `s3`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_in_spleen': ('s4', 0.0, 'native SBML value', 'Initial condition for iron in spleen. Maps to bundled SBML symbol `s4`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_iron_in_liver': ('s5', 0.0, 'native SBML value', 'Initial condition for iron in liver. Maps to bundled SBML symbol `s5`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'iron_in_plasma': ('s1', 'native SBML value', 'Iron In Plasma. Maps to SBML symbol `s1`.'), 'iron_in_bone_marrow': ('s2', 'native SBML value', 'Iron In Bone Marrow. Maps to SBML symbol `s2`.'), 'iron_metabolism_state_3': ('s3', 'native SBML value', 'Iron Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `s3`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'iron_in_spleen': ('s4', 'native SBML value', 'Iron In Spleen. Maps to SBML symbol `s4`.'), 'iron_in_liver': ('s5', 'native SBML value', 'Iron In Liver. Maps to SBML symbol `s5`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000260.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
