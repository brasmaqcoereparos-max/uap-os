from __future__ import annotations

from app.modules.education.schemas import (
    LabScenario,
)


class LabService:

    def __init__(self):
        self._scenarios: dict[
            str,
            LabScenario,
        ] = {}

    def register(
        self,
        scenario: LabScenario,
    ):
        if not scenario.simulation_only:
            raise ValueError(
                "Education laboratory "
                "must start in simulation mode"
            )

        self._scenarios[
            scenario.id
        ] = scenario

        return scenario

    def create(
        self,
        scenario_id: str,
        name: str,
        description: str = "",
        difficulty: str = "beginner",
        project_template=None,
        expected_state=None,
        metadata=None,
    ):
        scenario = LabScenario(
            id=scenario_id,
            name=name,
            description=description,
            difficulty=difficulty,
            project_template=dict(
                project_template or {}
            ),
            expected_state=dict(
                expected_state or {}
            ),
            simulation_only=True,
            metadata=dict(
                metadata or {}
            ),
        )

        return self.register(
            scenario
        )

    def get(
        self,
        scenario_id: str,
    ):
        return self._scenarios.get(
            scenario_id
        )

    def require(
        self,
        scenario_id: str,
    ):
        scenario = self.get(
            scenario_id
        )

        if scenario is None:
            raise KeyError(
                "Lab scenario not found: "
                f"{scenario_id}"
            )

        return scenario

    def start(
        self,
        scenario_id: str,
    ):
        scenario = self.require(
            scenario_id
        )

        return {
            "scenario_id": (
                scenario.id
            ),
            "status": "ready",
            "simulation_only": True,
            "project_template": dict(
                scenario.project_template
            ),
        }

    def list_all(self):
        return list(
            self._scenarios.values()
        )


lab_service = LabService()
