from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ai.project_requirement import (
    AIProjectRequirement,
)


@dataclass
class AIProjectSpec:
    id: str
    name: str

    objective: str

    requirements: list[
        AIProjectRequirement
    ] = field(
        default_factory=list
    )

    hardware: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    software: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    ui: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    automation: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    risks: list[str] = field(
        default_factory=list
    )

    tests: list[str] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_requirement(
        self,
        requirement: (
            AIProjectRequirement
        ),
    ):
        self.requirements.append(
            requirement
        )

        return requirement

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "objective": (
                self.objective
            ),
            "requirements": [
                requirement.to_dict()
                for requirement
                in self.requirements
            ],
            "hardware": [
                dict(item)
                for item in self.hardware
            ],
            "software": [
                dict(item)
                for item in self.software
            ],
            "ui": [
                dict(item)
                for item in self.ui
            ],
            "automation": [
                dict(item)
                for item in self.automation
            ],
            "risks": list(
                self.risks
            ),
            "tests": list(
                self.tests
            ),
            "metadata": dict(
                self.metadata
            ),
        }
