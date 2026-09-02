from typing import Any


class UILocalization:

    def __init__(
        self,
        default_locale: str = "pt-BR",
    ):
        self.default_locale = (
            default_locale
        )

        self.current_locale = (
            default_locale
        )

        self._messages: dict[
            str,
            dict[str, str],
        ] = {}

    def register(
        self,
        locale: str,
        messages: dict[
            str,
            str,
        ],
    ):
        target = (
            self._messages
            .setdefault(
                locale,
                {},
            )
        )

        target.update(messages)

    def set_locale(
        self,
        locale: str,
    ):
        self.current_locale = locale

        return locale

    def translate(
        self,
        key: str,
        values: (
            dict[str, Any] | None
        ) = None,
    ):
        messages = (
            self._messages.get(
                self.current_locale,
                {},
            )
        )

        fallback = (
            self._messages.get(
                self.default_locale,
                {},
            )
        )

        text = messages.get(
            key,
            fallback.get(
                key,
                key,
            ),
        )

        if values:
            try:
                text = text.format(
                    **values
                )
            except (
                KeyError,
                ValueError,
            ):
                pass

        return text


ui_localization = UILocalization()
