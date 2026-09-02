from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIAccessibility:
    label: str = ""

    description: str = ""

    role: str | None = None

    focusable: bool = True

    tab_index: int | None = None

    hidden: bool = False

    live_region: str | None = None

    attributes: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "label": self.label,
            "description": (
                self.description
            ),
            "role": self.role,
            "focusable": (
                self.focusable
            ),
            "tab_index": (
                self.tab_index
            ),
            "hidden": self.hidden,
            "live_region": (
                self.live_region
            ),
            "attributes": dict(
                self.attributes
            ),
        }
