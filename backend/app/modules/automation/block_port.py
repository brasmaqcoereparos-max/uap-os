class BlockPort:
    VALID_DIRECTIONS = {
        "input",
        "output",
    }

    def __init__(
        self,
        name,
        port_type="generic",
        direction=None,
        required=False,
        multiple=False,
        description="",
        icon="",
        metadata=None,
    ):
        self.name = str(name)

        self.port_type = str(
            port_type
        )

        self.direction = (
            str(direction).lower()
            if direction
            is not None
            else None
        )

        self.required = bool(
            required
        )

        self.multiple = bool(
            multiple
        )

        self.description = str(
            description
        )

        self.icon = str(icon)

        self.metadata = dict(
            metadata or {}
        )

        if (
            self.direction
            is not None
            and self.direction
            not in self.VALID_DIRECTIONS
        ):
            raise ValueError(
                "Direção de porta "
                f"inválida: {direction}"
            )

    def compatible_with(
        self,
        other,
    ):
        if not isinstance(
            other,
            BlockPort,
        ):
            return False

        if (
            self.direction
            and other.direction
            and self.direction
            == other.direction
        ):
            return False

        if (
            self.port_type
            == "generic"
            or other.port_type
            == "generic"
        ):
            return True

        return (
            self.port_type
            == other.port_type
        )

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.port_type,
            "direction": (
                self.direction
            ),
            "required": self.required,
            "multiple": self.multiple,
            "description": (
                self.description
            ),
            "icon": self.icon,
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
                "Definição de porta "
                "inválida."
            )

        return cls(
            name=data.get(
                "name",
                "",
            ),
            port_type=data.get(
                "type",
                "generic",
            ),
            direction=data.get(
                "direction"
            ),
            required=data.get(
                "required",
                False,
            ),
            multiple=data.get(
                "multiple",
                False,
            ),
            description=data.get(
                "description",
                "",
            ),
            icon=data.get(
                "icon",
                "",
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
    )
