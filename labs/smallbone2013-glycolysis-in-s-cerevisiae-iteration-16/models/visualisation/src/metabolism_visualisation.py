# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Dedicated visualisation model for cleaned metabolism SBML ODE labs."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec, unwrap_payload


SUMMARY_SCHEMA = {
    "duration_simulated": "float",
    "observable_count": "int",
    "largest_change_observable": "str",
    "largest_change_magnitude": "float",
    "peak_observable": "str",
    "peak_value": "float",
}


def _as_mapping(signal: BioSignal | None) -> Mapping[str, Any]:
    if signal is None:
        return {}
    value = unwrap_payload(signal)
    return value if isinstance(value, Mapping) else {}


def _finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if number == number and number not in (float("inf"), float("-inf")) else None


class MetabolismVisualisationModel(BioModule):
    """Render direct scientific answers and non-empty charts from SBML state."""

    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        sources: list[dict[str, Any]],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = lab_title
        self.question = question
        self.answer_focus = answer_focus
        self.sources = list(sources)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: dict[str, list[dict[str, float]]] = {}
        self._times: dict[str, list[float]] = {}
        self._t = 0.0

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        for source in self.sources:
            alias = str(source["alias"])
            observables = [str(item["id"]) for item in source.get("observables", [])]
            specs[f"{alias}_observable_values"] = SignalSpec.record(
                schema={name: "float" for name in observables} or {"payload": "json"},
                description="Latest user-facing observable values from the core metabolism model.",
            )
            specs[f"{alias}_run_summary"] = SignalSpec.record(
                schema=dict(SUMMARY_SCHEMA),
                description="Run summary from the core metabolism model.",
            )
            specs[f"{alias}_observable_labels"] = SignalSpec.record(
                schema={name: "str" for name in observables} or {"payload": "json"},
                description="Display labels for user-facing observables.",
            )
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._history = {str(source["alias"]): [] for source in self.sources}
        self._times = {str(source["alias"]): [] for source in self.sources}
        self._t = 0.0

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        self._t = float(end)
        for source in self.sources:
            alias = str(source["alias"])
            state = _as_mapping(self._inputs.get(f"{alias}_observable_values"))
            row: dict[str, float] = {}
            for item in source.get("observables", []):
                oid = str(item["id"])
                value = _finite(state.get(oid))
                if value is not None:
                    row[oid] = value
            if row:
                self._history.setdefault(alias, []).append(row)
                self._times.setdefault(alias, []).append(float(end))

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        visuals: list[dict[str, Any]] = []
        for source in self.sources:
            alias = str(source["alias"])
            labels = self._label_map(source)
            history = self._history.get(alias, [])
            summary = _as_mapping(self._inputs.get(f"{alias}_run_summary"))
            visuals.append(self._answer_table(source, labels, history, summary))
            ts = self._timeseries(source, labels, history)
            if ts is not None:
                visuals.append(ts)
            bar = self._bar(source, labels, history)
            if bar is not None:
                visuals.append(bar)
            scatter = self._scatter(source, labels, history)
            if scatter is not None:
                visuals.append(scatter)
        return visuals or None

    def _label_map(self, source: Mapping[str, Any]) -> dict[str, str]:
        alias = str(source["alias"])
        labels = dict(_as_mapping(self._inputs.get(f"{alias}_observable_labels")))
        for item in source.get("observables", []):
            oid = str(item["id"])
            labels.setdefault(oid, str(item.get("label") or oid))
        return {str(k): str(v) for k, v in labels.items()}

    def _answer_table(
        self,
        source: Mapping[str, Any],
        labels: Mapping[str, str],
        history: list[dict[str, float]],
        summary: Mapping[str, Any],
    ) -> dict[str, Any]:
        largest = str(summary.get("largest_change_observable") or "")
        peak = str(summary.get("peak_observable") or "")
        largest_label = labels.get(largest, largest) if largest else "No changing observable"
        peak_label = labels.get(peak, peak) if peak else "No peak observable"
        change = _finite(summary.get("largest_change_magnitude")) or 0.0
        peak_value = _finite(summary.get("peak_value")) or 0.0
        caveat = str(source.get("label_caveat") or "Values are native SBML quantities. The bundled SBML is executed directly and equations were not rewritten.")
        if history and change > 0.0:
            observed = f"{largest_label} changed the most during the simulated window."
            evidence = f"Largest excursion {change:.6g}; peak readout {peak_label} = {peak_value:.6g}."
        elif history:
            observed = "The selected SBML observables are near steady over this short run."
            evidence = f"Final state contains {len(history[-1])} finite observables; no material excursion was detected."
        else:
            observed = "No finite SBML state was available for rendering."
            evidence = "The visualisation suppresses charts unless core outputs contain finite values."
        return {
            "render": "table",
            "description": "Direct scientific answer for this metabolism lab run.",
            "data": {
                "title": f"{self.lab_title} - run interpretation",
                "columns": ["Prompt", "Answer"],
                "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", observed],
                    ["Evidence", evidence],
                    ["Dominant module", str(source.get("scope") or self.answer_focus)],
                    ["Caveat", caveat],
                ],
            },
        }

    def _timeseries(
        self,
        source: Mapping[str, Any],
        labels: Mapping[str, str],
        history: list[dict[str, float]],
    ) -> dict[str, Any] | None:
        if not history:
            return None
        alias = str(source["alias"])
        times = self._times.get(alias, [])
        observables = [str(item["id"]) for item in source.get("observables", [])]
        ranked = self._rank_observables(observables, history)[:6]
        series = []
        for oid in ranked:
            points = [[float(t), float(row[oid])] for t, row in zip(times, history) if oid in row]
            if points:
                series.append({"name": labels.get(oid, oid), "points": points})
        if not series:
            return None
        return {
            "render": "timeseries",
            "description": "Selected metabolite or pathway-state observables over model time.",
            "data": {
                "title": f"{source.get('title', self.lab_title)} observable dynamics",
                "x_label": "Model time",
                "y_label": "Native SBML value",
                "series": series,
            },
        }

    def _bar(
        self,
        source: Mapping[str, Any],
        labels: Mapping[str, str],
        history: list[dict[str, float]],
    ) -> dict[str, Any] | None:
        if not history:
            return None
        observables = [str(item["id"]) for item in source.get("observables", [])]
        items = []
        for oid in self._rank_observables(observables, history)[:8]:
            values = [row[oid] for row in history if oid in row]
            if not values:
                continue
            span = max(values) - min(values) if len(values) > 1 else abs(values[-1])
            items.append({"label": labels.get(oid, oid), "value": float(span)})
        if not items:
            return None
        return {
            "render": "bar",
            "description": "Observed SBML observables ranked by within-run excursion.",
            "data": {
                "title": "Largest observable excursions",
                "items": items,
                "x_label": "Observable",
                "y_label": "Max-min range",
            },
        }

    def _scatter(
        self,
        source: Mapping[str, Any],
        labels: Mapping[str, str],
        history: list[dict[str, float]],
    ) -> dict[str, Any] | None:
        if len(history) < 2:
            return None
        observables = self._rank_observables([str(item["id"]) for item in source.get("observables", [])], history)
        if len(observables) < 2:
            return None
        x_id, y_id = observables[0], observables[1]
        points = [
            {"x": float(row[x_id]), "y": float(row[y_id]), "series": "trajectory"}
            for row in history
            if x_id in row and y_id in row
        ]
        if len(points) < 2:
            return None
        return {
            "render": "scatter",
            "description": "Phase-style relationship between the two most active observables.",
            "data": {
                "title": "Observable phase relationship",
                "x_label": labels.get(x_id, x_id),
                "y_label": labels.get(y_id, y_id),
                "connect_points": True,
                "points": points,
            },
        }

    @staticmethod
    def _rank_observables(observables: list[str], history: list[dict[str, float]]) -> list[str]:
        scored: list[tuple[float, str]] = []
        for oid in observables:
            values = [row[oid] for row in history if oid in row]
            if not values:
                continue
            score = max(values) - min(values) if len(values) > 1 else abs(values[-1])
            scored.append((float(score), oid))
        scored.sort(reverse=True)
        return [oid for _score, oid in scored]
