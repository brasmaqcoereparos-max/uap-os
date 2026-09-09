from app.modules.simulator.programming.simulator.boards.board_loader import (
    BoardLoader,
)


def test_board_loader_creates_default_and_alias_boards():
    uno = BoardLoader.create(
        "uno"
    )

    esp = BoardLoader.create(
        "esp32"
    )

    pico = BoardLoader.create(
        "pico"
    )

    assert (
        uno.id
        == "arduino_uno"
    )

    assert (
        uno.name
        == "Arduino UNO"
    )

    assert (
        esp.name
        == "ESP32 DevKit"
    )

    assert (
        pico.name
        == "Raspberry Pi Pico"
    )
