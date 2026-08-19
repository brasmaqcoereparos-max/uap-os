from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.modules.uhal.device_model import UniversalDevice


@dataclass
class DiagnosticResult:
    device_id: str
    healthy: bool
    checks: dict[str, bool] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)


class DeviceDiagnostics:

    def run(
        self,
        device: UniversalDevice,
    ) -> DiagnosticResult:
        checks: dict[str, bool] = {}
        warnings: list[str] = []
        errors: list[str] = []

        checks["identity"] = bool(device.device_id)
        checks["name"] = bool(device.name)
        checks["type"] = bool(device.device_type)

        if not device.connections:
            warnings.append(
                "Nenhuma conexão foi configurada."
            )

        checks["connection"] = bool(device.connections)

        if not device.capabilities:
            warnings.append(
                "Nenhuma capacidade foi registrada."
            )

        checks["capabilities"] = bool(device.capabilities)

        if device.state == "error":
            errors.append(
                "O dispositivo está em estado de erro."
            )

        checks["state"] = device.state != "error"

        healthy = (
            all(checks.values())
            and not errors
        )

        return DiagnosticResult(
            device_id=device.device_id,
            healthy=healthy,
            checks=checks,
            warnings=warnings,
            errors=errors,
            details={
                "state": device.state,
                "connections": len(device.connections),
                "capabilities": len(device.capabilities),
                "inputs": len(device.inputs),
                "outputs": len(device.outputs),
            },
        )
