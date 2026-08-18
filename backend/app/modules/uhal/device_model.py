from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DeviceCapability:
    name: str
    enabled: bool = True
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class DeviceConnection:
    protocol: str
    address: str | None = None
    port: int | None = None
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class UniversalDevice:
    device_id: str
    name: str
    device_type: str
    manufacturer: str | None = None
    model: str | None = None
    firmware: str | None = None

    connections: list[DeviceConnection] = field(default_factory=list)
    capabilities: list[DeviceCapability] = field(default_factory=list)

    inputs: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, Any] = field(default_factory=dict)

    state: str = "unknown"
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_connection(
        self,
        protocol: str,
        address: str | None = None,
        port: int | None = None,
        parameters: dict[str, Any] | None = None,
    ) -> None:
        self.connections.append(
            DeviceConnection(
                protocol=protocol,
                address=address,
                port=port,
                parameters=parameters or {},
            )
        )

    def add_capability(
        self,
        name: str,
        parameters: dict[str, Any] | None = None,
    ) -> None:
        self.capabilities.append(
            DeviceCapability(
                name=name,
                parameters=parameters or {},
            )
        )

    def has_capability(self, name: str) -> bool:
        return any(
            capability.name == name and capability.enabled
            for capability in self.capabilities
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "device_id": self.device_id,
            "name": self.name,
            "device_type": self.device_type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "firmware": self.firmware,
            "connections": [
                {
                    "protocol": connection.protocol,
                    "address": connection.address,
                    "port": connection.port,
                    "parameters": connection.parameters,
                }
                for connection in self.connections
            ],
            "capabilities": [
                {
                    "name": capability.name,
                    "enabled": capability.enabled,
                    "parameters": capability.parameters,
                }
                for capability in self.capabilities
            ],
            "inputs": self.inputs,
            "outputs": self.outputs,
            "state": self.state,
            "metadata": self.metadata,
        }
