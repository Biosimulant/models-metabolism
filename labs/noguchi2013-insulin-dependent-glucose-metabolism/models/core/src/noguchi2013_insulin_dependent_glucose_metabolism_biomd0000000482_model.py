# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Noguchi2013 - Insulin dependent glucose metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Noguchi2013InsulinDependentGlucoseMetabolismBiomd0000000482Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Noguchi2013 - Insulin dependent glucose metabolism."""

    _SBML_ID = 'BIOMD0000000482'
    _TITLE = 'Noguchi2013 - Insulin dependent glucose metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'GP': 'glycolysis_state_1', 'pGP': 'glycolysis_state_2', 'mRNA': 'mitochondrial_rna', 'PEPCK': 'glycolysis_state_4', 'IRS': 'glycolysis_state_5', 'p1IRS': 'glycolysis_state_6', 'p2IRS': 'glycolysis_state_7', 'p1p2IRS': 'glycolysis_state_8', 'Akt': 'glycolysis_state_9', 'pAkt': 'glycolysis_state_10', 'mTOR': 'glycolysis_state_11', 'pmTOR': 'glycolysis_state_12', 'Foxo': 'glycolysis_state_13', 'pFoxo': 'glycolysis_state_14', 'PYRout': 'extracellular_pyruvate', 'GLCex': 'glycolysis_state_16', 'F16P': 'fructose_1_6_bisphosphate', 'PYRin': 'intracellular_pyruvate', 'LAC': 'lactate', 'OAA': 'glycolysis_state_20', 'GLY': 'glycolysis_state_21', 'G1P': 'glycolysis_state_22', 'G6P': 'glucose_6_phosphate'}
    _OBSERVABLES = ['GP', 'pGP', 'mRNA', 'PEPCK', 'IRS', 'p1IRS', 'p2IRS', 'p1p2IRS', 'Akt', 'pAkt', 'mTOR', 'pmTOR', 'Foxo', 'pFoxo', 'PYRout', 'GLCex', 'F16P', 'PYRin', 'LAC', 'OAA', 'GLY', 'G1P', 'G6P']
    _SPECIES_LABELS = {'GP': 'Glycolysis state 1', 'pGP': 'Glycolysis state 2', 'mRNA': 'Mitochondrial RNA', 'PEPCK': 'Glycolysis state 4', 'IRS': 'Glycolysis state 5', 'p1IRS': 'Glycolysis state 6', 'p2IRS': 'Glycolysis state 7', 'p1p2IRS': 'Glycolysis state 8', 'Akt': 'Glycolysis state 9', 'pAkt': 'Glycolysis state 10', 'mTOR': 'Glycolysis state 11', 'pmTOR': 'Glycolysis state 12', 'Foxo': 'Glycolysis state 13', 'pFoxo': 'Glycolysis state 14', 'PYRout': 'Extracellular Pyruvate', 'GLCex': 'Glycolysis state 16', 'F16P': 'Fructose 1 6 Bisphosphate', 'PYRin': 'Intracellular Pyruvate', 'LAC': 'Lactate', 'OAA': 'Glycolysis state 20', 'GLY': 'Glycolysis state 21', 'G1P': 'Glycolysis state 22', 'G6P': 'Glucose 6 Phosphate'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glycolysis_state_1': ('GP', 0.4726, 'native SBML value', 'Initial condition for glycolysis state 1. Maps to bundled SBML symbol `GP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_2': ('pGP', 0.1723, 'native SBML value', 'Initial condition for glycolysis state 2. Maps to bundled SBML symbol `pGP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_mitochondrial_rna': ('mRNA', 2.905, 'native SBML value', 'Initial condition for mitochondrial rna. Maps to bundled SBML symbol `mRNA`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_4': ('PEPCK', 0.7686, 'native SBML value', 'Initial condition for glycolysis state 4. Maps to bundled SBML symbol `PEPCK`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glycolysis_state_5': ('IRS', 888.77, 'native SBML value', 'Initial condition for glycolysis state 5. Maps to bundled SBML symbol `IRS`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'glycolysis_state_1': ('GP', 'native SBML value', 'Glycolysis state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `GP`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_2': ('pGP', 'native SBML value', 'Glycolysis state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `pGP`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'mitochondrial_rna': ('mRNA', 'native SBML value', 'Mitochondrial RNA. Maps to SBML symbol `mRNA`.'), 'glycolysis_state_4': ('PEPCK', 'native SBML value', 'Glycolysis state 4; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PEPCK`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'glycolysis_state_5': ('IRS', 'native SBML value', 'Glycolysis state 5; conservative display label for an abstract SBML state variable. Maps to SBML symbol `IRS`. Exact metabolite identity is not encoded in the bundled SBML metadata.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000482.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
