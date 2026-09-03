from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIAutomationProposal:
    name: str
    description: str = ""

    triggers: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    conditions: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    actions: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    timers: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    states: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    requires_review: bool = True

    def to_dict(self):
        return {
            "name": self.name,
            "description": (
                self.description
            ),
            "triggers": [
                dict(item)
                for item
                in self.triggers
            ],
            "conditions": [
                dict(item)
                for item
                in self.conditions
            ],
            "actions": [
                dict(item)
                for item
                in self.actions
            ],
            "timers": [
                dict(item)
                for item
                in self.timers
            ],
            "states": [
                dict(item)
                for item
                in self.states
            ],
            "requires_review": (
                self.requires_review
            ),
  }
