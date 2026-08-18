from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class DeviceType(str, Enum):
    SENSOR = "sensor"
    ACTUATOR = "actuator"
    MOTOR = "motor"
    CAMERA = "camera"
    DISPLAY = "display"
    CONTROLLER = "controller"
    RELAY = "relay"
    PUMP = "pump"
    SERVO = "servo"
    UNKNOWN = "unknown"


class DeviceState(str, Enum):
    OFFLINE = "offline"
    ONLINE = "online"
    ERROR = "error"
    UNKNOWN = "unknown"


@dataclass
class HardwarePort:
    name: str
    direction: str = "unknown"
    data_type: str = "unknown"
    value: Any = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class HardwareDevice:
    device_id: str
    name: str
    device_type: DeviceType = DeviceType.UNKNOWN
    manufacturer: str | None = None
    model: str | None = None
    connection: str | None = None
    state: DeviceState = DeviceState.UNKNOWN

    inputs: dict[str, HardwarePort] = field(default_factory=dict)
    outputs: dict[str, HardwarePort] = field(default_factory=dict)
    capabilities: set[str] = field(default_factory=set)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_input(
        self,
        name: str,
        data_type: str = "unknown",
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self.inputs[name] = HardwarePort(
            name=name,
            direction="input",
            data_type=data_type,
            metadata=metadata or {},
        )

    def add_output(
        self,
        name: str,
        data_type: str = "unknown",
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self.outputs[name] = HardwarePort(
            name=name,
            direction="output",
            data_type=data_type,
            metadata=metadata or {},
        )

    def add_capability(self, capability: str) -> None:
        self.capabilities.add(capability)

    def set_input(self, name: str, value: Any) -> None:
        if name not in self.inputs:
            raise KeyError(f"Input '{name}' not found")

        self.inputs[name].value = value

    def set_output(self, name: str, value: Any) -> None:
        if name not in self.outputs:
            raise KeyError(f"Output '{name}' not found")

        self.outputs[name].value = value

    def get_input(self, name: str) -> Any:
        if name not in self.inputs:
            raise KeyError(f"Input '{name}' not found")

        return self.inputs[name].value

    def get_output(self, name: str) -> Any:
        if name not in self.outputs:
            raise KeyError(f"Output '{name}' not found")

        return self.outputs[name].value

    def to_dict(self) -> dict[str, Any]:
        return {
            "device_id": self.device_id,
            "name": self.name,
            "device_type": self.device_type.value,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "connection": self.connection,
            "state": self.state.value,
            "inputs": {
                name: {
                    "name": port.name,
                    "direction": port.direction,
                    "data_type": port.data_type,
                    "value": port.value,
                    "metadata": port.metadata,
                }
                for name, port in self.inputs.items()
            },
            "outputs": {
                name: {
                    "name": port.name,
                    "direction": port.direction,
                    "data_type": port.data_type,
                    "value": port.value,
                    "metadata": port.metadata,
                }
                for name, port in self.outputs.items()
            },
            "capabilities": sorted(self.capabilities),
            "metadata": self.metadata,
        }


class HardwareAbstractionLayer:
    """
    Camada de abstração de hardware do UAP.

    O projeto trabalha com dispositivos lógicos,
    independentemente do controlador físico utilizado.
    """

    def __init__(self) -> None:
        self._devices: dict[str, HardwareDevice] = {}

    def register_device(self, device: HardwareDevice) -> HardwareDevice:
        self._devices[device.device_id] = device
        return device

    def unregister_device(self, device_id: str) -> None:
        self._devices.pop(device_id, None)

    def get_device(self, device_id: str) -> HardwareDevice | None:
        return self._devices.get(device_id)

    def list_devices(self) -> list[HardwareDevice]:
        return list(self._devices.values())

    def set_device_state(
        self,
        device_id: str,
        state: DeviceState,
    ) -> HardwareDevice:
        device = self._require_device(device_id)
        device.state = state
        return device

    def write(
        self,
        device_id: str,
        output: str,
        value: Any,
    ) -> HardwareDevice:
        device = self._require_device(device_id)
        device.set_output(output, value)
        return device

    def read(
        self,
        device_id: str,
        input_name: str,
    ) -> Any:
        device = self._require_device(device_id)
        return device.get_input(input_name)

    def _require_device(self, device_id: str) -> HardwareDevice:
        device = self.get_device(device_id)

        if device is None:
            raise KeyError(f"Hardware device '{device_id}' not found")

        return device
