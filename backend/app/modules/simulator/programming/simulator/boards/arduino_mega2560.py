"""
Modelo virtual Arduino Mega 2560.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ArduinoMega2560(BoardBase):

    name = "Arduino Mega 2560"

    manufacturer = "Arduino"

    gpio_count = 70
    pwm_count = 15
    adc_count = 16

    flash_size = 262144
    ram_size = 8192

    cpu = "ATmega2560"

    frequency = 16000000

    architecture = "AVR"

    voltage = 5.0

    digital_pins = tuple(
        range(
            0,
            54,
        )
    )

    analog_pins = tuple(
        f"A{index}"
        for index
        in range(16)
    )

    pwm_pins = (
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        44,
        45,
        46,
    )

    uart_ports = {
        "serial0": {
            "rx": 0,
            "tx": 1,
        },
        "serial1": {
            "rx": 19,
            "tx": 18,
        },
        "serial2": {
            "rx": 17,
            "tx": 16,
        },
        "serial3": {
            "rx": 15,
            "tx": 14,
        },
    }

    i2c_pins = {
        "sda": 20,
        "scl": 21,
    }

    spi_pins = {
        "ss": 53,
        "mosi": 51,
        "miso": 50,
        "sck": 52,
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
            "uart_ports": {
                key: dict(value)
                for key, value
                in self.uart_ports.items()
            },
            "i2c": dict(
                self.i2c_pins
            ),
            "spi": dict(
                self.spi_pins
            ),
        })

        return data
