from app.modules.simulator.programming.simulator.board_sdk.pin_bank import (
    PinBank,
)

from app.modules.simulator.programming.simulator.board_sdk.peripheral_bank import (
    PeripheralBank,
)


class BoardDescription:

    def __init__(self):

        self.pins = PinBank()

        self.peripherals = PeripheralBank()

        self.properties = {}
