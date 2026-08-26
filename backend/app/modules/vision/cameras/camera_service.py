from app.modules.vision.cameras.camera_registry import (
    camera_registry,
)


class CameraService:

    def register(
        self,
        camera_id,
        source=0,
        width=640,
        height=480,
        fps=15,
        metadata=None,
    ):

        return camera_registry.register(
            camera_id=camera_id,
            source=source,
            width=width,
            height=height,
            fps=fps,
            metadata=metadata,
        )

    def remove(self, camera_id):
        return camera_registry.remove(
            camera_id
        )

    def get(self, camera_id):

        camera = camera_registry.get(
            camera_id
        )

        if camera is None:
            raise KeyError(
                f"Câmera '{camera_id}' não encontrada."
            )

        return camera

    def list(self):
        return list(
            camera_registry.list().values()
        )

    def start(self, camera_id):
        return self.get(
            camera_id
        ).connect()

    def stop(self, camera_id):
        return self.get(
            camera_id
        ).disconnect()

    def capture(self, camera_id):
        return self.get(
            camera_id
        ).capture()

    def status(self, camera_id):
        return self.get(
            camera_id
        ).status()

    def status_all(self):

        return [
            camera.status()
            for camera in self.list()
        ]


camera_service = CameraService()
