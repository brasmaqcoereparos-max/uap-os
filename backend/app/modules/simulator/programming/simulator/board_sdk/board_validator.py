"""
Validação das placas do UAP Board SDK.
"""


class BoardValidator:

    REQUIRED_FIELDS = (
        "name",
        "manufacturer",
        "cpu",
        "frequency",
        "gpio_count",
    )

    NUMERIC_FIELDS = (
        "frequency",
        "gpio_count",
        "pwm_count",
        "adc_count",
        "flash_size",
        "ram_size",
    )

    def validate(
        self,
        board,
        raise_error=True,
    ):
        result = (
            self.validate_detailed(
                board
            )
        )

        if (
            not result["valid"]
            and raise_error
        ):
            raise ValueError(
                "; ".join(
                    result["errors"]
                )
            )

        if raise_error:
            return True

        return result

    def validate_detailed(
        self,
        board,
    ):
        errors = []
        warnings = []

        if board is None:
            return {
                "valid": False,
                "errors": [
                    "Placa não informada."
                ],
                "warnings": [],
            }

        for field in (
            self.REQUIRED_FIELDS
        ):
            if not hasattr(
                board,
                field,
            ):
                errors.append(
                    "Campo obrigatório ausente: "
                    f"{field}"
                )

                continue

            value = getattr(
                board,
                field,
            )

            if value is None:
                errors.append(
                    "Campo obrigatório nulo: "
                    f"{field}"
                )

        for field in (
            "name",
            "manufacturer",
            "cpu",
        ):
            if not hasattr(
                board,
                field,
            ):
                continue

            value = getattr(
                board,
                field,
            )

            if (
                isinstance(
                    value,
                    str,
                )
                and not value.strip()
            ):
                errors.append(
                    f"Campo vazio: {field}"
                )

        for field in (
            self.NUMERIC_FIELDS
        ):
            if not hasattr(
                board,
                field,
            ):
                continue

            value = getattr(
                board,
                field,
            )

            if not isinstance(
                value,
                (int, float),
            ):
                errors.append(
                    f"{field} precisa ser numérico."
                )

                continue

            if value < 0:
                errors.append(
                    f"{field} não pode ser negativo."
                )

        frequency = getattr(
            board,
            "frequency",
            0,
        )

        if (
            isinstance(
                frequency,
                (int, float),
            )
            and frequency == 0
        ):
            warnings.append(
                "Frequência da placa é zero."
            )

        return {
            "valid": (
                len(errors) == 0
            ),
            "errors": errors,
            "warnings": warnings,
        }

    def validate_class(
        self,
        board_class,
        raise_error=True,
    ):
        if not isinstance(
            board_class,
            type,
        ):
            if raise_error:
                raise TypeError(
                    "board_class precisa "
                    "ser uma classe."
                )

            return {
                "valid": False,
                "errors": [
                    "Objeto não é uma classe."
                ],
                "warnings": [],
            }

        return self.validate(
            board_class,
            raise_error=raise_error,
        )

    def validate_instance(
        self,
        board,
        raise_error=True,
    ):
        return self.validate(
            board,
            raise_error=raise_error,
        )


board_validator = BoardValidator()
