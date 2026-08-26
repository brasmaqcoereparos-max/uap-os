from app.modules.vision.vision_events import (
    vision_events,
)

from app.modules.vision.vision_state_manager import (
    vision_state_manager,
)


class VisionEventProcessor:

    def process(
        self,
        camera_id,
        analysis,
    ):

        if not analysis.get("success"):
            return analysis

        motion = analysis.get(
            "motion",
            {},
        )

        detections = analysis.get(
            "detections",
            [],
        )

        persons = int(
            analysis.get(
                "persons",
                0,
            )
        )

        vision_state_manager.record_analysis()

        if detections:
            vision_state_manager.record_detection(
                len(detections)
            )

        if motion.get("motion"):
            vision_state_manager.record_motion()

            vision_events.emit(
                "vision.motion.detected",
                camera_id,
                motion,
            )

        if persons > 0:
            vision_state_manager.record_person()

            vision_events.emit(
                "vision.person.detected",
                camera_id,
                {
                    "count": persons,
                },
            )

        vision_state_manager.set_analysis(
            analysis
        )

        return analysis


vision_event_processor = VisionEventProcessor()
