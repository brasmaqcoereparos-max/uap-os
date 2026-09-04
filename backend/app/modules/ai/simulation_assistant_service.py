from app.modules.ai.simulation_assistant import (
    ai_simulation_assistant,
)


class AISimulationAssistantService:

    def propose(
        self,
        name: str,
        description: str = "",
        devices: list[dict] | None = None,
        inputs: list[dict] | None = None,
        expected_outputs: (
            list[dict] | None
        ) = None,
    ):
        scenario = (
            ai_simulation_assistant
            .create_scenario(
                name=name,
                description=description,
                devices=devices,
                inputs=inputs,
                expected_outputs=(
                    expected_outputs
                ),
            )
        )

        return {
            "scenario": (
                scenario.to_dict()
            ),
            "target": "simulator",
            "direct_hardware": False,
            "requires_review": False,
        }


ai_simulation_assistant_service = (
    AISimulationAssistantService()
)
