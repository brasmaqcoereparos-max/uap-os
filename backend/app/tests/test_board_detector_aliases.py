from app.modules.uhal.board_detector import (
    BoardDetector,
)


def test_board_detector_normalizes_supported_aliases():

    detector = BoardDetector()

    assert (
        detector.detect(
            "uno"
        )
        == "arduino_uno"
    )

    assert (
        detector.detect(
            "ESP32-C3"
        )
        == "esp32_c3"
    )

    assert (
        detector.detect(
            "ESP32 S3"
        )
        == "esp32_s3"
    )

    assert (
        detector.detect(
            "Raspberry Pi"
        )
        == "raspberry_pi"
    )

    assert (
        detector.detect(
            "Pico"
        )
        == "raspberry_pico"
    )

    assert (
        detector.detect(
            "BeagleBone Black"
        )
        == "beaglebone"
    )
