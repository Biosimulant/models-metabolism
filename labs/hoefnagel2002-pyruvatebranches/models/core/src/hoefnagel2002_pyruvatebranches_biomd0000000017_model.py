# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Hoefnagel2002_PyruvateBranches."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hoefnagel2002PyruvatebranchesBiomd0000000017Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Hoefnagel2002_PyruvateBranches."""

    _SBML_ID = 'BIOMD0000000017'
    _TITLE = 'Hoefnagel2002_PyruvateBranches'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'ADP': 'adp', 'NAD': 'nad', 'ATP': 'atp', 'NADH': 'nadh', 'pyruvate': 'metabolic_pathway_state_5', 'CoA': 'coa', 'AcCoA': 'metabolic_pathway_state_7', 'AcP': 'metabolic_pathway_state_8', 'AcO': 'metabolic_pathway_state_9', 'AcLac': 'metabolic_pathway_state_10', 'AcetoinIn': 'metabolic_pathway_state_11'}
    _OBSERVABLES = ['ADP', 'NAD', 'ATP', 'NADH', 'pyruvate', 'CoA', 'AcCoA', 'AcP', 'AcO', 'AcLac', 'AcetoinIn']
    _SPECIES_LABELS = {'ADP': 'ADP', 'NAD': 'NAD', 'ATP': 'ATP', 'NADH': 'NADH', 'pyruvate': 'Metabolic Pathway state 5', 'CoA': 'CoA', 'AcCoA': 'Metabolic Pathway state 7', 'AcP': 'Metabolic Pathway state 8', 'AcO': 'Metabolic Pathway state 9', 'AcLac': 'Metabolic Pathway state 10', 'AcetoinIn': 'Metabolic Pathway state 11'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('ADP', 4.9, 'native SBML value', 'Initial condition for adp. Maps to bundled SBML symbol `ADP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nad': ('NAD', 6.33, 'native SBML value', 'Initial condition for nad. Maps to bundled SBML symbol `NAD`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_atp': ('ATP', 0.1, 'native SBML value', 'Initial condition for atp. Maps to bundled SBML symbol `ATP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_nadh': ('NADH', 3.67, 'native SBML value', 'Initial condition for nadh. Maps to bundled SBML symbol `NADH`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_metabolic_pathway_state_5': ('pyruvate', 1.0, 'native SBML value', 'Initial condition for metabolic pathway state 5. Maps to bundled SBML symbol `pyruvate`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'nad': ('NAD', 'native SBML value', 'NAD. Maps to SBML symbol `NAD`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'nadh': ('NADH', 'native SBML value', 'NADH. Maps to SBML symbol `NADH`.'), 'metabolic_pathway_state_5': ('pyruvate', 'native SBML value', 'Metabolic Pathway state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `pyruvate`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000017.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
