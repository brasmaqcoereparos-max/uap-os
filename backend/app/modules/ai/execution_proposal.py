from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ai.plan import (
    AIPlan,
)


@dataclass
class AIExecutionProposal:
    plan: AIPlan

    approved: bool = False

    requires_review: bool = True

    target: str = "application"

    actions: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def approve(self):
        self.approved = True
        self.requires_review = False

        return True

    def reject(self):
        self.approved = False
        self.requires_review = True

        return True

    def to_dict(self):
        return {
            "plan": self.plan.to_dict(),
            "approved": self.approved,
            "requires_review": (
                self.requires_review
            ),
            "target": self.target,
            "actions": [
                dict(action)
                for action
                in self.actions
            ],
            "metadata": dict(
                self.metadata
            ),
        }
