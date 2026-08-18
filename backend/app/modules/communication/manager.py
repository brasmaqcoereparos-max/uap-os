from __future__ import annotations

from typing import Any

from .base import CommunicationChannel


class CommunicationManager:
    def __init__(self) -> None:
        self._channels: dict[str, CommunicationChannel] = {}

    def register(
        self,
        name: str,
        channel: CommunicationChannel,
    ) -> None:
        self._channels[name] = channel

    def unregister(self, name: str) -> bool:
        return self._channels.pop(name, None) is not None

    def get(self, name: str) -> CommunicationChannel | None:
        return self._channels.get(name)

    def list(self) -> list[str]:
        return list(self._channels.keys())

    async def send(self, name: str, data: Any) -> Any:
        channel = self.get(name)

        if channel is None:
            raise KeyError(f"Communication channel '{name}' not found")

        return await channel.send(data)

    async def receive(self, name: str) -> Any:
        channel = self.get(name)

        if channel is None:
            raise KeyError(f"Communication channel '{name}' not found")

        return await channel.receive()
