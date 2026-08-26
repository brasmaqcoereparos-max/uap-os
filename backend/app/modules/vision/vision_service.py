from app.modules.vision.vision_router import (
    vision_router,
)


class VisionService:

    def execute(self, command):
        return vision_router.route(
            command
        )

    def analyze(self, camera_id):
        return self.execute(
            {
                "action": "vision.analyze",
                "camera_id": camera_id,
            }
        )

    def capture(self, camera_id):
        return self.execute(
            {
                "action": "vision.camera.capture",
                "camera_id": camera_id,
            }
        )

    def start(self, camera_id):
        return self.execute(
            {
                "action": "vision.camera.start",
                "camera_id": camera_id,
            }
        )

    def stop(self, camera_id):
        return self.execute(
            {
                "action": "vision.camera.stop",
                "camera_id": camera_id,
            }
        )

    def status(self, camera_id):
        return self.execute(
            {
                "action": "vision.camera.status",
                "camera_id": camera_id,
            }
        )


vision_service = VisionService()
