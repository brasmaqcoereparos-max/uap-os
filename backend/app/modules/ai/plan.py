from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ai.plan_step import (
    AIPlanStep,
)


@dataclass
class AIPlan:
    id: str
    objective: str

    title: str = ""

    steps: list[
        AIPlanStep
    ] = field(
        default_factory=list
    )

    status: str = "draft"

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_step(
        self,
        step: AIPlanStep,
    ):
        if self.get_step(step.id):
            raise ValueError(
                "Plan step already exists: "
                f"{step.id}"
            )

        self.steps.append(step)

        self.steps.sort(
            key=lambda item: (
                item.order,
                item.id,
            )
        )

        return step

    def get_step(
        self,
        step_id: str,
    ):
        for step in self.steps:
            if step.id == step_id:
                return step

        return None

    def remove_step(
        self,
        step_id: str,
    ):
        step = self.get_step(
            step_id
        )

        if not step:
            return False

        self.steps.remove(step)

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "objective": (
                self.objective
            ),
            "title": self.title,
            "status": self.status,
            "steps": [
                step.to_dict()
                for step
                in self.steps
            ],
            "metadata": dict(
                self.metadata
            ),
        }
