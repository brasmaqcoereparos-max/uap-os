from datetime import date
from datetime import datetime
from typing import Any


class UILocaleFormatter:

    @staticmethod
    def number(
        value: Any,
        decimals: int = 2,
        locale: str = "pt-BR",
    ):
        try:
            numeric = float(value)

        except (
            TypeError,
            ValueError,
        ):
            return str(value)

        text = (
            f"{numeric:,.{decimals}f}"
        )

        if locale.lower().startswith(
            "pt"
        ):
            text = (
                text
                .replace(",", "#")
                .replace(".", ",")
                .replace("#", ".")
            )

        return text

    @classmethod
    def currency(
        cls,
        value: Any,
        currency: str = "BRL",
        locale: str = "pt-BR",
    ):
        formatted = cls.number(
            value,
            decimals=2,
            locale=locale,
        )

        symbols = {
            "BRL": "R$",
            "USD": "$",
            "EUR": "€",
        }

        symbol = symbols.get(
            currency.upper(),
            currency.upper(),
        )

        return (
            f"{symbol} {formatted}"
        )

    @staticmethod
    def date_value(
        value: date | datetime,
        locale: str = "pt-BR",
    ):
        if locale.lower().startswith(
            "pt"
        ):
            return value.strftime(
                "%d/%m/%Y"
            )

        return value.strftime(
            "%Y-%m-%d"
        )

    @staticmethod
    def time_value(
        value: datetime,
    ):
        return value.strftime(
            "%H:%M:%S"
        )
