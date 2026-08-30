"""
Descrição universal de uma placa UAP.
"""

from app.modules.simulator.programming.simulator.board_sdk.pin_bank import (
    PinBank,
)

from app.modules.simulator.programming.simulator.board_sdk.peripheral_bank import (
    PeripheralBank,
)


class BoardDescription:

    def __init__(
        self,
        name="",
        manufacturer="",
        cpu="",
        frequency=0,
        flash_size=0,
        ram_size=0,
        properties=None,
        metadata=None,
    ):
        self.name = str(name)

        self.manufacturer = str(
            manufacturer
        )

        self.cpu = str(cpu)

        self.frequency = int(
            frequency or 0
        )

        self.flash_size = int(
            flash_size or 0
        )

        self.ram_size = int(
            ram_size or 0
        )

        self.pins = PinBank()

        self.peripherals = (
            PeripheralBank()
        )

        self.properties = dict(
            properties or {}
        )

        self.metadata = dict(
            metadata or {}
        )

    @property
    def gpio_count(self):
        return len(
            self.pins.all()
        )

    @property
    def pwm_count(self):
        return len(
            self.pins.by_capability(
                "pwm"
            )
        )

    @property
    def adc_count(self):
        return len(
            self.pins.by_capability(
                "adc"
            )
        )

    def add_pin(
        self,
        pin,
    ):
        return self.pins.add(
            pin
        )

    def add_peripheral(
        self,
        peripheral,
    ):
        return self.peripherals.add(
            peripheral
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

    def validate_basic(self):
        errors = []

        if not self.name.strip():
            errors.append(
                "name_required"
            )

        if not (
            self.manufacturer.strip()
        ):
            errors.append(
                "manufacturer_required"
            )

        if not self.cpu.strip():
            errors.append(
                "cpu_required"
            )

        return {
            "valid": (
                len(errors) == 0
            ),
            "errors": errors,
        }

    def to_dict(self):
        return {
            "name": self.name,
            "manufacturer": (
                self.manufacturer
            ),
            "cpu": self.cpu,
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
