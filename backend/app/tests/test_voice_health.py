from app.modules.voice.health import (
    voice_health,
)


def test_voice_health():
    result = (
        voice_health
        .check()
    )

    assert (
        result["service"]
        == "voice"
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["available"]
        is True
    )
