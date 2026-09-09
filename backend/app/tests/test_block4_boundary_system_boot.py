from app.modules.uhal.hal_manager import (
    hal_manager,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.system_boot import (
    initialize_hardware,
)


def test_system_boot_selects_explicit_board_and_initializes_once():

    hardware_registry.clear()

    hal_manager.unload()

    try:

        driver = (
            initialize_hardware(
                board="esp8266"
            )
        )

        assert (
            driver
            is hardware_registry.get(
                "esp8266"
            )
        )

        assert (
            driver.board.name
            == "ESP8266"
        )

        assert (
            driver.board.supports(
                "wifi"
            )
            is True
        )

        assert (
            driver.initialized
            is True
        )

        assert (
            hal_manager.current_board()
            == "esp8266"
        )

    finally:

        hal_manager.unload()

        hardware_registry.clear()
