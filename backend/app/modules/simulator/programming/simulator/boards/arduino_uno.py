"""
Modelo virtual Arduino Uno.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ArduinoUNO(BoardBase):

    name = "Arduino Uno"

    manufacturer = "Arduino"

    gpio_count = 20
    pwm_count = 6
    adc_count = 6

    flash_size = 32768
    ram_size = 2048

    cpu = "ATmega328P"

    frequency = 16000000

    architecture = "AVR"

    voltage = 5.0

    digital_pins = tuple(
        range(
            0,
            14,
        )
    )

    analog_pins = (
        "A0",
        "A1",
        "A2",
        "A3",
        "A4",
        "A5",
    )

    pwm_pins = (
        3,
        5,
        6,
        9,
        10,
        11,
    )

    uart_pins = {
        "rx": 0,
        "tx": 1,
    }

    i2c_pins = {
        "sda": "A4",
        "scl": "A5",
    }

    spi_pins = {
        "ss": 10,
        "mosi": 11,
        "miso": 12,
        "sck": 13,
    }

    def capabilities(self):
        data = super().capabilities()

        data.update({
            "digital_pins": list(
                self.digital_pins
            ),
            "analog_pins": list(
                self.analog_pins
            ),
            "pwm_pins": list(
                self.pwm_pins
            ),
            "uart": dict(
                self.uart_pins
            ),
            "i2c": dict(
                self.i2c_pins
            ),
            "spi": dict(
                self.spi_pins
            ),
        })

        return data
