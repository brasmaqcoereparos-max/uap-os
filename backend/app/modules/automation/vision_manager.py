from app.modules.automation.vision_registry import (
    vision_registry,
)


class VisionManager:

    def __init__(self):

        self.cameras = {}
        self.active_camera = None

    def register_camera(
        self,
        camera_id,
        camera,
    ):

        self.cameras[camera_id] = camera

    def remove_camera(
        self,
        camera_id,
    ):

        if camera_id not in self.cameras:
            return False

        self.cameras.pop(
            camera_id
        )

        if self.active_camera == camera_id:
            self.active_camera = None

        return True

    def select_camera(
        self,
        camera_id,
    ):

        if camera_id not in self.cameras:
            return False

        self.active_camera = camera_id

        return True

    def get_active_camera(self):

        if self.active_camera is None:
            return None

        return self.cameras.get(
            self.active_camera
        )

    def get_cameras(self):

        return dict(self.cameras)


vision_manager = VisionManager()
