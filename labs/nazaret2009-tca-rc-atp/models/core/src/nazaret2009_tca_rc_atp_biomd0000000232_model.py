# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Nazaret2009_TCA_RC_ATP."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nazaret2009TcaRcAtpBiomd0000000232Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Nazaret2009_TCA_RC_ATP."""

    _SBML_ID = 'BIOMD0000000232'
    _TITLE = 'Nazaret2009_TCA_RC_ATP'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ATP': 'atp', 'NAD': 'nad', 'AcCoA': 'mitochondrial_energy_state_3', 'KG': 'alpha_ketoglutarate', 'Cit': 'mitochondrial_energy_state_5', 'OAA': 'oxaloacetate', 'Pyr': 'pyruvate'}
    _OBSERVABLES = ['ATP', 'NAD', 'AcCoA', 'KG', 'Cit', 'OAA', 'Pyr']
    _SPECIES_LABELS = {'ATP': 'ATP', 'NAD': 'NAD', 'AcCoA': 'Mitochondrial Energy state 3', 'KG': 'Alpha Ketoglutarate', 'Cit': 'Mitochondrial Energy state 5', 'OAA': 'Oxaloacetate', 'Pyr': 'Pyruvate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_atp': ('ATP', 3.536, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad': ('NAD', 0.856, 'native SBML value', 'Initial condition for nad. Maps to bundled SBML symbol `NAD`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_mitochondrial_energy_state_3': ('AcCoA', 0.063, 'native SBML value', 'Initial condition for mitochondrial energy state 3. Maps to bundled SBML symbol `AcCoA`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_alpha_ketoglutarate': ('KG', 0.225, 'native SBML value', 'Initial condition for alpha ketoglutarate. Maps to bundled SBML symbol `KG`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_mitochondrial_energy_state_5': ('Cit', 0.44, 'native SBML value', 'Initial condition for mitochondrial energy state 5. Maps to bundled SBML symbol `Cit`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.'), 'mitochondrial_energy_state_3': ('AcCoA', 'native SBML value', 'Mitochondrial Energy state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `AcCoA`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'alpha_ketoglutarate': ('KG', 'native SBML value', 'Alpha Ketoglutarate. Maps to SBML symbol `KG`.'), 'mitochondrial_energy_state_5': ('Cit', 'native SBML value', 'Mitochondrial Energy state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `Cit`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000232.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
