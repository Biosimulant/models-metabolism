# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Saa2016 - Mammalian methionine cycle - approximate bayesian computation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Saa2016MammalianMethionineCycleApproximateBModel1603150000Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Saa2016 - Mammalian methionine cycle - approximate bayesian computation."""

    _SBML_ID = 'MODEL1603150000'
    _TITLE = 'Saa2016 - Mammalian methionine cycle - approximate bayesian computation'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'MET': 'methionine_cycle_state_1', 'ADOMET': 'methionine_cycle_state_2', 'ADOHCY': 'methionine_cycle_state_3', 'MTHF': 'methionine_cycle_state_4', 'HCY': 'methionine_cycle_state_5'}
    _OBSERVABLES = ['MET', 'ADOMET', 'ADOHCY', 'MTHF', 'HCY']
    _SPECIES_LABELS = {'MET': 'Methionine Cycle state 1', 'ADOMET': 'Methionine Cycle state 2', 'ADOHCY': 'Methionine Cycle state 3', 'MTHF': 'Methionine Cycle state 4', 'HCY': 'Methionine Cycle state 5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_methionine_cycle_state_1': ('MET', 50.0, 'native SBML value', 'Initial condition for methionine cycle state 1. Maps to bundled SBML symbol `MET`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_methionine_cycle_state_2': ('ADOMET', 60.0, 'native SBML value', 'Initial condition for methionine cycle state 2. Maps to bundled SBML symbol `ADOMET`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_methionine_cycle_state_3': ('ADOHCY', 35.0, 'native SBML value', 'Initial condition for methionine cycle state 3. Maps to bundled SBML symbol `ADOHCY`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_methionine_cycle_state_4': ('MTHF', 1.7, 'native SBML value', 'Initial condition for methionine cycle state 4. Maps to bundled SBML symbol `MTHF`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_methionine_cycle_state_5': ('HCY', 3.5, 'native SBML value', 'Initial condition for methionine cycle state 5. Maps to bundled SBML symbol `HCY`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'methionine_cycle_state_1': ('MET', 'native SBML value', 'Methionine Cycle state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `MET`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'methionine_cycle_state_2': ('ADOMET', 'native SBML value', 'Methionine Cycle state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `ADOMET`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'methionine_cycle_state_3': ('ADOHCY', 'native SBML value', 'Methionine Cycle state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `ADOHCY`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'methionine_cycle_state_4': ('MTHF', 'native SBML value', 'Methionine Cycle state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `MTHF`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'methionine_cycle_state_5': ('HCY', 'native SBML value', 'Methionine Cycle state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `HCY`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/MODEL1603150000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
