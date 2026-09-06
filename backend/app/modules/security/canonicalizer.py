import json
from typing import Any


class SecurityCanonicalizer:

    def serialize(
        self,
        data: dict[
            str,
            Any,
        ],
    ):
        return json.dumps(
            data,
            sort_keys=True,
            separators=(
                ",",
                ":",
            ),
            ensure_ascii=False,
            default=str,
        ).encode(
            "utf-8"
        )


security_canonicalizer = (
    SecurityCanonicalizer()
)
