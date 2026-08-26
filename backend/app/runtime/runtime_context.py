from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeContext:

    running: bool = False
    mode: str = "normal"

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    devices: dict[str, Any] = field(
        default_factory=dict
    )

    variables: dict[str, Any] = field(
        default_factory=dict
    )

    def set_variable(
        self,
        name: str,
        value: Any,
    ):
        self.variables[name] = value
        return value

    def get_variable(
        self,
        name: str,
        default: Any = None,
    ):
        return self.variables.get(
            name,
            default,
        )

    def register_device(
        self,
        device_id: str,
        device: Any,
    ):
        self.devices[device_id] = device
        return device

    def get_device(
        self,
        device_id: str,
    ):
        return self.devices.get(
            device_id
        )

    def remove_device(
        self,
        device_id: str,
    ):
        return self.devices.pop(
            device_id,
            None,
        )

    def clear(self):
        self.devices.clear()
        self.variables.clear()
        self.metadata.clear()

    def to_dict(self):
        return {
            "running": self.running,
            "mode": self.mode,
            "metadata": dict(self.metadata),
            "devices": list(
                self.devices.keys()
            ),
            "variables": dict(self.variables),
        }


runtime_context = RuntimeContext()
