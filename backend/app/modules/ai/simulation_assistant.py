import uuid

from app.modules.ai.simulation_scenario import (
    AISimulationScenario,
)
from app.modules.ai.simulation_test_case import (
    AISimulationTestCase,
)


class AISimulationAssistant:

    def create_scenario(
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
            AISimulationScenario(
                name=name,
                description=description,
                devices=list(
                    devices or []
                ),
                inputs=list(
                    inputs or []
                ),
                expected_outputs=list(
                    expected_outputs or []
                ),
            )
        )

        scenario.steps.extend(
            [
                {
                    "order": 1,
                    "action": (
                        "initialize_devices"
                    ),
                },
                {
                    "order": 2,
                    "action": (
                        "apply_inputs"
                    ),
                },
                {
                    "order": 3,
                    "action": (
                        "run_simulation"
                    ),
                },
                {
                    "order": 4,
                    "action": (
                        "compare_outputs"
                    ),
                },
            ]
        )

        return scenario

    def create_test_case(
        self,
        name: str,
        input_data: dict,
        expected: dict,
    ):
        return AISimulationTestCase(
            id=str(uuid.uuid4()),
            name=name,
            input_data=dict(
                input_data
            ),
            expected=dict(
                expected
            ),
        )


ai_simulation_assistant = (
    AISimulationAssistant()
      )
