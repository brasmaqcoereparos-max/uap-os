from app.modules.vision.camera_manager import (
    camera_manager,
)

from app.modules.vision.vision_detector import (
    vision_detector,
)

from app.modules.vision.motion_detector import (
    motion_detector,
)

from app.modules.vision.vision_events import (
    vision_events,
)


class VisionPipeline:

    def process(
        self,
        camera_id,
    ):

        frame = camera_manager.capture(
            camera_id
        )

        if frame is None:
            return {
                "success": False,
                "camera_id": camera_id,
                "error": "Frame não disponível.",
            }

        motion = motion_detector.detect(
            frame
        )

        detections = vision_detector.detect(
            frame
        )

        result = {
            "success": True,
            "camera_id": camera_id,
            "motion": motion,
            "detections": detections,
            "persons": len(
                [
                    item
                    for item in detections
                    if item.get("class") == "person"
                ]
            ),
        }

        if motion.get("motion"):
            vision_events.emit(
                "vision.motion.detected",
                camera_id,
                motion,
            )

        if result["persons"] > 0:
            vision_events.emit(
                "vision.person.detected",
                camera_id,
                {
                    "count": result["persons"],
                },
            )

        vision_events.emit(
            "vision.analysis.completed",
            camera_id,
            result,
        )

        return result


vision_pipeline = VisionPipeline()
