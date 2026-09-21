from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MetricsPersistence:

    VERSION = 1

    def __init__(
        self,
        base_path: (
            str | Path
        ) = "data/metrics",
    ):
        self.base_path = Path(
            base_path
        )

    def _ensure_directory(
        self,
    ):
        self.base_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _safe_name(
        self,
        name: str,
    ) -> str:
        normalized = str(
            name
        ).strip()

        if not normalized:
            raise ValueError(
                "Persistence name "
                "cannot be empty"
            )

        return "".join(
            character
            if (
                character.isalnum()
                or character
                in {
                    "-",
                    "_",
                }
            )
            else "_"
            for character
            in normalized
        )

    def _path(
        self,
        name: str,
    ) -> Path:
        return (
            self.base_path
            / (
                self._safe_name(
                    name
                )
                + ".json"
            )
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
                "Metrics persistence "
                "data must be a dict"
            )

        self._ensure_directory()

        path = self._path(
            name
        )

        temporary = (
            path.with_suffix(
                ".tmp"
            )
        )

        package = {
            "version": (
                self.VERSION
            ),
            "data": data,
        }

        temporary.write_text(
            json.dumps(
                package,
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
    ):

        path = self._path(
            name
        )

        if not path.exists():
            return None

        package = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        if (
            package.get(
                "version"
            )
            != self.VERSION
        ):
            raise ValueError(
                "Unsupported metrics "
                "persistence version"
            )

        data = package.get(
            "data"
        )

        if not isinstance(
            data,
            dict,
        ):
            raise ValueError(
                "Invalid metrics "
                "persistence data"
            )

        return data

    def delete(
        self,
        name: str,
    ) -> bool:

        path = self._path(
            name
        )

        if not path.exists():
            return False

        path.unlink()

        return True


metrics_persistence = (
    MetricsPersistence()
      )
