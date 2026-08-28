class VisionBase:
    def __init__(
        self,
        camera_id=None,
        metadata=None,
    ):
        self.enabled = False

        self.camera_id = (
            str(camera_id)
            if camera_id is not None
            else None
        )

        self.metadata = dict(
            metadata or {}
        )

        self.last_result = None

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

    def set_camera(self, camera_id):
        self.camera_id = (
            str(camera_id)
            if camera_id is not None
            else None
        )

        return self.camera_id

    def is_enabled(self):
        return self.enabled

    def get_camera(self):
        return self.camera_id

    def process(self, frame):
        if not self.enabled:
            return None

        self.last_result = frame

        return frame

    def reset(self):
        self.last_result = None

    def to_dict(self):
        return {
            "enabled": self.enabled,
            "camera_id": (
                self.camera_id
            ),
            "has_result": (
                self.last_result
                is not None
            ),
            "metadata": dict(
                self.metadata
            ),
    }
