from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ProtocolDefinition:
    name: str
    version: str = "1.0"
    description: str = ""
    metadata: dict[str, Any] | None = None


class ProtocolManager:
    def __init__(self) -> None:
        self._protocols: dict[
            str,
            ProtocolDefinition,
        ] = {}

    def register(
        self,
        name: str,
        version: str = "1.0",
        description: str = "",
        metadata: dict[str, Any] | None = None,
    ) -> ProtocolDefinition:
        protocol = ProtocolDefinition(
            name=name,
            version=version,
            description=description,
            metadata=metadata or {},
        )

        self._protocols[name] = protocol

        return protocol

    def get(
        self,
        name: str,
    ) -> ProtocolDefinition | None:
        return self._protocols.get(name)

    def list(self) -> list[ProtocolDefinition]:
        return list(self._protocols.values())

    def remove(
        self,
        name: str,
    ) -> bool:
        return self._protocols.pop(
            name,
            None,
        ) is not None
