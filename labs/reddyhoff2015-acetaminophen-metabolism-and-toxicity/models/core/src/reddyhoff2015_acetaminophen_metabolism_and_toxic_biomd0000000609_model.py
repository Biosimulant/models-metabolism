# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Reddyhoff2015 - Acetaminophen metabolism and toxicity."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Reddyhoff2015AcetaminophenMetabolismAndToxicBiomd0000000609Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Reddyhoff2015 - Acetaminophen metabolism and toxicity."""

    _SBML_ID = 'BIOMD0000000609'
    _TITLE = 'Reddyhoff2015 - Acetaminophen metabolism and toxicity'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'Sulphate__PAPS': 'sulphate_paps', 'GSH': 'glutathione', 'NAPQI': 'drug_metabolism_state_3', 'Paracetamol_APAP': 'drug_metabolism_state_4', 'Protein_adducts': 'drug_metabolism_state_5'}
    _OBSERVABLES = ['Sulphate__PAPS', 'GSH', 'NAPQI', 'Paracetamol_APAP', 'Protein_adducts']
    _SPECIES_LABELS = {'Sulphate__PAPS': 'Sulphate Paps', 'GSH': 'Glutathione', 'NAPQI': 'Drug Metabolism state 3', 'Paracetamol_APAP': 'Drug Metabolism state 4', 'Protein_adducts': 'Drug Metabolism state 5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_sulphate_paps': ('Sulphate__PAPS', 1.325e-14, 'native SBML value', 'Initial condition for sulphate paps. Maps to bundled SBML symbol `Sulphate__PAPS`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glutathione': ('GSH', 6.87e-15, 'native SBML value', 'Initial condition for glutathione. Maps to bundled SBML symbol `GSH`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_3': ('NAPQI', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 3. Maps to bundled SBML symbol `NAPQI`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_4': ('Paracetamol_APAP', 1.32e-13, 'native SBML value', 'Initial condition for drug metabolism state 4. Maps to bundled SBML symbol `Paracetamol_APAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_drug_metabolism_state_5': ('Protein_adducts', 0.0, 'native SBML value', 'Initial condition for drug metabolism state 5. Maps to bundled SBML symbol `Protein_adducts`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'sulphate_paps': ('Sulphate__PAPS', 'native SBML value', 'Sulphate Paps. Maps to SBML symbol `Sulphate__PAPS`.'), 'glutathione': ('GSH', 'native SBML value', 'Glutathione. Maps to SBML symbol `GSH`.'), 'drug_metabolism_state_3': ('NAPQI', 'native SBML value', 'Drug Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `NAPQI`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_4': ('Paracetamol_APAP', 'native SBML value', 'Drug Metabolism state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Paracetamol_APAP`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'drug_metabolism_state_5': ('Protein_adducts', 'native SBML value', 'Drug Metabolism state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Protein_adducts`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000609.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
