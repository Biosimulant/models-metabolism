# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Cloutier2009_EnergyMetabolism_ModelF."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cloutier2009EnergymetabolismModelfModel1006230096Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Cloutier2009_EnergyMetabolism_ModelF."""

    _SBML_ID = 'MODEL1006230096'
    _TITLE = 'Cloutier2009_EnergyMetabolism_ModelF'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'F6P': 'fructose_6_phosphate', 'F26P': 'fructose_2_6_bisphosphate', 'GAP': 'glyceraldehyde_3_phosphate', 'PYR': 'pyruvate', 'LAC': 'lactate', 'ATP': 'atp', 'PCr': 'metabolic_pathway_state_7', 'V_hk': 'metabolic_pathway_state_8', 'V_op': 'metabolic_pathway_state_9', 'V_ldh': 'metabolic_pathway_state_10', 'V_ck': 'metabolic_pathway_state_11', 'Cr': 'metabolic_pathway_state_12', 'ADP': 'adp', 'u': 'metabolic_pathway_state_14', 'dAMP_dATP': 'deoxy_deoxy_amp_atp', 'AMP': 'amp', 'ATP_inh': 'metabolic_pathway_state_17', 'V_pfk': 'metabolic_pathway_state_18', 'V_pfk2': 'metabolic_pathway_state_19', 'V_pk': 'metabolic_pathway_state_20', 'AMP_act': 'metabolic_pathway_state_21', 'v_stim': 'metabolic_pathway_state_22', 'V_ATPase': 'metabolic_pathway_state_23', 'V_lac': 'metabolic_pathway_state_24', 'unitpulseSB': 'metabolic_pathway_state_25', 'AMP_pfk2': 'metabolic_pathway_state_26'}
    _OBSERVABLES = ['F6P', 'F26P', 'GAP', 'PYR', 'LAC', 'ATP', 'PCr', 'V_hk', 'V_op', 'V_ldh', 'V_ck', 'Cr', 'ADP', 'u', 'dAMP_dATP', 'AMP', 'ATP_inh', 'V_pfk', 'V_pfk2', 'V_pk', 'AMP_act', 'v_stim', 'V_ATPase', 'V_lac', 'unitpulseSB', 'AMP_pfk2']
    _SPECIES_LABELS = {'F6P': 'Fructose 6 Phosphate', 'F26P': 'Fructose 2 6 Bisphosphate', 'GAP': 'Glyceraldehyde 3 Phosphate', 'PYR': 'Pyruvate', 'LAC': 'Lactate', 'ATP': 'ATP', 'PCr': 'Metabolic Pathway state 7', 'V_hk': 'Metabolic Pathway state 8', 'V_op': 'Metabolic Pathway state 9', 'V_ldh': 'Metabolic Pathway state 10', 'V_ck': 'Metabolic Pathway state 11', 'Cr': 'Metabolic Pathway state 12', 'ADP': 'ADP', 'u': 'Metabolic Pathway state 14', 'dAMP_dATP': 'Deoxy Deoxy AMP ATP', 'AMP': 'AMP', 'ATP_inh': 'Metabolic Pathway state 17', 'V_pfk': 'Metabolic Pathway state 18', 'V_pfk2': 'Metabolic Pathway state 19', 'V_pk': 'Metabolic Pathway state 20', 'AMP_act': 'Metabolic Pathway state 21', 'v_stim': 'Metabolic Pathway state 22', 'V_ATPase': 'Metabolic Pathway state 23', 'V_lac': 'Metabolic Pathway state 24', 'unitpulseSB': 'Metabolic Pathway state 25', 'AMP_pfk2': 'Metabolic Pathway state 26'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fructose_6_phosphate': ('F6P', 0.2, 'native SBML value', 'Initial condition for fructose 6 phosphate. Maps to bundled SBML symbol `F6P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_fructose_2_6_bisphosphate': ('F26P', 0.001, 'native SBML value', 'Initial condition for fructose 2 6 bisphosphate. Maps to bundled SBML symbol `F26P`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_glyceraldehyde_3_phosphate': ('GAP', 0.0405, 'native SBML value', 'Initial condition for glyceraldehyde 3 phosphate. Maps to bundled SBML symbol `GAP`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_pyruvate': ('PYR', 0.1, 'native SBML value', 'Initial condition for pyruvate. Maps to bundled SBML symbol `PYR`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_lactate': ('LAC', 0.5, 'native SBML value', 'Initial condition for lactate. Maps to bundled SBML symbol `LAC`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'fructose_6_phosphate': ('F6P', 'native SBML value', 'Fructose 6 Phosphate. Maps to SBML symbol `F6P`.'), 'fructose_2_6_bisphosphate': ('F26P', 'native SBML value', 'Fructose 2 6 Bisphosphate. Maps to SBML symbol `F26P`.'), 'glyceraldehyde_3_phosphate': ('GAP', 'native SBML value', 'Glyceraldehyde 3 Phosphate. Maps to SBML symbol `GAP`.'), 'pyruvate': ('PYR', 'native SBML value', 'Pyruvate. Maps to SBML symbol `PYR`.'), 'lactate': ('LAC', 'native SBML value', 'Lactate. Maps to SBML symbol `LAC`.')}

    def __init__(self, model_path: str = 'data/MODEL1006230096.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
