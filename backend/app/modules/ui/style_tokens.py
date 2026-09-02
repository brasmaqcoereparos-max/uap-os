from typing import Any

from app.modules.ui.style_token import (
    UIStyleToken,
)


class UIStyleTokens:

    def __init__(self):
        self._tokens: dict[
            str,
            UIStyleToken,
        ] = {}

    def register(
        self,
        token: UIStyleToken,
    ):
        self._tokens[
            token.name
        ] = token

        return token

    def set(
        self,
        name: str,
        value: Any,
        category: str = "general",
        description: str = "",
    ):
        token = UIStyleToken(
            name=name,
            value=value,
            category=category,
            description=description,
        )

        return self.register(token)

    def get(
        self,
        name: str,
    ):
        return self._tokens.get(
            name
        )

    def value(
        self,
        name: str,
        default: Any = None,
    ):
        token = self.get(name)

        if not token:
            return default

        return token.value

    def remove(
        self,
        name: str,
    ):
        return self._tokens.pop(
            name,
            None,
        )

    def by_category(
        self,
        category: str,
    ):
        return [
            token
            for token
            in self._tokens.values()
            if token.category == category
        ]

    def list_all(self):
        return list(
            self._tokens.values()
        )

    def to_dict(self):
        return {
            token.name: (
                token.to_dict()
            )
            for token
            in self._tokens.values()
        }


ui_style_tokens = UIStyleTokens()
