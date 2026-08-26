from app.modules.vision.camera_manager import (
    camera_manager,
)

from app.modules.vision.vision_analyzer import (
    vision_analyzer,
)

from app.modules.vision.vision_event_processor import (
    vision_event_processor,
)

from app.modules.vision.vision_events import (
    vision_events,
)

from app.modules.vision.vision_state_manager import (
    vision_state_manager,
)


class VisionPipeline:

    def process(self, camera_id):

        frame = camera_manager.capture(
            camera_id
        )

        vision_state_manager.record_frame()

        if frame is None:
            result = {
                "success": False,
                "camera_id": camera_id,
                "error": "Frame não disponível.",
            }

            vision_events.emit(
                "vision.frame.error",
                camera_id,
                result,
            )

            return result

        analysis = vision_analyzer.analyze(
            frame
        )

        result = vision_event_processor.process(
            camera_id,
            analysis,
        )

        result["camera_id"] = camera_id

        vision_events.emit(
            "vision.analysis.completed",
            camera_id,
            result,
        )

        return result


vision_pipeline = VisionPipeline()
