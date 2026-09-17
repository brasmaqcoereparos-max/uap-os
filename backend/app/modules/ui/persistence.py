from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.modules.ui.screen import (
    UIScreen,
)
from app.modules.ui.serializer import (
    UISerializer,
)
from app.modules.ui.theme import (
    UITheme,
)


class UIPersistence:

    def __init__(
        self,
        base_path: str | Path,
    ):
        self.base_path = Path(
            base_path
        )

        self.base_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _resolve(
        self,
        name: str,
    ) -> Path:
        safe_name = Path(
            str(name)
        ).name

        if not safe_name:
            raise ValueError(
                "Persistence name "
                "cannot be empty"
            )

        if not safe_name.endswith(
            ".json"
        ):
            safe_name = (
                f"{safe_name}.json"
            )

        return (
            self.base_path
            / safe_name
        )

    def save(
        self,
        name: str,
        data: dict[str, Any],
    ) -> Path:
        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "Persistence data "
                "must be a dict"
            )

        path = self._resolve(
            name
        )

        temporary = (
            path.with_suffix(
                ".tmp"
            )
        )

        temporary.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        temporary.replace(
            path
        )

        return path

    def load(
        self,
        name: str,
    ) -> dict[str, Any] | None:
        path = self._resolve(
            name
        )

        if not path.exists():
            return None

        data = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        if not isinstance(
            data,
            dict,
        ):
            raise ValueError(
                "Persisted UI data "
                "must be a dict"
            )

        return data

    def save_screen(
        self,
        name: str,
        screen: UIScreen,
    ) -> Path:
        return self.save(
            name,
            {
                "type": "ui_screen",
                "version": 1,
                "data": (
                    UISerializer
                    .screen_to_dict(
                        screen
                    )
                ),
            },
        )

    def load_screen(
        self,
        name: str,
    ) -> UIScreen | None:
        package = self.load(
            name
        )

        if package is None:
            return None

        if (
            package.get(
                "type"
            )
            != "ui_screen"
        ):
            raise ValueError(
                "Persisted object is "
                "not a UI screen"
            )

        data = package.get(
            "data"
        )

        if not isinstance(
            data,
            dict,
        ):
            raise ValueError(
                "Invalid UI screen "
                "persistence data"
            )

        return (
            UISerializer
            .screen_from_dict(
                data
            )
        )

    def save_theme(
        self,
        name: str,
        theme: UITheme,
    ) -> Path:
        return self.save(
            name,
            {
                "type": "ui_theme",
                "version": 1,
                "data": (
                    UISerializer
                    .theme_to_dict(
                        theme
                    )
                ),
            },
        )

    def load_theme(
        self,
        name: str,
    ) -> UITheme | None:
        package = self.load(
            name
        )

        if package is None:
            return None

        if (
            package.get(
                "type"
            )
            != "ui_theme"
        ):
            raise ValueError(
                "Persisted object is "
                "not a UI theme"
            )

        data = package.get(
            "data"
        )

        if not isinstance(
            data,
            dict,
        ):
            raise ValueError(
                "Invalid UI theme "
                "persistence data"
            )

        return (
            UISerializer
            .theme_from_dict(
                data
            )
        )

    def delete(
        self,
        name: str,
    ) -> bool:
        path = self._resolve(
            name
        )

        if not path.exists():
            return False

        path.unlink()

        return True

    def exists(
        self,
        name: str,
    ) -> bool:
        return (
            self._resolve(
                name
            ).exists()
        )

    def list_files(
        self,
    ) -> list[str]:
        return sorted(
            path.name
            for path
            in self.base_path.glob(
                "*.json"
            )
        )
