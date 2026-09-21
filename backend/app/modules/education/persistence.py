from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


class EducationPersistence:

    VERSION = 1

    def __init__(
        self,
        base_path: (
            str | Path | None
        ) = None,
    ):
        configured = (
            base_path
            or os.getenv(
                "UAP_EDUCATION_DATA_DIR"
            )
            or (
                Path("data")
                / "education"
            )
        )

        self.base_path = Path(
            configured
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

        safe = "".join(
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

        if not safe:
            raise ValueError(
                "Invalid persistence name"
            )

        return safe

    def _path(
        self,
        name: str,
    ):
        safe = self._safe_name(
            name
        )

        return (
            self.base_path
            / f"{safe}.json"
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
                "Education persistence "
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
    ) -> dict[str, Any] | None:

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

        if not isinstance(
            package,
            dict,
        ):
            raise ValueError(
                "Invalid education "
                "persistence package"
            )

        version = package.get(
            "version"
        )

        if version != self.VERSION:
            raise ValueError(
                "Unsupported education "
                "persistence version: "
                f"{version}"
            )

        data = package.get(
            "data"
        )

        if not isinstance(
            data,
            dict,
        ):
            raise ValueError(
                "Invalid education "
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

    def exists(
        self,
        name: str,
    ) -> bool:

        return self._path(
            name
        ).exists()

    def list_files(
        self,
    ) -> list[str]:

        if not self.base_path.exists():
            return []

        return sorted(
            path.name
            for path
            in self.base_path.glob(
                "*.json"
            )
        )


education_persistence = (
    EducationPersistence()
      )
