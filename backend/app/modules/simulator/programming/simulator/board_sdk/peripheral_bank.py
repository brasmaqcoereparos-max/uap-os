"""
Banco de periféricos associados a uma placa UAP.
"""


class PeripheralBank:

    def __init__(self):
        self.peripherals = []

    def add(
        self,
        peripheral,
        replace=False,
    ):
        if peripheral is None:
            raise ValueError(
                "Periférico não informado."
            )

        name = getattr(
            peripheral,
            "name",
            None,
        )

        if name is None:
            raise TypeError(
                "Periférico precisa possuir "
                "atributo name."
            )

        existing = self.get(
            name
        )

        if existing is not None:
            if not replace:
                return existing

            self.remove(
                name
            )

        self.peripherals.append(
            peripheral
        )

        return peripheral

    def get(
        self,
        name,
    ):
        expected = str(
            name
        ).lower()

        for peripheral in (
            self.peripherals
        ):
            if (
                str(
                    peripheral.name
                ).lower()
                == expected
            ):
                return peripheral

        return None

    def remove(
        self,
        name,
    ):
        peripheral = self.get(
            name
        )

        if peripheral is None:
            return None

        self.peripherals.remove(
            peripheral
        )

        return peripheral

    def exists(
        self,
        name,
    ):
        return (
            self.get(name)
            is not None
        )

    def all(self):
        return self.peripherals.copy()

    def names(self):
        return [
            peripheral.name
            for peripheral
            in self.peripherals
        ]

    def by_type(
        self,
        peripheral_type,
    ):
        expected = str(
            peripheral_type
        ).lower()

        return [
            peripheral
            for peripheral
            in self.peripherals
            if (
                str(
                    getattr(
                        peripheral,
                        "type",
                        "",
                    )
                ).lower()
                == expected
            )
        ]

    def enabled(self):
        return [
            peripheral
            for peripheral
            in self.peripherals
            if getattr(
                peripheral,
                "enabled",
                True,
            )
        ]

    def initialize_all(self):
        result = {}

        for peripheral in (
            self.peripherals
        ):
            method = getattr(
                peripheral,
                "initialize",
                None,
            )

            result[
                peripheral.name
            ] = (
                method()
                if callable(method)
                else None
            )

        return result

    def shutdown_all(self):
        result = {}

        for peripheral in (
            self.peripherals
        ):
            method = getattr(
                peripheral,
                "shutdown",
                None,
            )

            result[
                peripheral.name
            ] = (
                method()
                if callable(method)
                else None
            )

        return result

    def clear(self):
        count = len(
            self.peripherals
        )

        self.peripherals.clear()

        return count

    def count(self):
        return len(
            self.peripherals
        )

    def to_dict(self):
        return [
            (
                peripheral.to_dict()
                if hasattr(
                    peripheral,
                    "to_dict",
                )
                else {
                    "name": getattr(
                        peripheral,
                        "name",
                        str(peripheral),
                    )
                }
            )
            for peripheral
            in self.peripherals
        ]


peripheral_bank = (
    PeripheralBank()
        )
