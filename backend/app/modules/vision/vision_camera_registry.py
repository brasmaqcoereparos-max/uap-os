from app.modules.vision.camera_factory import (
    camera_factory,
)

from app.modules.vision.camera_manager import (
    camera_manager,
)


class VisionCameraRegistry:

    def register(
        self,
        camera_id: str,
        source=0,
    ):

        camera = camera_factory.create(
            camera_id,
            source,
        )

        camera_manager.register(
            camera_id,
            camera,
        )

        return camera

    def unregister(
        self,
        camera_id: str,
    ):

        camera = camera_manager.unregister(
            camera_id
        )

        if camera is not None:

            stop = getattr(
                camera,
                "stop",
                None,
            )

            if callable(stop):
                stop()

        return camera

    def get(self, camera_id):
        return camera_manager.get(
            camera_id
        )

    def list(self):
        return camera_manager.list()

    def count(self):
        return camera_manager.count()


vision_camera_registry = (
    VisionCameraRegistry()
      )
