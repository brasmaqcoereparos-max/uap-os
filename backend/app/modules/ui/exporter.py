import json
from typing import Any

from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.state import (
    ui_state,
)


class UIExporter:

    @staticmethod
    def export_runtime():
        return {
            "version": 1,
            "screens": [
                screen.to_dict()
                for screen
                in ui_registry.list_screens()
            ],
            "themes": [
                theme.to_dict()
                for theme
                in ui_registry.list_themes()
            ],
            "state": (
                ui_state.snapshot()
            ),
        }

    @staticmethod
    def export_json():
        return json.dumps(
            UIExporter.export_runtime(),
            ensure_ascii=False,
            indent=2,
        )

    @staticmethod
    def package(
        metadata: (
            dict[str, Any] | None
        ) = None,
    ):
        return {
            "metadata": dict(
                metadata or {}
            ),
            "ui": (
                UIExporter
                .export_runtime()
            ),
        }
