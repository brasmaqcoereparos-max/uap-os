import json
import os
from pathlib import Path
from typing import Any


class SecureStorage:

    def __init__(
        self,
        base_path: str = ".uap_secure",
    ):
        self.base_path = Path(
            base_path
        )

    def _ensure(self):
        self.base_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write_json(
        self,
        name: str,
        data: dict[str, Any],
    ):
        self._ensure()

        path = (
            self.base_path
            / f"{name}.json"
        )

        path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
            encoding="utf-8",
        )

        try:
            os.chmod(
                path,
                0o600,
            )
        except OSError:
            pass

        return str(path)

    def read_json(
        self,
        name: str,
    ):
        path = (
            self.base_path
            / f"{name}.json"
        )

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
        path = (
            self.base_path
            / f"{name}.json"
        )

        if not path.exists():
            return False

        path.unlink()

        return True


secure_storage = SecureStorage()
