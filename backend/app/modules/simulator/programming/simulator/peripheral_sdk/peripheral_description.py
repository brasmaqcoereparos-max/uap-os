"""
Descrição serializável de periféricos UAP.
"""


class PeripheralDescription:

    def __init__(
        self,
        name="",
        manufacturer="",
        category="",
        version="1.0",
        description="",
        icon="",
        properties=None,
        interfaces=None,
        pins=None,
        metadata=None,
    ):
        self.name = str(name)

        self.manufacturer = str(
            manufacturer
        )

        self.category = str(
            category
        )

        self.version = str(
            version
        )

        self.description = str(
            description
        )

        self.icon = str(icon)

        self.properties = dict(
            properties or {}
        )

        self.interfaces = list(
            interfaces or []
        )

        self.pins = list(
            pins or []
        )

        self.metadata = dict(
            metadata or {}
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

    def add_interface(
        self,
        interface,
    ):
        if interface not in (
            self.interfaces
        ):
            self.interfaces.append(
                interface
            )

        return interface

    def add_pin(
        self,
        pin,
    ):
        if pin not in self.pins:
            self.pins.append(pin)

        return pin

    def validate(self):
        errors = []

        if not self.name.strip():
            errors.append(
                "name_required"
            )

        if not (
            self.category.strip()
        ):
            errors.append(
                "category_required"
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
            "category": (
                self.category
            ),
            "version": (
                self.version
            ),
            "description": (
                self.description
            ),
            "icon": self.icon,
            "properties": dict(
                self.properties
            ),
            "interfaces": list(
                self.interfaces
            ),
            "pins": list(
                self.pins
            ),
            "metadata": dict(
                self.metadata
            ),
        }

    @classmethod
    def from_dict(
        cls,
        data,
    ):
        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "data deve ser um dicionário."
            )

        return cls(
            name=data.get(
                "name",
                "",
            ),
            manufacturer=data.get(
                "manufacturer",
                "",
            ),
            category=data.get(
                "category",
                "",
            ),
            version=data.get(
                "version",
                "1.0",
            ),
            description=data.get(
                "description",
                "",
            ),
            icon=data.get(
                "icon",
                "",
            ),
            properties=data.get(
                "properties",
                {},
            ),
            interfaces=data.get(
                "interfaces",
                [],
            ),
            pins=data.get(
                "pins",
                [],
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
    )
