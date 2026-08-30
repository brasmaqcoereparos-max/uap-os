"""
Periférico associado a uma placa no UAP.
"""


class Peripheral:

    def __init__(
        self,
        name,
        peripheral_type,
        interface=None,
        pins=None,
        properties=None,
        metadata=None,
    ):
        self.name = str(name)

        self.type = str(
            peripheral_type
        )

        self.peripheral_type = (
            self.type
        )

        self.interface = interface

        self.pins = list(
            pins or []
        )

        self.properties = dict(
            properties or {}
        )

        self.metadata = dict(
            metadata or {}
        )

        self.enabled = True
        self.initialized = False

    def initialize(self):
        if not self.enabled:
            return False

        self.initialized = True

        return True

    def shutdown(self):
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
        if pin not in self.pins:
            self.pins.append(
                pin
            )

        return pin

    def remove_pin(
        self,
        pin,
    ):
        if pin in self.pins:
            self.pins.remove(
                pin
            )

            return True

        return False

    def set_interface(
        self,
        interface,
    ):
        self.interface = interface

        return interface

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

    def reset(self):
        self.initialized = False

        return True

    def to_dict(self):
        interface = (
            getattr(
                self.interface,
                "name",
                self.interface,
            )
            if self.interface
            is not None
            else None
        )

        return {
            "name": self.name,
            "type": self.type,
            "interface": (
                interface
            ),
            "pins": [
                getattr(
                    pin,
                    "number",
                    pin,
                )
                for pin
                in self.pins
            ],
            "properties": dict(
                self.properties
            ),
            "metadata": dict(
                self.metadata
            ),
            "enabled": (
                self.enabled
            ),
            "initialized": (
                self.initialized
            ),
            }
