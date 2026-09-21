from typing import Any

from app.modules.vision.ai.ai_service import (
    ai_service,
)
from app.modules.vision.automation.automation_flow_executor import (
    automation_flow_executor,
)
from app.modules.vision.automation.vision_event_actions import (
    vision_event_actions,
)
from app.modules.vision.decision.decision_service import (
    decision_service,
)
from app.modules.vision.detection.detection_service import (
    detection_service,
)
from app.modules.vision.events.vision_event_service import (
    vision_event_service,
)
from app.modules.vision.processing.frame_analyzer import (
    frame_analyzer,
)
from app.modules.vision.vision_config import (
    vision_config,
)


class VisionPipeline:

    def analyze_frame(
        self,
        camera_id: str | None,
        frame: Any,
    ):

        analysis = (
            frame_analyzer.analyze(
                frame
            )
        )

        if (
            vision_config
            .person_detection_enabled
        ):
            analysis[
                "persons"
            ] = (
                detection_service
                .count_persons(
                    frame
                )
            )

        else:
            analysis[
                "persons"
            ] = 0

        if (
            vision_config
            .object_detection_enabled
        ):
            analysis[
                "detections"
            ] = (
                detection_service
                .objects(
                    frame
                )
            )

        else:
            analysis[
                "detections"
            ] = []

        analysis[
            "ai"
        ] = (
            self._run_ai(
                frame
            )
        )

        return analysis

    def _run_ai(
        self,
        frame: Any,
    ):

        if not (
            vision_config
            .ai_enabled
        ):
            return {
                "enabled": False,
                "success": True,
                "results": {},
                "failed_models": [],
            }

        models = list(
            vision_config.ai_models
        )

        if not models:
            return {
                "enabled": True,
                "success": True,
                "results": {},
                "failed_models": [],
            }

        result = (
            ai_service
            .infer_selected(
                model_names=models,
                frame=frame,
                fail_safe=(
                    vision_config
                    .ai_fail_safe
                ),
            )
        )

        result[
            "enabled"
        ] = True

        return result

    def process(
        self,
        camera_id: str | None,
        frame: Any,
    ):

        analysis = (
            self.analyze_frame(
                camera_id,
                frame,
            )
        )

        events = (
            vision_event_service
            .process(
                camera_id,
                analysis,
            )
        )

        decisions = (
            decision_service
            .evaluate(
                analysis
            )
        )

        action_requests = (
            decision_service
            .evaluate_actions(
                analysis
            )
        )

        action_results = (
            vision_event_actions
            .execute_decisions(
                action_requests
            )
        )

        return {
            "camera_id": (
                camera_id
            ),
            "analysis": (
                analysis
            ),
            "events": (
                events
            ),
            "decisions": [
                rule.to_dict()
                for rule
                in decisions
            ],
            "actions": (
                action_requests
            ),
            "action_results": (
                action_results
            ),
        }

    def execute_flow(
        self,
        flow_name: str,
        context: dict,
    ):

        return (
            automation_flow_executor
            .execute(
                flow_name,
                context,
            )
        )


vision_pipeline = VisionPipeline()
