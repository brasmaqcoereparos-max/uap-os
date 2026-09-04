from typing import Any


class AISchemaGuard:

    def require_keys(
        self,
        data: dict[
            str,
            Any,
        ],
        keys: list[str],
    ):
        missing = [
            key
            for key in keys
            if key not in data
        ]

        return {
            "valid": not missing,
            "missing": missing,
        }

    def ensure_dict(
        self,
        value: Any,
    ):
        return isinstance(
            value,
            dict,
        )

    def ensure_list(
        self,
        value: Any,
    ):
        return isinstance(
            value,
            list,
        )


ai_schema_guard = (
    AISchemaGuard()
)
