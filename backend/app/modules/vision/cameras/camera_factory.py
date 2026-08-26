from app.modules.vision.cameras.camera_device import (
    CameraDevice,
)

from app.modules.vision.cameras.opencv_camera import (
    OpenCVCamera,
)


class CameraFactory:

    def create_opencv(
        self,
        camera_id: str,
        source=0,
        width: int = 640,
        height: int = 480,
        fps: int = 15,
        metadata=None,
    ):

        backend = OpenCVCamera(
            camera_id=camera_id,
            source=source,
            width=width,
            height=height,
            fps=fps,
        )

        return CameraDevice(
            camera_id=camera_id,
            backend=backend,
            metadata=metadata,
        )


camera_factory = CameraFactory()
