from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Relay:
    relay_id: str
    name: str
    device_id: str | None = None
    state: bool = False
    normally_closed: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def on(self) -> None:
        self.state = True

    def off(self) -> None:
        self.state = False

    def toggle(self) -> None:
        self.state = not self.state


class RelayManager:
    def __init__(self) -> None:
        self._relays: dict[str, Relay] = {}

    def register(
        self,
        relay_id: str,
        name: str,
        device_id: str | None = None,
        normally_closed: bool = False,
        metadata: dict[str, Any] | None = None,
    ) -> Relay:
        relay = Relay(
            relay_id=relay_id,
            name=name,
            device_id=device_id,
            normally_closed=normally_closed,
            metadata=metadata or {},
        )

        self._relays[relay_id] = relay
        return relay

    def get(self, relay_id: str) -> Relay | None:
        return self._relays.get(relay_id)

    def list(self) -> list[Relay]:
        return list(self._relays.values())

    def on(self, relay_id: str) -> Relay:
        relay = self.get(relay_id)

        if relay is None:
            raise KeyError(
                f"Relay '{relay_id}' not found"
            )

        relay.on()
        return relay

    def off(self, relay_id: str) -> Relay:
        relay = self.get(relay_id)

        if relay is None:
            raise KeyError(
                f"Relay '{relay_id}' not found"
            )

        relay.off()
        return relay

    def toggle(self, relay_id: str) -> Relay:
        relay = self.get(relay_id)

        if relay is None:
            raise KeyError(
                f"Relay '{relay_id}' not found"
            )

        relay.toggle()
        return relay

    def remove(self, relay_id: str) -> bool:
        return self._relays.pop(
            relay_id,
            None,
        ) is not None
