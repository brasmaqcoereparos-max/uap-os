"""
Representação universal de um pino de placa no UAP.
"""


class Pin:

    VALID_DIRECTIONS = {
        "input",
        "output",
        "bidirectional",
    }

    def __init__(
        self,
        number,
        name,
        modes=None,
        direction="bidirectional",
        capabilities=None,
        metadata=None,
    ):
        self.number = number
        self.name = str(name)

        self.modes = list(
            modes or []
        )

        direction = str(
            direction
        ).lower()

        if (
            direction
            not in self.VALID_DIRECTIONS
        ):
            raise ValueError(
                "direction deve ser input, "
                "output ou bidirectional."
            )

        self.direction = direction

        self.capabilities = set(
            capabilities or self.modes
        )

        self.metadata = dict(
            metadata or {}
        )

        self.value = 0
        self.mode = (
            self.modes[0]
            if self.modes
            else None
        )

        self.enabled = True
        self.reserved = False
        self.owner = None

    def supports(
        self,
        capability,
    ):
        capability = str(
            capability
        ).lower()

        return any(
            str(item).lower()
            == capability
            for item
            in self.capabilities
        )

    def add_capability(
        self,
        capability,
    ):
        self.capabilities.add(
            str(capability)
        )

        return capability

    def remove_capability(
        self,
        capability,
    ):
        self.capabilities.discard(
            str(capability)
        )

        return True

    def set_mode(
        self,
        mode,
    ):
        mode = str(mode)

        if (
            self.modes
            and mode not in self.modes
        ):
            raise ValueError(
                f"Modo '{mode}' não suportado "
                f"pelo pino {self.name}."
            )

        self.mode = mode

        return self.mode

    def write(
        self,
        value,
    ):
        if not self.enabled:
            return False

        if self.direction == "input":
            return False

        if self.reserved:
            return False

        self.value = value

        return True

    def read(self):
        if not self.enabled:
            return None

        return self.value

    def set_value(
        self,
        value,
    ):
        self.value = value

        return self.value

    def reserve(
        self,
        owner=None,
    ):
        if self.reserved:
            return False

        self.reserved = True
        self.owner = owner

        return True

    def release(
        self,
        owner=None,
    ):
        if not self.reserved:
            return True

        if (
            owner is not None
            and self.owner is not None
            and owner != self.owner
        ):
            return False

        self.reserved = False
        self.owner = None

        return True

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

    def reset(self):
        self.value = 0

        self.mode = (
            self.modes[0]
            if self.modes
            else None
        )

        self.reserved = False
        self.owner = None

        return True

    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name,
            "modes": list(
                self.modes
            ),
            "mode": self.mode,
            "direction": (
                self.direction
            ),
            "capabilities": sorted(
                str(item)
                for item
                in self.capabilities
            ),
            "value": self.value,
            "enabled": (
                self.enabled
            ),
            "reserved": (
                self.reserved
            ),
            "owner": self.owner,
            "metadata": dict(
                self.metadata
            ),
            }
