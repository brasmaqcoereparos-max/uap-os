from dataclasses import dataclass
from typing import Any

from app.modules.ui.form_field import (
    UIFormField,
)


@dataclass
class UIValidationResult:
    valid: bool

    message: str | None = None


class UIFormValidator:

    @staticmethod
    def required(
        field: UIFormField,
    ):
        if not field.required:
            return UIValidationResult(
                valid=True
            )

        value = field.value

        if value is None:
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} is required"
                ),
            )

        if (
            isinstance(value, str)
            and not value.strip()
        ):
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} is required"
                ),
            )

        return UIValidationResult(
            valid=True
        )

    @staticmethod
    def min_length(
        field: UIFormField,
        length: int,
    ):
        value = field.value

        if value is None:
            return UIValidationResult(
                valid=True
            )

        if len(str(value)) < length:
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} must have "
                    f"at least {length} "
                    "characters"
                ),
            )

        return UIValidationResult(
            valid=True
        )

    @staticmethod
    def max_length(
        field: UIFormField,
        length: int,
    ):
        value = field.value

        if value is None:
            return UIValidationResult(
                valid=True
            )

        if len(str(value)) > length:
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} must have "
                    f"at most {length} "
                    "characters"
                ),
            )

        return UIValidationResult(
            valid=True
        )

    @staticmethod
    def numeric_range(
        field: UIFormField,
        minimum: float | None = None,
        maximum: float | None = None,
    ):
        if field.value is None:
            return UIValidationResult(
                valid=True
            )

        try:
            value = float(field.value)

        except (
            TypeError,
            ValueError,
        ):
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} must be "
                    "numeric"
                ),
            )

        if (
            minimum is not None
            and value < minimum
        ):
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} must be "
                    f">= {minimum}"
                ),
            )

        if (
            maximum is not None
            and value > maximum
        ):
            return UIValidationResult(
                valid=False,
                message=(
                    f"{field.name} must be "
                    f"<= {maximum}"
                ),
            )

        return UIValidationResult(
            valid=True
    )
