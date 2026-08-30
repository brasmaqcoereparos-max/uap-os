"""
Modelo virtual Raspberry Pi Pico.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class RaspberryPiPico(BoardBase):

    name = "Raspberry Pi Pico"

    manufacturer = "Raspberry Pi"

    gpio_count = 30
    pwm_count = 16
    adc_count = 4

    flash_size = 2097152
    ram_size = 270336

    cpu = "RP2040 Dual Core"

    frequency = 133000000

    architecture = "ARM Cortex-M0+"

    voltage = 3.3

    cores = 2

    adc_resolution = 12

    uart_count = 2
    spi_count = 2
    i2c_count = 2

    pwm_slices = 8
    pwm_channels = 16

    pio_blocks = 2
    state_machines = 8

    temperature_sensor = True

    gpio_pins = tuple(
        range(
            0,
            30,
        )
    )

    adc_pins = (
        26,
        27,
        28,
        29,
    )

    default_i2c0 = {
        "sda": 4,
        "scl": 5,
    }

    default_spi0 = {
        "rx": 16,
        "csn": 17,
        "sck": 18,
        "tx": 19,
    }

    default_uart0 = {
        "tx": 0,
        "rx": 1,
    }

    def capabilities(self):
        data = super().capabilities()

        data.update({
            "cores": self.cores,
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
            "pwm_slices": (
                self.pwm_slices
            ),
            "pwm_channels": (
                self.pwm_channels
            ),
            "pio_blocks": (
                self.pio_blocks
            ),
            "state_machines": (
                self.state_machines
            ),
            "temperature_sensor": (
                self.temperature_sensor
            ),
            "gpio_pins": list(
                self.gpio_pins
            ),
            "adc_pins": list(
                self.adc_pins
            ),
            "default_i2c0": dict(
                self.default_i2c0
            ),
            "default_spi0": dict(
                self.default_spi0
            ),
            "default_uart0": dict(
                self.default_uart0
            ),
        })

        return data
