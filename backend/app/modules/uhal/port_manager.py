from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LogicalPort:
    name: str
    direction: str
    data_type: str = "unknown"
    physical_port: str | None = None
    device_id: str | None = None
    value: Any = None
    enabled: bool = True
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class PortManager:

    def __init__(self) -> None:
        self._ports: dict[
            str,
            LogicalPort,
        ] = {}

    def register(
        self,
        name: str,
        direction: str,
        data_type: str = "unknown",
        device_id: str | None = None,
        physical_port: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> LogicalPort:
        normalized_direction = str(
            direction
        ).strip().lower()

        if normalized_direction not in (
            "input",
            "output",
            "bidirectional",
        ):
            raise ValueError(
                f"Invalid port direction: {direction}"
            )

        port = LogicalPort(
            name=name,
            direction=normalized_direction,
            data_type=data_type,
            device_id=device_id,
            physical_port=physical_port,
            metadata=metadata or {},
        )

        self._ports[name] = port

        return port

    def get(
        self,
        name: str,
    ) -> LogicalPort | None:
        return self._ports.get(
            name
        )

    def remove(
        self,
        name: str,
    ) -> bool:
        return (
            self._ports.pop(
                name,
                None,
            )
            is not None
        )

    def list(
        self,
    ) -> list[LogicalPort]:
        return list(
            self._ports.values()
        )

    def set_value(
        self,
        name: str,
        value: Any,
    ) -> None:
        port = self.get(
            name
        )

        if port is None:
            raise KeyError(
                f"Logical port '{name}' not found"
            )

        if not port.enabled:
            raise RuntimeError(
                f"Logical port '{name}' is disabled"
            )

        port.value = value

    def get_value(
        self,
        name: str,
    ) -> Any:
        port = self.get(
            name
        )

        if port is None:
            raise KeyError(
                f"Logical port '{name}' not found"
            )

        if not port.enabled:
            raise RuntimeError(
                f"Logical port '{name}' is disabled"
            )

        return port.value

    def enable(
        self,
        name: str,
    ) -> LogicalPort:
        port = self.get(
            name
        )

        if port is None:
            raise KeyError(
                f"Logical port '{name}' not found"
            )

        port.enabled = True

        return port

    def disable(
        self,
        name: str,
    ) -> LogicalPort:
        port = self.get(
            name
        )

        if port is None:
            raise KeyError(
                f"Logical port '{name}' not found"
            )

        port.enabled = False

        return port
