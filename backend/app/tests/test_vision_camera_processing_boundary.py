from app.modules.vision.cameras.camera_backend import (
    CameraBackend,
)
from app.modules.vision.cameras.camera_device import (
    CameraDevice,
)
from app.modules.vision.cameras.camera_registry import (
    camera_registry,
)
from app.modules.vision.pipeline.pipeline_service import (
    PipelineService,
)


class FakeFrame:

    def __init__(
        self,
        width=640,
        height=480,
        channels=3,
    ):
        self.shape = (
            height,
            width,
            channels,
        )


class FakeCameraBackend(
    CameraBackend
):

    def __init__(
        self,
        frame=None,
    ):
        self.frame = frame

        self.running = False

    def start(self):
        self.running = True

        return True

    def stop(self):
        self.running = False

        return True

    def capture(self):
        if not self.running:
            self.start()

        return self.frame

    def status(self):
        return {
            "running": (
                self.running
            ),
            "available": True,
        }


def install_fake_camera(
    camera_id: str,
    frame,
):
    camera = CameraDevice(
        camera_id=camera_id,
        backend=(
            FakeCameraBackend(
                frame=frame
            )
        ),
        metadata={
            "test": True,
        },
    )

    camera_registry.add(
        camera
    )

    return camera


def test_camera_device_capture_contract():
    frame = FakeFrame()

    camera = install_fake_camera(
        "camera-test-1",
        frame,
    )

    captured = camera.capture()

    assert captured is frame

    assert (
        camera.status()[
            "type"
        ]
        == "camera"
    )

    camera_registry.remove(
        "camera-test-1"
    )


def test_pipeline_service_captures_frame():
    frame = FakeFrame()

    install_fake_camera(
        "camera-test-2",
        frame,
    )

    service = PipelineService()

    captured = (
        service.capture_frame(
            "camera-test-2"
        )
    )

    assert captured is frame

    camera_registry.remove(
        "camera-test-2"
    )


def test_pipeline_returns_failure_when_frame_missing():
    install_fake_camera(
        "camera-empty",
        None,
    )

    service = PipelineService()

    result = (
        service.capture_and_process(
            "camera-empty"
        )
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["camera_id"]
        == "camera-empty"
    )

    assert (
        result["error"]
        is not None
    )

    camera_registry.remove(
        "camera-empty"
    )


def test_camera_status_reaches_pipeline_service():
    frame = FakeFrame()

    install_fake_camera(
        "camera-status",
        frame,
    )

    service = PipelineService()

    status = (
        service.camera_status(
            "camera-status"
        )
    )

    assert (
        status["id"]
        == "camera-status"
    )

    assert (
        status["type"]
        == "camera"
    )

    assert (
        status["backend"][
            "available"
        ]
        is True
    )

    camera_registry.remove(
        "camera-status"
    )


def test_missing_camera_is_rejected():
    service = PipelineService()

    try:
        service.capture_and_process(
            "camera-not-found"
        )

        raised = False

    except KeyError:
        raised = True

    assert raised is True
