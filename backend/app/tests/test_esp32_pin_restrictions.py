import pytest

from app.modules.simulator.programming.simulator.boards.esp32 import (
    ESP32Board,
)


def test_esp32_input_only_pins_reject_output():
    board = ESP32Board()

    with pytest.raises(
        ValueError
    ):
        board.digital_write(
            34,
            1,
        )

    assert (
        board.digital_write(
            18,
            1,
        )
        == 1
    )

    assert (
        board.digital_read(
            18
        )
        == 1
    )
