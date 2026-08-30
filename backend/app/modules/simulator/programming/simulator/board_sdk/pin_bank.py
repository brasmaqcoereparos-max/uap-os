"""
Banco de pinos de uma placa UAP.
"""


class PinBank:

    def __init__(self):
        self.pins = {}

    def add(
        self,
        pin,
        replace=True,
    ):
        if pin is None:
            raise ValueError(
                "Pin não informado."
            )

        if not hasattr(
            pin,
            "number",
        ):
            raise TypeError(
                "Objeto informado não possui "
                "atributo number."
            )

        number = pin.number

        if (
            number in self.pins
            and not replace
        ):
            raise ValueError(
                f"Pino já registrado: {number}"
            )

        self.pins[
            number
        ] = pin

        return pin

    def get(
        self,
        number,
    ):
        return self.pins.get(
            number
        )

    def get_by_name(
        self,
        name,
    ):
        expected = str(
            name
        ).lower()

        for pin in (
            self.pins.values()
        ):
            if (
                str(
                    getattr(
                        pin,
                        "name",
                        "",
                    )
                ).lower()
                == expected
            ):
                return pin

        return None

    def remove(
        self,
        number,
    ):
        return self.pins.pop(
            number,
            None,
        )

    def exists(
        self,
        number,
    ):
        return (
            number in self.pins
        )

    def all(self):
        return list(
            self.pins.values()
        )

    def numbers(self):
        return list(
            self.pins.keys()
        )

    def available(self):
        return [
            pin
            for pin
            in self.pins.values()
            if (
                getattr(
                    pin,
                    "enabled",
                    True,
                )
                and not getattr(
                    pin,
                    "reserved",
                    False,
                )
            )
        ]

    def reserved(self):
        return [
            pin
            for pin
            in self.pins.values()
            if getattr(
                pin,
                "reserved",
                False,
            )
        ]

    def by_mode(
        self,
        mode,
    ):
        expected = str(
            mode
        ).lower()

        return [
            pin
            for pin
            in self.pins.values()
            if (
                expected
                in [
                    str(item).lower()
                    for item
                    in getattr(
                        pin,
                        "modes",
                        [],
                    )
                ]
            )
        ]

    def by_capability(
        self,
        capability,
    ):
        result = []

        for pin in (
            self.pins.values()
        ):
            supports = getattr(
                pin,
                "supports",
                None,
            )

            if (
                callable(supports)
                and supports(
                    capability
                )
            ):
                result.append(pin)

        return result

    def reserve(
        self,
        number,
        owner=None,
    ):
        pin = self.get(
            number
        )

        if pin is None:
            return False

        method = getattr(
            pin,
            "reserve",
            None,
        )

        if callable(method):
            return method(
                owner
            )

        return False

    def release(
        self,
        number,
        owner=None,
    ):
        pin = self.get(
            number
        )

        if pin is None:
            return False

        method = getattr(
            pin,
            "release",
            None,
        )

        if callable(method):
            return method(
                owner
            )

        return False

    def clear(self):
        count = len(
            self.pins
        )

        self.pins.clear()

        return count

    def count(self):
        return len(
            self.pins
        )

    def to_dict(self):
        return {
            str(number): (
                pin.to_dict()
                if hasattr(
                    pin,
                    "to_dict",
                )
                else str(pin)
            )
            for number, pin
            in self.pins.items()
        }


pin_bank = PinBank()
