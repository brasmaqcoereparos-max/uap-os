import json
from pathlib import Path

from app.modules.simulator.programming.canvas.device_export import (
    device_export,
)
from app.modules.simulator.programming.canvas.device_import import (
    device_import,
)


class DevicePersistence:

    def save(
        self,
        filename,
    ):

        Path(filename).write_text(

            device_export.export(),

            encoding="utf-8",

        )

    def load(
        self,
        filename,
    ):

        content = Path(filename).read_text(

            encoding="utf-8",

        )

        device_import.import_json(content)

    def exists(
        self,
        filename,
    ):

        return Path(filename).exists()


device_persistence = DevicePersistence()
