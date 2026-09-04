from app.modules.ai.education_assistant_service import (
    ai_education_assistant_service,
)
from app.modules.ai.simulation_assistant_service import (
    ai_simulation_assistant_service,
)


def test_ai_education_assistant():
    result = (
        ai_education_assistant_service
        .explain(
            topic="Sensor digital",
            level="beginner",
        )
    )

    assert "response" in result

    assert (
        result["target"]
        == "education"
    )


def test_ai_simulation_assistant():
    result = (
        ai_simulation_assistant_service
        .propose(
            name="Teste simulação",
            devices=[
                {
                    "id": "sensor-1",
                }
            ],
        )
    )

    assert "scenario" in result

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )
