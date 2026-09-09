from app.modules.uhal.drivers.esp8266 import (
    ESP8266Driver,
)

from app.modules.uhal.drivers.raspberry_pico import (
    RaspberryPicoDriver,
)

from app.modules.uhal.drivers.stm32 import (
    STM32Driver,
)

from app.modules.uhal.drivers.arduino_nano import (
    ArduinoNanoDriver,
)

from app.modules.uhal.drivers.arduino_mega import (
    ArduinoMegaDriver,
)

from app.modules.uhal.drivers.teensy import (
    TeensyDriver,
)

from app.modules.uhal.drivers.beaglebone import (
    BeagleBoneDriver,
)


def test_extended_board_profiles():

    cases = [
        (
            ESP8266Driver,
            "ESP8266",
            17,
            17,
            1,
        ),
        (
            RaspberryPicoDriver,
            "Raspberry Pi Pico",
            30,
            30,
            4,
        ),
        (
            STM32Driver,
            "STM32",
            80,
            80,
            24,
        ),
        (
            ArduinoNanoDriver,
            "Arduino Nano",
            22,
            6,
            8,
        ),
        (
            ArduinoMegaDriver,
            "Arduino Mega",
            70,
            12,
            16,
        ),
        (
            TeensyDriver,
            "Teensy",
            40,
            40,
            18,
        ),
        (
            BeagleBoneDriver,
            "BeagleBone Black",
            65,
            65,
            7,
        ),
    ]

    for (
        driver_class,
        expected_name,
        expected_gpio,
        expected_pwm,
        expected_adc,
    ) in cases:

        driver = (
            driver_class()
        )

        capabilities = (
            driver
            .board
            .capabilities
        )

        assert (
            driver.board.name
            == expected_name
        )

        assert (
            capabilities.gpio
            == expected_gpio
        )

        assert (
            capabilities.pwm
            == expected_pwm
        )

        assert (
            capabilities.adc
            == expected_adc
      )
