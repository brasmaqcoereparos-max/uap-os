"""
Modelo virtual ESP8266.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ESP8266(BoardBase):

    name = "ESP8266"

    manufacturer = "Espressif"

    gpio_count = 17
    pwm_count = 8
    adc_count = 1

    flash_size = 4194304
    ram_size = 81920

    cpu = "Tensilica L106"

    frequency = 80000000

    architecture = "Xtensa"

    voltage = 3.3

    wifi = True
    bluetooth = False

    adc_resolution = 10

    uart_count = 2
    spi_count = 2
    i2c_count = 1

    default_uart = {
        "rx": 3,
        "tx": 1,
    }

    default_spi = {
        "mosi": 13,
        "miso": 12,
        "sck": 14,
        "ss": 15,
    }

    default_i2c = {
        "sda": 4,
        "scl": 5,
    }

    boot_sensitive_pins = (
        0,
        2,
        15,
    )

    def capabilities(self):
        data = super().capabilities()

        data.update({
            "wifi": self.wifi,
            "bluetooth": (
                self.bluetooth
            ),
            "adc_resolution": (
                self.adc_resolution
            ),
            "uart_count": (
                self.uart_count
            ),
            "spi_count": (
                self.spi_count
            ),
            "i2c_count": (
                self.i2c_count
            ),
            "default_uart": dict(
                self.default_uart
            ),
            "default_spi": dict(
                self.default_spi
            ),
            "default_i2c": dict(
                self.default_i2c
            ),
            "boot_sensitive_pins": list(
                self.boot_sensitive_pins
            ),
        })

        return data
