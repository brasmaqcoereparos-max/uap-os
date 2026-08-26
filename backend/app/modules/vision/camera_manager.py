from typing import Any


class CameraManager:

    def __init__(self):
        self._cameras: dict[str, Any] = {}

    def register(
        self,
        camera_id: str,
        camera: Any,
    ):
        if not camera_id:
            raise ValueError(
                "camera_id obrigatório."
            )

        self._cameras[str(camera_id)] = camera

        return camera

    def unregister(
        self,
        camera_id: str,
    ):
        return self._cameras.pop(
            str(camera_id),
            None,
        )

    def get(
        self,
        camera_id: str,
    ):
        return self._cameras.get(
            str(camera_id)
        )

    def exists(
        self,
        camera_id: str,
    ):
        return str(camera_id) in self._cameras

    def list(self):
        return dict(self._cameras)

    def count(self):
        return len(self._cameras)

    def clear(self):
        self._cameras.clear()

    def capture(
        self,
        camera_id: str,
    ):
        camera = self._require(
            camera_id
        )

        method = getattr(
            camera,
            "capture",
            None,
        )

        if not callable(method):
            raise RuntimeError(
                "Câmera não possui método capture."
            )

        return method()

    def start(
        self,
        camera_id: str,
    ):
        camera = self._require(
            camera_id
        )

        method = getattr(
            camera,
            "start",
            None,
        )

        if not callable(method):
            raise RuntimeError(
                "Câmera não possui método start."
            )

        return method()

    def stop(
        self,
        camera_id: str,
    ):
        camera = self._require(
            camera_id
        )

        method = getattr(
            camera,
            "stop",
            None,
        )

        if not callable(method):
            raise RuntimeError(
                "Câmera não possui método stop."
            )

        return method()

    def status(
        self,
        camera_id: str,
    ):
        camera = self._require(
            camera_id
        )

        method = getattr(
            camera,
            "status",
            None,
        )

        if callable(method):
            return method()

        return {
            "id": camera_id,
            "registered": True,
        }

    def _require(
        self,
        camera_id: str,
    ):
        camera = self.get(camera_id)

        if camera is None:
            raise KeyError(
                f"Câmera '{camera_id}' não encontrada."
            )

        return camera


camera_manager = CameraManager()
