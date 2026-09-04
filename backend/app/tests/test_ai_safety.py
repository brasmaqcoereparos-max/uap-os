from app.modules.ai.safety_service import (
    ai_safety_service,
)


def test_ai_safe_proposal():
    result = (
        ai_safety_service
        .inspect(
            {
                "target": "ui",
                "action": "navigate",
            }
        )
    )

    assert (
        result.status
        in {
            "approved",
            "review_required",
        }
    )


def test_ai_blocks_direct_gpio():
    result = (
        ai_safety_service
        .inspect(
            {
                "gpio": {
                    "pin": 2,
                    "value": 1,
                }
            }
        )
    )

    assert (
        result.status
        == "blocked"
    )

    assert (
        result.accepted
        is False
    )


def test_ai_runtime_requires_review():
    result = (
        ai_safety_service
        .inspect(
            {
                "runtime": {
                    "action": "start",
                }
            }
        )
    )

    assert (
        result.status
        == "review_required"
    )
