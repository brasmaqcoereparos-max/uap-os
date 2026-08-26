from typing import Any

from app.modules.vision.cameras.camera_backend import (
    CameraBackend,
)


class CameraDevice:

    def __init__(
        self,
        camera_id: str,
        backend: CameraBackend,
        metadata: dict[str, Any] | None = None,
    ):
        self.id = str(camera_id)
        self.backend = backend
        self.metadata = metadata or {}

    def connect(self):
        return self.backend.start()

    def disconnect(self):
        return self.backend.stop()

    def capture(self):
        return self.backend.capture()

    def read(self):
        return self.capture()

    def write(self, value):
        raise RuntimeError(
            "Câmera não suporta escrita."
        )

    def status(self):

        status = self.backend.status()

        return {
            "id": self.id,
            "type": "camera",
            "backend": status,
            "metadata": dict(
                self.metadata
            ),
        }

    def is_available(self):
        return self.backend.available()
