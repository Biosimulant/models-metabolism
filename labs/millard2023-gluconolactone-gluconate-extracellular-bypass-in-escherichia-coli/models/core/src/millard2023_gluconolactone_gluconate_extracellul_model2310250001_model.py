# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed wrapper for Millard2023 - Gluconolactone-Gluconate extracellular bypass in Escherichia coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Millard2023GluconolactoneGluconateExtracellulModel2310250001Model(TelluriumSBMLBioModule):
    """Tellurium-backed wrapper for Millard2023 - Gluconolactone-Gluconate extracellular bypass in Escherichia coli."""

    _SBML_ID = 'MODEL2310250001'
    _TITLE = 'Millard2023 - Gluconolactone-Gluconate extracellular bypass in Escherichia coli'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _SPECIES_LABELS_OUTPUT_NAME = 'observable_labels'
    _SUMMARY_OUTPUT_NAME = 'run_summary'
    _STATE_OUTPUT_NAME = 'observable_values'
    _STATE_OUTPUT_ALIASES = {'G6P_0': 'microbial_metabolism_state_1', 'GAP_0': 'microbial_metabolism_state_2', 'PYR_0': 'microbial_metabolism_state_3', '_6PGL_0': 'observable_6pgl_0', '_6PG_0': 'observable_6pg_0', 'GAP_1': 'microbial_metabolism_state_6', 'PYR_1': 'microbial_metabolism_state_7', '_6PG_1': 'observable_6pg_1', 'X': 'microbial_metabolism_state_9', '_6PGL_1': 'observable_6pgl_1', 'G6P_1': 'microbial_metabolism_state_11'}
    _OBSERVABLES = ['G6P_0', 'GAP_0', 'PYR_0', '_6PGL_0', '_6PG_0', 'GAP_1', 'PYR_1', '_6PG_1', 'X', '_6PGL_1', 'G6P_1']
    _SPECIES_LABELS = {'G6P_0': 'Microbial Metabolism state 1', 'GAP_0': 'Microbial Metabolism state 2', 'PYR_0': 'Microbial Metabolism state 3', '_6PGL_0': '6pgl 0', '_6PG_0': '6pg 0', 'GAP_1': 'Microbial Metabolism state 6', 'PYR_1': 'Microbial Metabolism state 7', '_6PG_1': '6pg 1', 'X': 'Microbial Metabolism state 9', '_6PGL_1': '6pgl 1', 'G6P_1': 'Microbial Metabolism state 11'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_microbial_metabolism_state_1': ('G6P_0', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 1. Maps to bundled SBML symbol `G6P_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_2': ('GAP_0', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 2. Maps to bundled SBML symbol `GAP_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_microbial_metabolism_state_3': ('PYR_0', 1.0, 'native SBML value', 'Initial condition for microbial metabolism state 3. Maps to bundled SBML symbol `PYR_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_observable_6pgl_0': ('_6PGL_0', 1.0, 'native SBML value', 'Initial condition for observable 6pgl 0. Maps to bundled SBML symbol `_6PGL_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.'), 'initial_observable_6pg_0': ('_6PG_0', 1.0, 'native SBML value', 'Initial condition for observable 6pg 0. Maps to bundled SBML symbol `_6PG_0`. Applied before the Tellurium simulation starts; this does not change kinetic parameters or equations.')}
    _HEADLINE_OUTPUTS = {'microbial_metabolism_state_1': ('G6P_0', 'native SBML value', 'Microbial Metabolism state 1; conservative display label for an abstract SBML state variable. Maps to SBML symbol `G6P_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'microbial_metabolism_state_2': ('GAP_0', 'native SBML value', 'Microbial Metabolism state 2; conservative display label for an abstract SBML state variable. Maps to SBML symbol `GAP_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'microbial_metabolism_state_3': ('PYR_0', 'native SBML value', 'Microbial Metabolism state 3; conservative display label for an abstract SBML state variable. Maps to SBML symbol `PYR_0`. Exact metabolite identity is not encoded in the bundled SBML metadata.'), 'observable_6pgl_0': ('_6PGL_0', 'native SBML value', '6pgl 0. Maps to SBML symbol `_6PGL_0`.'), 'observable_6pg_0': ('_6PG_0', 'native SBML value', '6pg 0. Maps to SBML symbol `_6PG_0`.')}

    def __init__(self, model_path: str = 'data/MODEL2310250001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
