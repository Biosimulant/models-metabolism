# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Olsen2003_neutrophil_oscillatory_metabolism."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Olsen2003NeutrophilOscillatoryMetabolismBiomd0000000143Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Olsen2003_neutrophil_oscillatory_metabolism."""

    _SBML_ID = 'BIOMD0000000143'
    _TITLE = 'Olsen2003_neutrophil_oscillatory_metabolism'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'H2O2_p': 'h2o2', 'per3_p': 'ferric_peroxidase', 'coI_p': 'compound_i', 'MLTH_p': 'melatonin', 'coII_p': 'compound_ii', 'MLT_p': 'melatonin_free_radical', 'O2minus_p': 'superoxide', 'H_p': 'metabolic_pathway_state_8', 'O2_p': 'metabolic_pathway_state_9', 'NADPH_c': 'nadph', 'O2_c': 'cytosolic_o2', 'NADPplus_c': 'nadp', 'H2O2_c': 'h2o2_2', 'NADP_c': 'nadp_2', 'O2minus_c': 'superoxide_2', 'H_c': 'metabolic_pathway_state_16', 'MLT_c': 'melatonin_free_radical_2', 'MLTH_c': 'melatonin_2', 'coIII_p': 'compound_iii', 'NADP2_c': 'nadp2'}
    _OBSERVABLES = ['H2O2_p', 'per3_p', 'coI_p', 'MLTH_p', 'coII_p', 'MLT_p', 'O2minus_p', 'H_p', 'O2_p', 'NADPH_c', 'O2_c', 'NADPplus_c', 'H2O2_c', 'NADP_c', 'O2minus_c', 'H_c', 'MLT_c', 'MLTH_c', 'coIII_p', 'NADP2_c']
    _SPECIES_LABELS = {'H2O2_p': 'H2o2', 'per3_p': 'Ferric Peroxidase', 'coI_p': 'Compound I', 'MLTH_p': 'Melatonin', 'coII_p': 'Compound Ii', 'MLT_p': 'Melatonin Free Radical', 'O2minus_p': 'Superoxide', 'H_p': 'Metabolic Pathway state 8', 'O2_p': 'Metabolic Pathway state 9', 'NADPH_c': 'NADPH', 'O2_c': 'Cytosolic O2', 'NADPplus_c': 'NADP', 'H2O2_c': 'H2o2 2', 'NADP_c': 'NADP 2', 'O2minus_c': 'Superoxide 2', 'H_c': 'Metabolic Pathway state 16', 'MLT_c': 'Melatonin Free Radical 2', 'MLTH_c': 'Melatonin 2', 'coIII_p': 'Compound Iii', 'NADP2_c': 'Nadp2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_h2o2': ('H2O2_p', 0.0, 'native SBML value', 'Initial condition for h2o2. Maps to bundled SBML symbol `H2O2_p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_ferric_peroxidase': ('per3_p', 300.0, 'native SBML value', 'Initial condition for ferric peroxidase. Maps to bundled SBML symbol `per3_p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_compound_i': ('coI_p', 0.0, 'native SBML value', 'Initial condition for compound i. Maps to bundled SBML symbol `coI_p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_melatonin': ('MLTH_p', 300.0, 'native SBML value', 'Initial condition for melatonin. Maps to bundled SBML symbol `MLTH_p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_compound_ii': ('coII_p', 0.0, 'native SBML value', 'Initial condition for compound ii. Maps to bundled SBML symbol `coII_p`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'h2o2': ('H2O2_p', 'native SBML value', 'H2o2. Maps to SBML symbol `H2O2_p`.'), 'ferric_peroxidase': ('per3_p', 'native SBML value', 'Ferric Peroxidase. Maps to SBML symbol `per3_p`.'), 'compound_i': ('coI_p', 'native SBML value', 'Compound I. Maps to SBML symbol `coI_p`.'), 'melatonin': ('MLTH_p', 'native SBML value', 'Melatonin. Maps to SBML symbol `MLTH_p`.'), 'compound_ii': ('coII_p', 'native SBML value', 'Compound Ii. Maps to SBML symbol `coII_p`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000143.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
