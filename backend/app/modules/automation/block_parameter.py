from enum import Enum


class ParameterType(
    str,
    Enum,
):
    NUMBER = "number"
    INTEGER = "integer"

    TEXT = "text"
    BOOLEAN = "boolean"

    SELECT = "select"
    TIME = "time"

    COLOR = "color"

    DEVICE = "device"
    SENSOR = "sensor"
    ACTUATOR = "actuator"

    FILE = "file"
    IMAGE = "image"

    EXPRESSION = "expression"

    @classmethod
    def normalize(
        cls,
        value,
    ):
        if isinstance(
            value,
            cls,
        ):
            return value

        text = str(
            value
        ).strip().lower()

        for item in cls:
            if item.value == text:
                return item

        raise ValueError(
            "Tipo de parâmetro "
            f"inválido: {value}"
        )


class BlockParameter:
    def __init__(
        self,
        name,
        parameter_type,
        default=None,
        description="",
        required=False,
        options=None,
        minimum=None,
        maximum=None,
        unit=None,
        visible=True,
        advanced=False,
    ):
        self.name = str(name)

        self.parameter_type = (
            ParameterType.normalize(
                parameter_type
            )
        )

        self.default = default
        self.value = default

        self.description = str(
            description
        )

        self.required = bool(
            required
        )

        self.options = list(
            options or []
        )

        self.minimum = minimum
        self.maximum = maximum

        self.unit = unit

        self.visible = bool(
            visible
        )

        self.advanced = bool(
            advanced
        )

    def validate(
        self,
        value,
    ):
        if value is None:
            return not self.required

        if (
            self.parameter_type
            == ParameterType.NUMBER
        ):
            if not isinstance(
                value,
                (int, float),
            ):
                return False

        elif (
            self.parameter_type
            == ParameterType.INTEGER
        ):
            if (
                not isinstance(
                    value,
                    int,
                )
                or isinstance(
                    value,
                    bool,
                )
            ):
                return False

        elif (
            self.parameter_type
            == ParameterType.BOOLEAN
        ):
            if not isinstance(
                value,
                bool,
            ):
                return False

        elif (
            self.parameter_type
            == ParameterType.SELECT
        ):
            if (
                self.options
                and value
                not in self.options
            ):
                return False

        if self.minimum is not None:
            try:
                if (
                    value
                    < self.minimum
                ):
                    return False

            except TypeError:
                return False

        if self.maximum is not None:
            try:
                if (
                    value
                    > self.maximum
                ):
                    return False

            except TypeError:
                return False

        return True

    def set(
        self,
        value,
    ):
        if not self.validate(
            value
        ):
            raise ValueError(
                "Valor inválido para "
                f"parâmetro '{self.name}': "
                f"{value}"
            )

        self.value = value

        return value

    def get(self):
        return self.value

    def reset(self):
        self.value = self.default

        return self.value

    def to_dict(self):
        return {
            "name": self.name,
            "type": (
                self.parameter_type.value
            ),
            "default": self.default,
            "value": self.value,
            "description": (
                self.description
            ),
            "required": self.required,
            "options": list(
                self.options
            ),
            "minimum": self.minimum,
            "maximum": self.maximum,
            "unit": self.unit,
            "visible": self.visible,
            "advanced": self.advanced,
        }
