from app.modules.ai.hardware_assistant_service import (
    ai_hardware_assistant_service,
)


def test_ai_hardware_recommendation():
    result = (
        ai_hardware_assistant_service
        .recommend(
            requirements={
                "gpio": 4,
                "wifi": True,
            },
            boards=[
                {
                    "id": "board-1",
                    "name": "Board Test",
                    "capabilities": {
                        "gpio": 20,
                        "wifi": True,
                    },
                }
            ],
        )
    )

    assert (
        result["recommended"]
        is not None
    )

    assert (
        result["recommended"][
            "compatible"
        ]
        is True
    )
