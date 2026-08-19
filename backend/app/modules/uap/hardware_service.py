from __future__ import annotations

from typing import Any

from app.modules.devices.diagnostics import (
    DeviceDiagnostics,
)
from app.modules.devices.discovery import (
    create_default_discovery_service,
)
from app.modules.uap.hardware_context import (
    UAPHardwareContext,
)
from app.modules.uhal.compatibility import (
    HardwareCompatibilityChecker,
)
from app.modules.uhal.device_adapter import (
    DeviceAdapter,
)
from app.modules.uhal.device_model import (
    UniversalDevice,
)


class UAPHardwareService:
    def __init__(
        self,
        context: UAPHardwareContext | None = None,
    ) -> None:
        self.context = context or UAPHardwareContext()

        self.adapter = DeviceAdapter(
            self.context.hal
        )

        self.compatibility = (
            HardwareCompatibilityChecker()
        )

        self.diagnostics = DeviceDiagnostics()

        self.discovery = (
            create_default_discovery_service()
        )

    def register_device(
        self,
        device: UniversalDevice,
    ) -> UniversalDevice:
        self.context.devices.register(device)
        self.adapter.attach(device)

        return device

    def unregister_device(
        self,
        device_id: str,
    ) -> bool:
        self.context.hal.unregister_device(
            device_id
        )

        return self.context.devices.unregister(
            device_id
        )

    def get_device(
        self,
        device_id: str,
    ) -> UniversalDevice | None:
        return self.context.devices.get(device_id)

    def list_devices(
        self,
    ) -> list[UniversalDevice]:
        return self.context.devices.list()

    def discover_devices(
        self,
        protocol: str | None = None,
    ) -> list[dict[str, Any]]:
        return self.discovery.discover(
            protocol
        )

    def check_compatibility(
        self,
        device_id: str,
        required_capabilities: list[str],
    ) -> dict[str, Any]:
        device = self.get_device(device_id)

        if device is None:
            raise KeyError(
                f"Device '{device_id}' not found"
            )

        result = self.compatibility.check(
            device,
            required_capabilities,
        )

        return {
            "compatible": result.compatible,
            "missing_capabilities":
                result.missing_capabilities,
            "available_capabilities":
                result.available_capabilities,
            "message": result.message,
        }

    def diagnose(
        self,
        device_id: str,
    ) -> dict[str, Any]:
        device = self.get_device(device_id)

        if device is None:
            raise KeyError(
                f"Device '{device_id}' not found"
            )

        result = self.diagnostics.run(device)

        return {
            "device_id": result.device_id,
            "healthy": result.healthy,
            "checks": result.checks,
            "warnings": result.warnings,
            "errors": result.errors,
            "details": result.details,
        }

    def system_status(self) -> dict[str, Any]:
        return self.context.status()
