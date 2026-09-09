from app.modules.uhal.board_detector import (
    BoardDetector,
)


def test_board_detector_uses_environment_override(
    monkeypatch,
):

    detector = BoardDetector()

    monkeypatch.setenv(
        "UAP_BOARD",
        "Arduino Mega",
    )

    assert (
        detector.detect()
        == "arduino_mega"
    )

    monkeypatch.delenv(
        "UAP_BOARD"
    )

    monkeypatch.setenv(
        "UAP_BOARD_TYPE",
        "ESP8266",
    )

    assert (
        detector.detect()
        == "esp8266"
    )
