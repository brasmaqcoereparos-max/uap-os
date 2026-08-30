"""
Validação de periféricos do UAP Peripheral SDK.
"""


class PeripheralValidator:

    REQUIRED = (
        "name",
        "manufacturer",
        "category",
    )

    OPTIONAL = (
        "version",
        "metadata",
        "properties",
        "interfaces",
        "pins",
    )

    def validate(
        self,
        peripheral,
        raise_error=True,
    ):
        result = (
            self.validate_detailed(
                peripheral
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
        peripheral,
    ):
        errors = []
        warnings = []

        if peripheral is None:
            return {
                "valid": False,
                "errors": [
                    "Periférico não informado."
                ],
                "warnings": [],
            }

        for field in self.REQUIRED:
            if not hasattr(
                peripheral,
                field,
            ):
                errors.append(
                    "Campo obrigatório "
                    f"ausente: {field}"
                )

                continue

            value = getattr(
                peripheral,
                field,
            )

            if value is None:
                errors.append(
                    "Campo obrigatório "
                    f"nulo: {field}"
                )

                continue

            if (
                isinstance(
                    value,
                    str,
                )
                and not value.strip()
            ):
                errors.append(
                    "Campo obrigatório "
                    f"vazio: {field}"
                )

        version = getattr(
            peripheral,
            "version",
            None,
        )

        if version is None:
            warnings.append(
                "Versão do periférico "
                "não definida."
            )

        interfaces = getattr(
            peripheral,
            "interfaces",
            None,
        )

        if (
            interfaces is not None
            and not isinstance(
                interfaces,
                (dict, list, tuple, set),
            )
        ):
            errors.append(
                "interfaces deve ser "
                "uma coleção."
            )

        pins = getattr(
            peripheral,
            "pins",
            None,
        )

        if (
            pins is not None
            and not isinstance(
                pins,
                (dict, list, tuple, set),
            )
        ):
            errors.append(
                "pins deve ser "
                "uma coleção."
            )

        metadata = getattr(
            peripheral,
            "metadata",
            None,
        )

        if (
            metadata is not None
            and not isinstance(
                metadata,
                dict,
            )
        ):
            errors.append(
                "metadata deve ser "
                "um dicionário."
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
        peripheral_class,
        raise_error=True,
    ):
        if not isinstance(
            peripheral_class,
            type,
        ):
            result = {
                "valid": False,
                "errors": [
                    "Objeto informado "
                    "não é uma classe."
                ],
                "warnings": [],
            }

            if raise_error:
                raise TypeError(
                    result["errors"][0]
                )

            return result

        return self.validate(
            peripheral_class,
            raise_error=raise_error,
        )

    def validate_instance(
        self,
        peripheral,
        raise_error=True,
    ):
        return self.validate(
            peripheral,
            raise_error=raise_error,
        )

    def validate_description(
        self,
        description,
        raise_error=True,
    ):
        if description is None:
            result = {
                "valid": False,
                "errors": [
                    "Descrição não informada."
                ],
                "warnings": [],
            }

        elif hasattr(
            description,
            "validate",
        ):
            validation = (
                description.validate()
            )

            result = {
                "valid": bool(
                    validation.get(
                        "valid",
                        False,
                    )
                ),
                "errors": list(
                    validation.get(
                        "errors",
                        [],
                    )
                ),
                "warnings": list(
                    validation.get(
                        "warnings",
                        [],
                    )
                ),
            }

        else:
            result = (
                self.validate_detailed(
                    description
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

        return (
            True
            if raise_error
            else result
        )


peripheral_validator = (
    PeripheralValidator()
    )
