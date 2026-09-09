from app.modules.vision.health import (
    vision_health,
)


def test_vision_health():
    result = (
        vision_health
        .check()
    )

    assert (
        result["service"]
        == "vision"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )
