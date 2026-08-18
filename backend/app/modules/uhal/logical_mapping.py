from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LogicalMapping:
    logical_name: str
    device_id: str
    physical_port: str
    direction: str
    parameters: dict[str, Any] = field(default_factory=dict)


class LogicalMappingManager:
    def __init__(self) -> None:
        self._mappings: dict[str, LogicalMapping] = {}

    def map(
        self,
        logical_name: str,
        device_id: str,
        physical_port: str,
        direction: str,
        parameters: dict[str, Any] | None = None,
    ) -> LogicalMapping:

        mapping = LogicalMapping(
            logical_name=logical_name,
            device_id=device_id,
            physical_port=physical_port,
            direction=direction,
            parameters=parameters or {},
        )

        self._mappings[logical_name] = mapping

        return mapping

    def get(self, logical_name: str) -> LogicalMapping | None:
        return self._mappings.get(logical_name)

    def remove(self, logical_name: str) -> bool:
        return self._mappings.pop(logical_name, None) is not None

    def list(self) -> list[LogicalMapping]:
        return list(self._mappings.values())

    def resolve(self, logical_name: str) -> tuple[str, str] | None:
        mapping = self.get(logical_name)

        if mapping is None:
            return None

        return mapping.device_id, mapping.physical_port

    def export(self) -> list[dict[str, Any]]:
        return [
            {
                "logical_name": mapping.logical_name,
                "device_id": mapping.device_id,
                "physical_port": mapping.physical_port,
                "direction": mapping.direction,
                "parameters": mapping.parameters,
            }
            for mapping in self._mappings.values()
        ]
