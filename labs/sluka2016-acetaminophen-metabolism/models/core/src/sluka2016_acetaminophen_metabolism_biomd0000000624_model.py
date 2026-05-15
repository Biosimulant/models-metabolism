# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Sluka2016 - Acetaminophen metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sluka2016AcetaminophenMetabolismBiomd0000000624Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Sluka2016 - Acetaminophen metabolism."""

    _SBML_ID = 'BIOMD0000000624'
    _TITLE = 'Sluka2016 - Acetaminophen metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'APAP': 'drug_metabolism_state_1', 'NAPQI': 'drug_metabolism_state_2', 'GSH': 'glutathione', 'NAPQIGSH': 'drug_metabolism_state_4', 'APAPconj_Glu': 'drug_metabolism_state_5', 'APAPconj_Sul': 'drug_metabolism_state_6'}
    _OBSERVABLES = ['APAP', 'NAPQI', 'GSH', 'NAPQIGSH', 'APAPconj_Glu', 'APAPconj_Sul']
    _SPECIES_LABELS = {'APAP': 'Drug Metabolism state 1', 'NAPQI': 'Drug Metabolism state 2', 'GSH': 'Glutathione', 'NAPQIGSH': 'Drug Metabolism state 4', 'APAPconj_Glu': 'Drug Metabolism state 5', 'APAPconj_Sul': 'Drug Metabolism state 6'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_drug_metabolism_state_1': ('APAP', 0.1, 'native SBML value', 'Initial condition for drug metabolism state 1. Maps to bundled SBML symbol `APAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_2': ('NAPQI', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 2. Maps to bundled SBML symbol `NAPQI`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glutathione': ('GSH', 10.0, 'native SBML value', 'Initial condition for glutathione. Maps to bundled SBML symbol `GSH`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_4': ('NAPQIGSH', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 4. Maps to bundled SBML symbol `NAPQIGSH`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_5': ('APAPconj_Glu', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 5. Maps to bundled SBML symbol `APAPconj_Glu`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'drug_metabolism_state_1': ('APAP', 'native SBML value', 'Drug Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `APAP`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_2': ('NAPQI', 'native SBML value', 'Drug Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `NAPQI`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glutathione': ('GSH', 'native SBML value', 'Glutathione. Maps to SBML symbol `GSH`.'), 'drug_metabolism_state_4': ('NAPQIGSH', 'native SBML value', 'Drug Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `NAPQIGSH`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_5': ('APAPconj_Glu', 'native SBML value', 'Drug Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `APAPconj_Glu`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000624.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
