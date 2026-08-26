from app.modules.vision.vision_service import (
    vision_service,
)

from app.runtime.runtime_events import (
    runtime_events,
)


class VisionRuntimeBridge:

    def execute(self, command):

        result = vision_service.execute(
            command
        )

        runtime_events.emit(
            "vision.result",
            "vision_runtime_bridge",
            result,
        )

        return result

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


vision_runtime_bridge = VisionRuntimeBridge()
