from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


VALID_STUDIO_LEVELS = {
    "beginner",
    "intermediate",
    "professional",
}


@dataclass(frozen=True)
class UIStudioLevelPolicy:
    level: str

    visible_panels: tuple[str, ...]

    capabilities: dict[
        str,
        bool,
    ] = field(
        default_factory=dict
    )

    def allows_panel(
        self,
        panel_id: str,
    ) -> bool:
        return (
            panel_id
            in self.visible_panels
        )

    def allows(
        self,
        capability: str,
    ) -> bool:
        return bool(
            self.capabilities.get(
                capability,
                False,
            )
        )

    def filter_panels(
        self,
        panels: list,
    ) -> list:
        return [
            panel
            for panel in panels
            if self.allows_panel(
                panel.id
            )
        ]

    def filter_dock_snapshot(
        self,
        snapshot: dict[str, Any],
    ) -> dict[str, Any]:
        result = {}

        for (
            position,
            area,
        ) in snapshot.items():
            data = dict(
                area
            )

            panel_ids = [
                panel_id
                for panel_id
                in data.get(
                    "panel_ids",
                    [],
                )
                if self.allows_panel(
                    panel_id
                )
            ]

            active_panel_id = (
                data.get(
                    "active_panel_id"
                )
            )

            if (
                active_panel_id
                not in panel_ids
            ):
                active_panel_id = (
                    panel_ids[0]
                    if panel_ids
                    else None
                )

            data[
                "panel_ids"
            ] = panel_ids

            data[
                "active_panel_id"
            ] = active_panel_id

            result[
                position
            ] = data

        return result

    def to_dict(self):
        return {
            "level": self.level,
            "visible_panels": list(
                self.visible_panels
            ),
            "capabilities": dict(
                self.capabilities
            ),
        }


_POLICIES = {
    "beginner": UIStudioLevelPolicy(
        level="beginner",
        visible_panels=(
            "palette",
            "properties",
            "preview",
        ),
        capabilities={
            "visual_editor": True,
            "drag_drop": True,
            "preview": True,
            "basic_properties": True,
            "advanced_properties": False,
            "events": False,
            "hierarchy": False,
            "console": False,
            "hardware_details": False,
            "code_details": False,
        },
    ),
    "intermediate": UIStudioLevelPolicy(
        level="intermediate",
        visible_panels=(
            "palette",
            "hierarchy",
            "properties",
            "events",
            "preview",
        ),
        capabilities={
            "visual_editor": True,
            "drag_drop": True,
            "preview": True,
            "basic_properties": True,
            "advanced_properties": True,
            "events": True,
            "hierarchy": True,
            "console": False,
            "hardware_details": False,
            "code_details": False,
        },
    ),
    "professional": UIStudioLevelPolicy(
        level="professional",
        visible_panels=(
            "palette",
            "hierarchy",
            "properties",
            "events",
            "console",
            "preview",
        ),
        capabilities={
            "visual_editor": True,
            "drag_drop": True,
            "preview": True,
            "basic_properties": True,
            "advanced_properties": True,
            "events": True,
            "hierarchy": True,
            "console": True,
            "hardware_details": True,
            "code_details": True,
        },
    ),
}


def get_studio_level_policy(
    level: str,
) -> UIStudioLevelPolicy:
    normalized = str(
        level
    ).strip().lower()

    if (
        normalized
        not in VALID_STUDIO_LEVELS
    ):
        raise ValueError(
            "Unsupported studio level: "
            f"{level}"
        )

    return _POLICIES[
        normalized
          ]
