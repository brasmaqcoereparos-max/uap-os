"""
Arduino UNO virtual utilizado pelo SimulatorService.
"""

from app.modules.simulator.boards.virtual_board import (
    VirtualBoard,
)


class ArduinoUNO(VirtualBoard):

    BOARD_TYPE = "Arduino UNO"

    MANUFACTURER = "Arduino"

    CPU = "ATmega328P"

    FREQUENCY_HZ = 16_000_000

    FLASH_SIZE = 32_768

    RAM_SIZE = 2_048

    PWM_PINS = (
        3,
        5,
        6,
        9,
        10,
        11,
    )

    def __init__(
        self,
        board_id: str,
        name: str,
    ):
        super().__init__(
            board_id=board_id,
            name=name,
            board_type=self.BOARD_TYPE,
            digital_pins=14,
            analog_pins=6,
            pwm_pins=self.PWM_PINS,
            metadata={
                "manufacturer": (
                    self.MANUFACTURER
                ),
                "cpu": self.CPU,
                "frequency_hz": (
                    self.FREQUENCY_HZ
                ),
                "flash_size": (
                    self.FLASH_SIZE
                ),
                "ram_size": (
                    self.RAM_SIZE
                ),
            },
            capabilities={
                "uart": 1,
                "spi": 1,
                "i2c": 1,
                "adc_resolution_bits": 10,
                "logic_voltage": 5.0,
            },
        )

    def capabilities(self):
        data = super().capabilities()

        data.update({
            "manufacturer": (
                self.MANUFACTURER
            ),
            "cpu": self.CPU,
            "frequency_hz": (
                self.FREQUENCY_HZ
            ),
            "flash_size": (
                self.FLASH_SIZE
            ),
            "ram_size": (
                self.RAM_SIZE
            ),
            "uart_pins": {
                "rx": 0,
                "tx": 1,
            },
            "i2c_pins": {
                "sda": "A4",
                "scl": "A5",
            },
            "spi_pins": {
                "ss": 10,
                "mosi": 11,
                "miso": 12,
                "sck": 13,
            },
        })

        return data
