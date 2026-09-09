from app.modules.simulator.programming.simulator.board_sdk.board_registry import (
    BoardRegistry,
)


class ESP32Board:
    name = "ESP32"
    manufacturer = "Espressif"


def test_board_registry_alias_metadata_and_manufacturer():
    registry = BoardRegistry()

    registry.register(
        ESP32Board,
        aliases=[
            "esp",
            "esp32-devkit",
        ],
        metadata={
            "family": "esp32",
            "architecture": "xtensa",
        },
    )

    assert registry.exists(
        "ESP32"
    ) is True

    assert registry.exists(
        "esp"
    ) is True

    assert registry.get(
        "esp"
    ) is ESP32Board

    assert registry.get(
        "esp32-devkit"
    ) is ESP32Board

    metadata = registry.info(
        "ESP32"
    )

    assert metadata[
        "family"
    ] == "esp32"

    assert metadata[
        "architecture"
    ] == "xtensa"

    assert registry.by_manufacturer(
        "espressif"
    ) == [
        ESP32Board
    ]

    assert registry.count() == 1
