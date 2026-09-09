from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


def test_builtin_drivers_are_registered():

    hardware_registry.clear()

    try:

        drivers = (
            register_builtin_drivers()
        )

        expected = {
            "simulator",
            "esp32",
            "esp32_c3",
            "esp32_s3",
            "esp8266",
            "arduino_uno",
            "arduino_nano",
            "arduino_mega",
            "raspberry_pi",
            "raspberry_pico",
            "stm32",
            "teensy",
            "beaglebone",
        }

        assert expected.issubset(
            set(
                drivers.keys()
            )
        )

        esp8266 = (
            hardware_registry.get(
                "esp8266"
            )
        )

        assert (
            esp8266
            .board
            .capabilities
            .wifi
            is True
        )

        beaglebone = (
            hardware_registry.get(
                "beaglebone"
            )
        )

        assert (
            beaglebone
            .board
            .capabilities
            .ethernet
            is True
        )

        teensy = (
            hardware_registry.get(
                "teensy"
            )
        )

        assert (
            teensy
            .board
            .capabilities
            .can
            is True
        )

    finally:

        hardware_registry.clear()
