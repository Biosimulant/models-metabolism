# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Jallet2024 - Isotopic model of ethanolamine metabolism in E. coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jallet2024IsotopicModelOfEthanolamineMetaboModel2403010002Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Jallet2024 - Isotopic model of ethanolamine metabolism in E. coli."""

    _SBML_ID = 'MODEL2403010002'
    _TITLE = 'Jallet2024 - Isotopic model of ethanolamine metabolism in E. coli'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'EA_c': 'microbial_metabolism_state_1', 'EA_eut': 'microbial_metabolism_state_2', 'AAL_eut': 'microbial_metabolism_state_3', 'NH4_eut': 'microbial_metabolism_state_4', 'EtOH_eut': 'microbial_metabolism_state_5', 'AcCoA_eut': 'microbial_metabolism_state_6', 'NADH_eut': 'microbial_metabolism_state_7', 'NAD_eut': 'microbial_metabolism_state_8', 'AcP_eut': 'microbial_metabolism_state_9', 'NH4_c': 'microbial_metabolism_state_10', 'EtOH_c': 'microbial_metabolism_state_11', 'AcP_c_1': 'microbial_metabolism_state_12', 'GLY_c': 'microbial_metabolism_state_13', 'AcP_c_0': 'microbial_metabolism_state_14', 'BIOMASS': 'microbial_metabolism_state_15', 'Ace_c_0': 'microbial_metabolism_state_16', 'Ace_c_1': 'microbial_metabolism_state_17'}
    _OBSERVABLES = ['EA_c', 'EA_eut', 'AAL_eut', 'NH4_eut', 'EtOH_eut', 'AcCoA_eut', 'NADH_eut', 'NAD_eut', 'AcP_eut', 'NH4_c', 'EtOH_c', 'AcP_c_1', 'GLY_c', 'AcP_c_0', 'BIOMASS', 'Ace_c_0', 'Ace_c_1']
    _SPECIES_LABELS = {'EA_c': 'Microbial Metabolism state 1', 'EA_eut': 'Microbial Metabolism state 2', 'AAL_eut': 'Microbial Metabolism state 3', 'NH4_eut': 'Microbial Metabolism state 4', 'EtOH_eut': 'Microbial Metabolism state 5', 'AcCoA_eut': 'Microbial Metabolism state 6', 'NADH_eut': 'Microbial Metabolism state 7', 'NAD_eut': 'Microbial Metabolism state 8', 'AcP_eut': 'Microbial Metabolism state 9', 'NH4_c': 'Microbial Metabolism state 10', 'EtOH_c': 'Microbial Metabolism state 11', 'AcP_c_1': 'Microbial Metabolism state 12', 'GLY_c': 'Microbial Metabolism state 13', 'AcP_c_0': 'Microbial Metabolism state 14', 'BIOMASS': 'Microbial Metabolism state 15', 'Ace_c_0': 'Microbial Metabolism state 16', 'Ace_c_1': 'Microbial Metabolism state 17'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_microbial_metabolism_state_1': ('EA_c', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 1. Maps to bundled SBML symbol `EA_c`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_2': ('EA_eut', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 2. Maps to bundled SBML symbol `EA_eut`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_3': ('AAL_eut', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 3. Maps to bundled SBML symbol `AAL_eut`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_4': ('NH4_eut', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 4. Maps to bundled SBML symbol `NH4_eut`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_5': ('EtOH_eut', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 5. Maps to bundled SBML symbol `EtOH_eut`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'microbial_metabolism_state_1': ('EA_c', 'native SBML value', 'Microbial Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `EA_c`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'microbial_metabolism_state_2': ('EA_eut', 'native SBML value', 'Microbial Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `EA_eut`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'microbial_metabolism_state_3': ('AAL_eut', 'native SBML value', 'Microbial Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `AAL_eut`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'microbial_metabolism_state_4': ('NH4_eut', 'native SBML value', 'Microbial Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `NH4_eut`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'microbial_metabolism_state_5': ('EtOH_eut', 'native SBML value', 'Microbial Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `EtOH_eut`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL2403010002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
