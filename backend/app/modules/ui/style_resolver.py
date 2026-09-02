from typing import Any

from app.modules.ui.style_tokens import (
    UIStyleTokens,
    ui_style_tokens,
)


class UIStyleResolver:

    def __init__(
        self,
        tokens: UIStyleTokens = (
            ui_style_tokens
        ),
    ):
        self.tokens = tokens

    def resolve_value(
        self,
        value: Any,
    ):
        if not isinstance(
            value,
            str,
        ):
            return value

        if not value.startswith(
            "$"
        ):
            return value

        token_name = value[1:]

        return self.tokens.value(
            token_name,
            value,
        )

    def resolve(
        self,
        style: dict[
            str,
            Any,
        ],
    ):
        return {
            key: self.resolve_value(
                value
            )
            for key, value
            in style.items()
        }


ui_style_resolver = (
    UIStyleResolver()
)
