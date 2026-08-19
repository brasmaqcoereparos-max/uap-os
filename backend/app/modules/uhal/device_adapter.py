from __future__ import annotations

from typing import Any

from .hardware_abstraction import (
    DeviceState,
    HardwareAbstractionLayer,
    HardwareDevice,
)
from .device_model import UniversalDevice


class DeviceAdapter:
    def __init__(
        self,
        hal: HardwareAbstractionLayer,
    ) -> None:
        self.hal = hal

    def attach(self, device: UniversalDevice) -> HardwareDevice:
        hardware = HardwareDevice(
            device_id=device.device_id,
            name=device.name,
            device_type=device.device_type,
            manufacturer=device.manufacturer,
            model=device.model,
            connection=(
                device.connections[0].protocol
                if device.connections
                else None
            ),
        )

        hardware.state = DeviceState.ONLINE

        for capability in device.capabilities:
            if capability.enabled:
                hardware.add_capability(capability.name)

        for name, value in device.inputs.items():
            hardware.add_input(
                name=name,
                data_type=str(value.get("data_type", "unknown"))
                if isinstance(value, dict)
                else "unknown",
            )

        for name, value in device.outputs.items():
            hardware.add_output(
                name=name,
                data_type=str(value.get("data_type", "unknown"))
                if isinstance(value, dict)
                else "unknown",
            )

        return self.hal.register_device(hardware)

    def write(
        self,
        device_id: str,
        output: str,
        value: Any,
    ) -> None:
        self.hal.write(device_id, output, value)

    def read(
        self,
        device_id: str,
        input_name: str,
    ) -> Any:
        return self.hal.read(device_id, input_name)
