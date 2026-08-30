"""
Classe base de periféricos do UAP Peripheral SDK.
"""

import uuid


class PeripheralBase:

    name = "Peripheral"
    manufacturer = ""
    category = ""
    version = "1.0"

    def __init__(
        self,
        peripheral_id=None,
        name=None,
        manufacturer=None,
        category=None,
        version=None,
        metadata=None,
    ):
        self.id = (
            str(peripheral_id)
            if peripheral_id
            is not None
            else str(uuid.uuid4())
        )

        if name is not None:
            self.name = str(name)

        if manufacturer is not None:
            self.manufacturer = str(
                manufacturer
            )

        if category is not None:
            self.category = str(
                category
            )

        if version is not None:
            self.version = str(
                version
            )

        self.metadata = dict(
            metadata or {}
        )

        self.properties = {}

        self.interfaces = {}
        self.pins = {}

        self.initialized = False
        self.enabled = True

        self.update_count = 0
        self.last_error = None

    def initialize(self):
        self.initialized = True
        self.last_error = None

        return True

    def update(self):
        if not self.initialized:
            return None

        if not self.enabled:
            return None

        self.update_count += 1

        return {
            "update_count": (
                self.update_count
            )
        }

    def shutdown(self):
        self.initialized = False

        return True

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

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

    def add_interface(
        self,
        interface,
        name=None,
    ):
        key = str(
            name
            or getattr(
                interface,
                "name",
                type(
                    interface
                ).__name__,
            )
        )

        self.interfaces[
            key
        ] = interface

        return interface

    def remove_interface(
        self,
        name,
    ):
        return self.interfaces.pop(
            str(name),
            None,
        )

    def get_interface(
        self,
        name,
    ):
        return self.interfaces.get(
            str(name)
        )

    def add_pin(
        self,
        name,
        pin=None,
    ):
        key = str(name)

        self.pins[key] = (
            pin
            if pin is not None
            else {
                "name": key
            }
        )

        return self.pins[key]

    def remove_pin(
        self,
        name,
    ):
        return self.pins.pop(
            str(name),
            None,
        )

    def get_pin(
        self,
        name,
    ):
        return self.pins.get(
            str(name)
        )

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "manufacturer": (
                self.manufacturer
            ),
            "category": (
                self.category
            ),
            "version": (
                self.version
            ),
            "initialized": (
                self.initialized
            ),
            "enabled": (
                self.enabled
            ),
            "update_count": (
                self.update_count
            ),
            "last_error": (
                self.last_error
            ),
        }

    def reset(self):
        self.properties.clear()

        self.update_count = 0
        self.last_error = None

        return True

    def to_dict(self):
        return {
            **self.status(),
            "properties": dict(
                self.properties
            ),
            "interfaces": list(
                self.interfaces.keys()
            ),
            "pins": list(
                self.pins.keys()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
