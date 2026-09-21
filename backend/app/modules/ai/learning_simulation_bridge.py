from __future__ import annotations

from app.modules.ai.education_assistant_service import (
    ai_education_assistant_service,
)
from app.modules.ai.simulation_assistant_service import (
    ai_simulation_assistant_service,
)


class AILearningSimulationBridge:

    def prepare_lesson(
        self,
        topic: str,
        level: str = "beginner",
        scenario_name: (
            str | None
        ) = None,
        devices: (
            list[dict] | None
        ) = None,
        inputs: (
            list[dict] | None
        ) = None,
        expected_outputs: (
            list[dict] | None
        ) = None,
    ):
        lesson = (
            ai_education_assistant_service
            .explain(
                topic=topic,
                level=level,
                include_examples=True,
                include_exercises=True,
            )
        )

        simulation = (
            ai_simulation_assistant_service
            .propose(
                name=(
                    scenario_name
                    or f"{topic} Simulation"
                ),
                description=(
                    "Didactic simulation "
                    f"for {topic}"
                ),
                devices=(
                    devices
                ),
                inputs=(
                    inputs
                ),
                expected_outputs=(
                    expected_outputs
                ),
            )
        )

        return {
            "lesson": lesson,
            "simulation": simulation,
            "workflow": [
                "learn",
                "practice",
                "simulate",
                "evaluate",
                "review",
            ],
            "simulation_only": True,
            "direct_hardware": False,
            "requires_review": False,
        }

    def propose_lab(
        self,
        topic: str,
        level: str = "beginner",
    ):
        education = (
            ai_education_assistant_service
            .propose_lab(
                topic=topic,
                level=level,
            )
        )

        simulation = (
            ai_simulation_assistant_service
            .propose(
                name=education[
                    "name"
                ],
                description=education[
                    "description"
                ],
                devices=[],
                inputs=[],
                expected_outputs=[],
            )
        )

        return {
            "education": education,
            "simulation": simulation,
            "simulation_only": True,
            "registered": False,
            "requires_review": True,
            "direct_hardware": False,
        }


ai_learning_simulation_bridge = (
    AILearningSimulationBridge()
    )
