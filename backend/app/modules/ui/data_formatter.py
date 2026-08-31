from datetime import datetime
from typing import Any


class UIDataFormatter:

    @staticmethod
    def number(
        value: Any,
        decimals: int = 2,
    ):
        try:
            numeric = float(value)

        except (
            TypeError,
            ValueError,
        ):
            return str(value)

        return f"{numeric:.{decimals}f}"

    @staticmethod
    def integer(
        value: Any,
    ):
        try:
            return str(
                int(float(value))
            )

        except (
            TypeError,
            ValueError,
        ):
            return str(value)

    @staticmethod
    def percentage(
        value: Any,
        decimals: int = 1,
    ):
        try:
            numeric = float(value)

        except (
            TypeError,
            ValueError,
        ):
            return str(value)

        return (
            f"{numeric:.{decimals}f}%"
        )

    @staticmethod
    def boolean(
        value: Any,
        true_text: str = "ON",
        false_text: str = "OFF",
    ):
        if bool(value):
            return true_text

        return false_text

    @staticmethod
    def datetime_value(
        value: Any,
    ):
        if isinstance(
            value,
            datetime,
        ):
            return value.isoformat()

        return str(value)

    @staticmethod
    def unit(
        value: Any,
        unit: str,
        decimals: int = 2,
    ):
        formatted = (
            UIDataFormatter.number(
                value,
                decimals,
            )
        )

        return (
            f"{formatted} {unit}"
            if unit
            else formatted
    )
