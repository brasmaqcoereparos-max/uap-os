from app.modules.vision.cameras.camera_factory import (
    camera_factory,
)


class CameraRegistry:

    def __init__(self):
        self._cameras = {}

    def register(
        self,
        camera_id: str,
        source=0,
        width: int = 640,
        height: int = 480,
        fps: int = 15,
        metadata=None,
    ):

        camera = camera_factory.create_opencv(
            camera_id=camera_id,
            source=source,
            width=width,
            height=height,
            fps=fps,
            metadata=metadata,
        )

        self._cameras[str(camera_id)] = camera

        return camera

    def add(self, camera):
        self._cameras[camera.id] = camera
        return camera

    def get(self, camera_id):
        return self._cameras.get(
            str(camera_id)
        )

    def remove(self, camera_id):

        camera = self._cameras.pop(
            str(camera_id),
            None,
        )

        if camera is not None:
            camera.disconnect()

        return camera

    def list(self):
        return dict(self._cameras)

    def ids(self):
        return list(
            self._cameras.keys()
        )

    def count(self):
        return len(self._cameras)

    def clear(self):

        for camera in list(
            self._cameras.values()
        ):
            camera.disconnect()

        self._cameras.clear()


camera_registry = CameraRegistry()
