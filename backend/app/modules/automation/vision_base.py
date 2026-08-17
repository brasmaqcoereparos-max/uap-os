class VisionBase:

    def __init__(self):

        self.enabled = False
        self.camera_id = None

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def set_camera(self, camera_id):

        self.camera_id = camera_id

    def is_enabled(self):

        return self.enabled

    def get_camera(self):

        return self.camera_id
