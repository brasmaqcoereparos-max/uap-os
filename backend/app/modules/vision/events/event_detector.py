from app.modules.vision.events.vision_event import (
    VisionEvent,
)


class EventDetector:

    def detect(
        self,
        camera_id,
        analysis,
    ):

        events = []

        if not isinstance(
            analysis,
            dict,
        ):
            return events

        motion = analysis.get(
            "motion",
            {},
        )

        if (
            isinstance(motion, dict)
            and motion.get("motion")
        ):
            events.append(
                VisionEvent(
                    event_type="motion",
                    camera_id=camera_id,
                    data=motion,
                )
            )

        persons = analysis.get(
            "persons",
            0,
        )

        if persons:
            events.append(
                VisionEvent(
                    event_type="person_detected",
                    camera_id=camera_id,
                    data={
                        "count": persons,
                    },
                )
            )

        detections = analysis.get(
            "detections",
            [],
        )

        if detections:
            events.append(
                VisionEvent(
                    event_type="object_detected",
                    camera_id=camera_id,
                    data={
                        "detections": detections,
                    },
                )
            )

        return events


event_detector = EventDetector()
