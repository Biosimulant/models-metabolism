# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Curto1998 - purine metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Curto1998PurineMetabolismBiomd0000000015Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Curto1998 - purine metabolism."""

    _SBML_ID = 'BIOMD0000000015'
    _TITLE = 'Curto1998 - purine metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'PRPP': 'phosphoribosylpyrophosphate', 'IMP': 'inosine_monophosphate', 'SAMP': 'adenylosuccinate', 'ATP': 'atp', 'SAM': 's_adenosyl_l_methionine', 'Ade': 'purine_metabolism_state_6', 'XMP': 'xanthosine_monophosphate', 'GTP': 'purine_metabolism_state_8', 'dATP': 'deoxy_atp', 'dGTP': 'purine_metabolism_state_10', 'RNA': 'rna', 'DNA': 'dna', 'HX': 'purine_metabolism_state_13', 'Xa': 'purine_metabolism_state_14', 'Gua': 'purine_metabolism_state_15', 'UA': 'purine_metabolism_state_16'}
    _OBSERVABLES = ['PRPP', 'IMP', 'SAMP', 'ATP', 'SAM', 'Ade', 'XMP', 'GTP', 'dATP', 'dGTP', 'RNA', 'DNA', 'HX', 'Xa', 'Gua', 'UA']
    _SPECIES_LABELS = {'PRPP': 'Phosphoribosylpyrophosphate', 'IMP': 'Inosine Monophosphate', 'SAMP': 'Adenylosuccinate', 'ATP': 'ATP', 'SAM': 'S Adenosyl L Methionine', 'Ade': 'Purine Metabolism state 6', 'XMP': 'Xanthosine Monophosphate', 'GTP': 'Purine Metabolism state 8', 'dATP': 'Deoxy ATP', 'dGTP': 'Purine Metabolism state 10', 'RNA': 'RNA', 'DNA': 'DNA', 'HX': 'Purine Metabolism state 13', 'Xa': 'Purine Metabolism state 14', 'Gua': 'Purine Metabolism state 15', 'UA': 'Purine Metabolism state 16'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_phosphoribosylpyrophosphate': ('PRPP', 5.01742, 'native SBML value', 'Initial condition for phosphoribosylpyrophosphate. Maps to bundled SBML symbol `PRPP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_inosine_monophosphate': ('IMP', 98.2634, 'native SBML value', 'Initial condition for inosine monophosphate. Maps to bundled SBML symbol `IMP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_adenylosuccinate': ('SAMP', 0.198189, 'native SBML value', 'Initial condition for adenylosuccinate. Maps to bundled SBML symbol `SAMP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 2475.35, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_s_adenosyl_l_methionine': ('SAM', 3.99187, 'native SBML value', 'Initial condition for s adenosyl l methionine. Maps to bundled SBML symbol `SAM`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'phosphoribosylpyrophosphate': ('PRPP', 'native SBML value', 'Phosphoribosylpyrophosphate. Maps to SBML symbol `PRPP`.'), 'inosine_monophosphate': ('IMP', 'native SBML value', 'Inosine Monophosphate. Maps to SBML symbol `IMP`.'), 'adenylosuccinate': ('SAMP', 'native SBML value', 'Adenylosuccinate. Maps to SBML symbol `SAMP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 's_adenosyl_l_methionine': ('SAM', 'native SBML value', 'S Adenosyl L Methionine. Maps to SBML symbol `SAM`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000015.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
