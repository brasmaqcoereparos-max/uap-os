from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class CommunicationMessageFilter:
    source: str | None = None
    channel: str | None = None

    required_keys: set[str] = field(
        default_factory=set
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def matches(
        self,
        message,
    ):
        if (
            self.source
            and message.source
            != self.source
        ):
            return False

        if (
            self.channel
            and message.channel
            != self.channel
        ):
            return False

        if self.required_keys:
            if not isinstance(
                message.payload,
                dict,
            ):
                return False

            keys = set(
                message.payload.keys()
            )

            if not (
                self.required_keys
                .issubset(keys)
            ):
                return False

        return True
