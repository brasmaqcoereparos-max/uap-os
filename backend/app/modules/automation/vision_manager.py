from app.modules.automation.vision_registry import (
    vision_registry,
)

from app.modules.automation.vision_result import (
    VisionResult,
)


class VisionManager:
    def __init__(self):
        self.cameras = {}
        self.active_camera = None
        self.last_result = None

    def register_camera(
        self,
        camera_id,
        camera,
        replace=True,
    ):
        camera_id = str(
            camera_id
        )

        if (
            camera_id in self.cameras
            and not replace
        ):
            raise ValueError(
                "Câmera já registrada: "
                f"{camera_id}"
            )

        self.cameras[
            camera_id
        ] = camera

        return camera

    def remove_camera(
        self,
        camera_id,
    ):
        camera_id = str(
            camera_id
        )

        camera = self.cameras.pop(
            camera_id,
            None,
        )

        if camera is None:
            return False

        if (
            self.active_camera
            == camera_id
        ):
            self.active_camera = None

        return True

    def select_camera(
        self,
        camera_id,
    ):
        camera_id = str(
            camera_id
        )

        if (
            camera_id
            not in self.cameras
        ):
            return False

        self.active_camera = (
            camera_id
        )

        return True

    def get_camera(
        self,
        camera_id,
    ):
        return self.cameras.get(
            str(camera_id)
        )

    def get_active_camera(self):
        if self.active_camera is None:
            return None

        return self.cameras.get(
            self.active_camera
        )

    def get_cameras(self):
        return dict(
            self.cameras
        )

    def register_detector(
        self,
        name,
        detector,
        replace=True,
    ):
        return vision_registry.register(
            name,
            detector,
            replace=replace,
        )

    def process(
        self,
        frame=None,
        detector_name=None,
    ):
        if frame is None:
            camera = (
                self.get_active_camera()
            )

            if camera is None:
                return None

            capture = getattr(
                camera,
                "capture",
                None,
            )

            if callable(capture):
                frame = capture()
            else:
                read = getattr(
                    camera,
                    "read",
                    None,
                )

                if callable(read):
                    frame = read()

        if frame is None:
            return None

        if detector_name is None:
            detectors = (
                vision_registry.all()
            )
        else:
            detector = (
                vision_registry.get(
                    detector_name
                )
            )

            detectors = (
                [detector]
                if detector is not None
                else []
            )

        result = VisionResult()

        for detector in detectors:
            if not getattr(
                detector,
                "enabled",
                True,
            ):
                continue

            process = getattr(
                detector,
                "process",
                None,
            )

            if not callable(process):
                continue

            detection = process(
                frame
            )

            if detection is None:
                continue

            if isinstance(
                detection,
                (list, tuple),
            ):
                for item in detection:
                    result.add_detection(
                        item
                    )
            else:
                result.add_detection(
                    detection
                )

        self.last_result = result

        return result

    def clear(self):
        self.cameras.clear()
        self.active_camera = None
        self.last_result = None


vision_manager = VisionManager()
