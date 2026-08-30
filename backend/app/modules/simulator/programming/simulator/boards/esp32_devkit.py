"""
Modelo virtual ESP32 DevKit.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ESP32DevKit(BoardBase):

    name = "ESP32 DevKit"

    manufacturer = "Espressif"

    gpio_count = 39
    pwm_count = 16
    adc_count = 18

    flash_size = 4194304
    ram_size = 520192

    cpu = "Xtensa LX6 Dual Core"

    frequency = 240000000

    architecture = "Xtensa"

    voltage = 3.3

    wifi = True
    bluetooth = True
    ble = True

    dac_count = 2

    touch_count = 10

    uart_count = 3
    spi_count = 4
    i2c_count = 2

    pwm_channels = 16

    adc_resolution = 12

    dac_pins = (
        25,
        26,
    )

    default_i2c = {
        "sda": 21,
        "scl": 22,
    }

    default_spi = {
        "mosi": 23,
        "miso": 19,
        "sck": 18,
        "ss": 5,
    }

    default_uart = {
        "rx": 3,
        "tx": 1,
    }

    input_only_pins = (
        34,
        35,
        36,
        39,
    )

    def capabilities(self):
        data = super().capabilities()

        data.update({
            "wifi": self.wifi,
            "bluetooth": (
                self.bluetooth
            ),
            "ble": self.ble,
            "dac_count": (
                self.dac_count
            ),
            "touch_count": (
                self.touch_count
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
            "pwm_channels": (
                self.pwm_channels
            ),
            "adc_resolution": (
                self.adc_resolution
            ),
            "dac_pins": list(
                self.dac_pins
            ),
            "default_i2c": dict(
                self.default_i2c
            ),
            "default_spi": dict(
                self.default_spi
            ),
            "default_uart": dict(
                self.default_uart
            ),
            "input_only_pins": list(
                self.input_only_pins
            ),
        })

        return data
