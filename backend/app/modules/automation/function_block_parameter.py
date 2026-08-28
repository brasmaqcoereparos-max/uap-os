class FunctionBlockParameter:

    def __init__(
        self,
        name,
        value=None,
        parameter_type="generic",
        required=False,
        options=None,
        minimum=None,
        maximum=None,
        unit=None,
    ):
        self.name = str(name)

        self.value = value

        self.parameter_type = str(
            parameter_type
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

    def validate(
        self,
        value,
    ):
        if value is None:
            return not self.required

        if self.options:
            if value not in self.options:
                return False

        if (
            self.parameter_type
            in {
                "number",
                "float",
            }
        ):
            if not isinstance(
                value,
                (int, float),
            ):
                return False

        if (
            self.parameter_type
            in {
                "integer",
                "int",
            }
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

        if (
            self.parameter_type
            == "boolean"
        ):
            if not isinstance(
                value,
                bool,
            ):
                return False

        if self.minimum is not None:
            try:
                if value < self.minimum:
                    return False
            except TypeError:
                return False

        if self.maximum is not None:
            try:
                if value > self.maximum:
                    return False
            except TypeError:
                return False

        return True

    def set_value(
        self,
        value,
    ):
        if not self.validate(
            value
        ):
            raise ValueError(
                f"Valor inválido para "
                f"'{self.name}': {value}"
            )

        self.value = value

        return value

    def get_value(self):
        return self.value

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "type": (
                self.parameter_type
            ),
            "required": (
                self.required
            ),
            "options": list(
                self.options
            ),
            "minimum": self.minimum,
            "maximum": self.maximum,
            "unit": self.unit,
        }
