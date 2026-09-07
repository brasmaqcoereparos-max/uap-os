from typing import Any


class SecurityConfigGuard:

    BLOCKED_KEYS = {
        "password",
        "secret",
        "api_key",
        "token",
        "private_key",
    }

    def sanitize(
        self,
        data: dict[
            str,
            Any,
        ],
    ):
        result = {}

        for key, value in (
            data.items()
        ):
            lowered = str(
                key
            ).lower()

            if any(
                blocked
                in lowered
                for blocked
                in self.BLOCKED_KEYS
            ):
                result[key] = "***"

            elif isinstance(
                value,
                dict,
            ):
                result[key] = (
                    self.sanitize(
                        value
                    )
                )

            else:
                result[key] = value

        return result


security_config_guard = (
    SecurityConfigGuard()
          )
