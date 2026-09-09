from app.modules.uhal.board_info import (
    BoardInfo,
)


def test_board_info_exposes_capabilities_and_serialization():

    board = BoardInfo(
        "ESP32",
        "Espressif",
    )

    board.version = "1.0"

    board.capabilities.gpio = 40

    board.capabilities.wifi = True

    assert (
        board.supports(
            "gpio"
        )
        is True
    )

    assert (
        board.supports(
            "wifi"
        )
        is True
    )

    assert (
        board.supports(
            "camera"
        )
        is False
    )

    data = board.to_dict()

    assert (
        data["name"]
        == "ESP32"
    )

    assert (
        data["manufacturer"]
        == "Espressif"
    )

    assert (
        data["version"]
        == "1.0"
    )

    assert (
        data[
            "capabilities"
        ][
            "gpio"
        ]
        == 40
  )
