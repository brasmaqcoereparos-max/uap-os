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
                devices=devices,
            )
        )

        return {
            "lesson": lesson,
            "simulation": simulation,
            "workflow": [
                "learn",
                "simulate",
                "validate",
                "build",
            ],
        }


ai_learning_simulation_bridge = (
    AILearningSimulationBridge()
      )
