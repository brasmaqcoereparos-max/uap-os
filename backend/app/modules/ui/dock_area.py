from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass
class UIDockArea:
    position: str

    panel_ids: list[
        str
    ] = field(
        default_factory=list
    )

    active_panel_id: (
        str | None
    ) = None

    def add(
        self,
        panel_id: str,
    ):
        if (
            panel_id
            not in self.panel_ids
        ):
            self.panel_ids.append(
                panel_id
            )

        if (
            self.active_panel_id
            is None
        ):
            self.active_panel_id = (
                panel_id
            )

        return panel_id

    def remove(
        self,
        panel_id: str,
    ):
        if (
            panel_id
            not in self.panel_ids
        ):
            return False

        self.panel_ids.remove(
            panel_id
        )

        if (
            self.active_panel_id
            == panel_id
        ):
            self.active_panel_id = (
                self.panel_ids[0]
                if self.panel_ids
                else None
            )

        return True

    def activate(
        self,
        panel_id: str,
    ):
        if (
            panel_id
            not in self.panel_ids
        ):
            return False

        self.active_panel_id = (
            panel_id
        )

        return True

    def move(
        self,
        panel_id: str,
        index: int,
    ) -> bool:
        if (
            panel_id
            not in self.panel_ids
        ):
            return False

        self.panel_ids.remove(
            panel_id
        )

        index = max(
            0,
            min(
                int(index),
                len(self.panel_ids),
            ),
        )

        self.panel_ids.insert(
            index,
            panel_id,
        )

        return True

    def contains(
        self,
        panel_id: str,
    ) -> bool:
        return (
            panel_id
            in self.panel_ids
        )

    def clear(self) -> None:
        self.panel_ids.clear()
        self.active_panel_id = None

    def to_dict(self):
        return {
            "position": self.position,
            "panel_ids": list(
                self.panel_ids
            ),
            "active_panel_id": (
                self.active_panel_id
            ),
        }
