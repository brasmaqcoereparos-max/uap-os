import platform
from typing import Any

from app.modules.vision.ai.local.inference_backend import (
    InferenceBackend,
)


class RaspberryPiBackend(
    InferenceBackend
):

    def __init__(self):
        self._loaded = False
        self._model = None

    def load(self):

        self._loaded = True

        return True

    def infer(
        self,
        frame: Any,
    ):

        if not self._loaded:
            self.load()

        return {
            "success": True,
            "detections": [],
        }

    def unload(self):

        self._model = None
        self._loaded = False

    def status(self):

        return {
            "platform": platform.machine(),
            "system": platform.system(),
            "loaded": self._loaded,
            "backend": "raspberry_pi",
        }


raspberry_pi_backend = (
    RaspberryPiBackend()
)
