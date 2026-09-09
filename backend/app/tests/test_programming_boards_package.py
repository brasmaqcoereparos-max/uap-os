from app.modules.simulator.programming.simulator.boards import (
    ArduinoUNO,
    ESP32Board,
    RaspberryPiBoard,
    VirtualBoard,
)


def test_programming_boards_package_exports_local_advanced_contract():
    board = VirtualBoard(
        "v1",
        "Virtual",
        "virtual",
        4,
        2,
        pwm_pins=[
            1,
        ],
        metadata={
            "x": 1,
        },
        capabilities={
            "gpio": True,
        },
    )

    assert (
        board.capabilities()[
            "gpio"
        ]
        is True
    )

    assert isinstance(
        ArduinoUNO(),
        VirtualBoard,
    )

    assert isinstance(
        ESP32Board(),
        VirtualBoard,
    )

    assert isinstance(
        RaspberryPiBoard(),
        VirtualBoard,
  )
