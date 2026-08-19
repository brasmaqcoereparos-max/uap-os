from __future__ import annotations

from dataclasses import dataclass, field

from .device_model import UniversalDevice


@dataclass
class CompatibilityResult:
    compatible: bool
    missing_capabilities: list[str] = field(default_factory=list)
    available_capabilities: list[str] = field(default_factory=list)
    message: str = ""


class HardwareCompatibilityChecker:
    def check(
        self,
        device: UniversalDevice,
        required_capabilities: list[str],
    ) -> CompatibilityResult:
        available = {
            capability.name
            for capability in device.capabilities
            if capability.enabled
        }

        missing = [
            capability
            for capability in required_capabilities
            if capability not in available
        ]

        compatible = not missing

        if compatible:
            message = "Hardware compatível com os requisitos."
        else:
            message = (
                "Hardware incompatível. "
                f"Capacidades ausentes: {', '.join(missing)}"
            )

        return CompatibilityResult(
            compatible=compatible,
            missing_capabilities=missing,
            available_capabilities=sorted(available),
            message=message,
        )
