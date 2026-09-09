from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


def test_builtin_driver_catalog_is_complete_for_block4():

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

        assert (
            expected.issubset(
                drivers.keys()
            )
        )

        for name in expected:

            driver = (
                hardware_registry.get(
                    name
                )
            )

            assert (
                driver
                is not None
            )

            assert (
                hasattr(
                    driver,
                    "board",
                )
                or
                name
                == "simulator"
            )

    finally:

        hardware_registry.clear()
