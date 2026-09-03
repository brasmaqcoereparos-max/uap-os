from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIUIProposal:
    name: str

    screen_type: str = "standard"

    screens: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    widgets: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    navigation: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    theme: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    requires_review: bool = True

    def to_dict(self):
        return {
            "name": self.name,
            "screen_type": (
                self.screen_type
            ),
            "screens": [
                dict(item)
                for item
                in self.screens
            ],
            "widgets": [
                dict(item)
                for item
                in self.widgets
            ],
            "navigation": [
                dict(item)
                for item
                in self.navigation
            ],
            "theme": dict(
                self.theme
            ),
            "requires_review": (
                self.requires_review
            ),
        }
