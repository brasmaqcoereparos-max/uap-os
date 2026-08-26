from app.modules.vision.camera_source import (
    CameraSource,
)


class CameraFactory:

    def create(
        self,
        camera_id: str,
        source=0,
    ):

        return CameraSource(
            camera_id=camera_id,
            source=source,
        )


camera_factory = CameraFactory()
