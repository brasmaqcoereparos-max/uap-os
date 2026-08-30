"""
Template universal para criação de novas placas UAP.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)

from app.modules.simulator.programming.simulator.board_sdk.pin_bank import (
    PinBank,
)

from app.modules.simulator.programming.simulator.board_sdk.peripheral_bank import (
    PeripheralBank,
)


class BoardTemplate(BoardBase):

    name = "New Board"

    manufacturer = "Manufacturer"

    cpu = "CPU"

    frequency = 0

    flash_size = 0

    ram_size = 0

    gpio_count = 0

    pwm_count = 0

    adc_count = 0

    architecture = ""
    voltage = 0.0

    def __init__(self):
        self.pins = PinBank()

        self.peripherals = (
            PeripheralBank()
        )

        self.properties = {}
        self.metadata = {}

        self.initialized = False
        self.enabled = True

    def initialize(self):
        if not self.enabled:
            return False

        self.peripherals.initialize_all()

        self.initialized = True

        return True

    def shutdown(self):
        self.peripherals.shutdown_all()

        self.initialized = False

        return True

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

    def add_pin(
        self,
        pin,
    ):
        result = self.pins.add(
            pin
        )

        self._update_counts()

        return result

    def remove_pin(
        self,
        number,
    ):
        result = self.pins.remove(
            number
        )

        self._update_counts()

        return result

    def add_peripheral(
        self,
        peripheral,
    ):
        return self.peripherals.add(
            peripheral
        )

    def get_pin(
        self,
        number,
    ):
        return self.pins.get(
            number
        )

    def set_property(
        self,
        name,
        value,
    ):
        self.properties[
            str(name)
        ] = value

        return value

    def get_property(
        self,
        name,
        default=None,
    ):
        return self.properties.get(
            str(name),
            default,
        )

    def _update_counts(self):
        self.gpio_count = (
            self.pins.count()
        )

        self.pwm_count = len(
            self.pins.by_capability(
                "pwm"
            )
        )

        self.adc_count = len(
            self.pins.by_capability(
                "adc"
            )
        )

    def to_dict(self):
        self._update_counts()

        return {
            "name": self.name,
            "manufacturer": (
                self.manufacturer
            ),
            "cpu": self.cpu,
            "architecture": (
                self.architecture
            ),
            "frequency": (
                self.frequency
            ),
            "flash_size": (
                self.flash_size
            ),
            "ram_size": (
                self.ram_size
            ),
            "gpio_count": (
                self.gpio_count
            ),
            "pwm_count": (
                self.pwm_count
            ),
            "adc_count": (
                self.adc_count
            ),
            "voltage": (
                self.voltage
            ),
            "initialized": (
                self.initialized
            ),
            "enabled": (
                self.enabled
            ),
            "pins": (
                self.pins.to_dict()
            ),
            "peripherals": (
                self.peripherals.to_dict()
            ),
            "properties": dict(
                self.properties
            ),
            "metadata": dict(
                self.metadata
            ),
    }
