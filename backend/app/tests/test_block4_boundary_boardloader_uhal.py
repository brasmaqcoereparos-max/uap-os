from app.modules.simulator.programming.simulator.boards.board_loader import (
    BoardLoader,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


def test_simulator_board_and_uhal_driver_resolve_same_family():

    hardware_registry.clear()

    try:

        simulated = (
            BoardLoader.create(
                "esp32"
            )
        )

        drivers = (
            register_builtin_drivers()
        )

        driver = (
            drivers[
                "esp32"
            ]
        )

        assert (
            simulated.name
            == "ESP32 DevKit"
        )

        assert (
            simulated.manufacturer
            == "Espressif"
        )

        assert (
            simulated
            .capabilities()[
                "wifi"
            ]
            is True
        )

        assert (
            driver.board.name
            == "ESP32"
        )

        assert (
            driver.board.manufacturer
            == "Espressif"
        )

        assert (
            driver.board.supports(
                "gpio"
            )
            is True
        )

        assert (
            driver.board.supports(
                "pwm"
            )
            is True
        )

        assert (
            driver.board.supports(
                "wifi"
            )
            is True
        )

    finally:

        hardware_registry.clear()
