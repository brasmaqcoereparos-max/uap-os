import json
from pathlib import Path
from typing import Any


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
    ):
        safe_name = Path(
            name
        ).name

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
    ):
        path = self._resolve(name)

        temporary = path.with_suffix(
            ".tmp"
        )

        temporary.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        temporary.replace(path)

        return path

    def load(
        self,
        name: str,
    ):
        path = self._resolve(name)

        if not path.exists():
            return None

        return json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

    def delete(
        self,
        name: str,
    ):
        path = self._resolve(name)

        if not path.exists():
            return False

        path.unlink()

        return True

    def exists(
        self,
        name: str,
    ):
        return self._resolve(
            name
        ).exists()

    def list_files(self):
        return sorted(
            path.name
            for path
            in self.base_path.glob(
                "*.json"
            )
    )
