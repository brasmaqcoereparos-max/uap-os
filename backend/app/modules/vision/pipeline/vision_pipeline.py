from typing import Any

from app.modules.vision.processing.frame_analyzer import (
    frame_analyzer,
)

from app.modules.vision.detection.detection_service import (
    detection_service,
)

from app.modules.vision.events.vision_event_service import (
    vision_event_service,
)

from app.modules.vision.decision.decision_service import (
    decision_service,
)

from app.modules.vision.automation.automation_flow_executor import (
    automation_flow_executor,
)


class VisionPipeline:

    def analyze_frame(
        self,
        camera_id: str | None,
        frame: Any,
    ):

        analysis = frame_analyzer.analyze(
            frame
        )

        persons = detection_service.count_persons(
            frame
        )

        detections = detection_service.objects(
            frame
        )

        analysis["persons"] = persons
        analysis["detections"] = detections

        return analysis

    def process(
        self,
        camera_id: str | None,
        frame: Any,
    ):

        analysis = self.analyze_frame(
            camera_id,
            frame,
        )

        events = vision_event_service.process(
            camera_id,
            analysis,
        )

        decisions = decision_service.evaluate(
            analysis
        )

        actions = decision_service.evaluate_actions(
            analysis
        )

        return {
            "camera_id": camera_id,
            "analysis": analysis,
            "events": events,
            "decisions": [
                rule.to_dict()
                for rule in decisions
            ],
            "actions": actions,
        }

    def execute_flow(
        self,
        flow_name: str,
        context: dict,
    ):

        return automation_flow_executor.execute(
            flow_name,
            context,
        )


vision_pipeline = VisionPipeline()
