from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIMenuItem:
    id: str
    label: str

    target_screen_id: (
        str | None
    ) = None

    icon: str | None = None

    enabled: bool = True
    visible: bool = True

    order: int = 0

    children: list[
        "UIMenuItem"
    ] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_child(
        self,
        item: "UIMenuItem",
    ):
        self.children.append(item)

        return item

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "target_screen_id": (
                self.target_screen_id
            ),
            "icon": self.icon,
            "enabled": self.enabled,
            "visible": self.visible,
            "order": self.order,
            "children": [
                child.to_dict()
                for child in sorted(
                    self.children,
                    key=lambda item: (
                        item.order
                    ),
                )
            ],
            "metadata": dict(
                self.metadata
            ),
        }
