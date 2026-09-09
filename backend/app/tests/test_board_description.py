from app.modules.simulator.programming.simulator.board_sdk.board_description import (
    BoardDescription,
)

from app.modules.simulator.programming.simulator.board_sdk.pin import (
    Pin,
)


def test_board_description_counts_and_serialization():
    board = BoardDescription(
        name="ESP32",
        manufacturer="Espressif",
        cpu="Xtensa",
        frequency=240000000,
        flash_size=4194304,
        ram_size=520000,
    )

    board.add_pin(
        Pin(
            1,
            "GPIO1",
            capabilities=[
                "gpio",
                "pwm",
            ],
        )
    )

    board.add_pin(
        Pin(
            2,
            "GPIO2",
            capabilities=[
                "gpio",
                "adc",
            ],
        )
    )

    assert board.gpio_count == 2
    assert board.pwm_count == 1
    assert board.adc_count == 1

    validation = (
        board.validate_basic()
    )

    assert validation[
        "valid"
    ] is True

    assert validation[
        "errors"
    ] == []

    data = board.to_dict()

    assert data[
        "name"
    ] == "ESP32"

    assert data[
        "manufacturer"
    ] == "Espressif"

    assert data[
        "cpu"
    ] == "Xtensa"

    assert data[
        "gpio_count"
    ] == 2

    assert data[
        "pwm_count"
    ] == 1

    assert data[
        "adc_count"
    ] == 1
