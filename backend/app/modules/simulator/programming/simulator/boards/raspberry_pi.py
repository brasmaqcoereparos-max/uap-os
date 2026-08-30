"""
Raspberry Pi virtual utilizado pelo SimulatorService.

O modelo mantém os 40 pinos já definidos no projeto,
mas registra que o Raspberry Pi não possui ADC nativo.
"""

from app.modules.simulator.boards.virtual_board import (
    VirtualBoard,
)


class RaspberryPiBoard(VirtualBoard):

    BOARD_TYPE = "Raspberry Pi"

    MANUFACTURER = (
        "Raspberry Pi"
    )

    CPU = "ARM"

    LOGIC_VOLTAGE = 3.3

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
            analog_pins=0,
            pwm_pins=(
                12,
                13,
                18,
                19,
            ),
            metadata={
                "manufacturer": (
                    self.MANUFACTURER
                ),
                "cpu": self.CPU,
            },
            capabilities={
                "adc_native": False,
                "uart": True,
                "spi": True,
                "i2c": True,
                "pwm": True,
                "logic_voltage": (
                    self.LOGIC_VOLTAGE
                ),
            },
        )

    def analog_write(
        self,
        pin: int,
        value: float,
    ):
        raise ValueError(
            "Raspberry Pi não possui "
            "saída analógica nativa."
        )

    def capabilities(self):
        data = super().capabilities()

        data.update({
            "manufacturer": (
                self.MANUFACTURER
            ),
            "cpu": self.CPU,
            "physical_header_pins": 40,
            "default_i2c": {
                "sda": 2,
                "scl": 3,
            },
            "default_uart": {
                "tx": 14,
                "rx": 15,
            },
            "default_spi0": {
                "mosi": 10,
                "miso": 9,
                "sck": 11,
                "ce0": 8,
                "ce1": 7,
            },
        })

        return data
