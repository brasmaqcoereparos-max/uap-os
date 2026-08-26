from app.modules.vision.camera_manager import (
    camera_manager,
)

from app.modules.vision.vision_events import (
    vision_events,
)


class VisionManager:

    def register_camera(
        self,
        camera_id,
        camera,
    ):
        return camera_manager.register(
            camera_id,
            camera,
        )

    def remove_camera(
        self,
        camera_id,
    ):
        return camera_manager.unregister(
            camera_id
        )

    def cameras(self):
        return camera_manager.list()

    def camera_count(self):
        return camera_manager.count()

    def capture(
        self,
        camera_id,
    ):

        frame = camera_manager.capture(
            camera_id
        )

        vision_events.emit(
            "vision.frame.captured",
            camera_id,
            {
                "frame_available": frame is not None,
            },
        )

        return frame

    def start(
        self,
        camera_id,
    ):

        result = camera_manager.start(
            camera_id
        )

        vision_events.emit(
            "vision.camera.started",
            camera_id,
        )

        return result

    def stop(
        self,
        camera_id,
    ):

        result = camera_manager.stop(
            camera_id
        )

        vision_events.emit(
            "vision.camera.stopped",
            camera_id,
        )

        return result

    def status(
        self,
        camera_id,
    ):
        return camera_manager.status(
            camera_id
        )

    def emit_detection(
        self,
        camera_id,
        detection_type,
        data=None,
    ):

        return vision_events.emit(
            detection_type,
            camera_id,
            data,
        )


vision_manager = VisionManager()
