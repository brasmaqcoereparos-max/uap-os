"""
ESP32 virtual utilizado pelo SimulatorService.
"""

from app.modules.simulator.boards.virtual_board import (
    VirtualBoard,
)


class ESP32Board(VirtualBoard):

    BOARD_TYPE = "ESP32"

    MANUFACTURER = "Espressif"

    CPU = "Xtensa LX6"

    FREQUENCY_HZ = 240_000_000

    FLASH_SIZE = 4_194_304

    RAM_SIZE = 520_192

    INPUT_ONLY_PINS = (
        34,
        35,
        36,
        39,
    )

    DAC_PINS = (
        25,
        26,
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
            digital_pins=40,
            analog_pins=20,
            pwm_pins=range(
                0,
                16,
            ),
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
                "wifi": True,
                "bluetooth": True,
                "ble": True,
                "adc_resolution_bits": 12,
                "dac_channels": 2,
                "touch_channels": 10,
                "uart": 3,
                "spi": 4,
                "i2c": 2,
                "logic_voltage": 3.3,
            },
        )

    def digital_write(
        self,
        pin: int,
        value: int,
    ):
        pin = int(pin)

        if pin in (
            self.INPUT_ONLY_PINS
        ):
            raise ValueError(
                f"GPIO {pin} é somente entrada."
            )

        return super().digital_write(
            pin,
            value,
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
            "input_only_pins": list(
                self.INPUT_ONLY_PINS
            ),
            "dac_pins": list(
                self.DAC_PINS
            ),
            "default_i2c": {
                "sda": 21,
                "scl": 22,
            },
            "default_spi": {
                "mosi": 23,
                "miso": 19,
                "sck": 18,
                "ss": 5,
            },
            "default_uart": {
                "rx": 3,
                "tx": 1,
            },
        })

        return data
