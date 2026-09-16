from __future__ import annotations

from typing import Any

from app.modules.uhal.hardware_controller import (
    HardwareController,
)
from app.modules.uhal.port_manager import (
    PortManager,
)


class IOManager:
    def __init__(
        self,
        ports: PortManager | None = None,
        hardware: HardwareController | None = None,
    ) -> None:
        self.ports = ports or PortManager()
        self.hardware = hardware

    def _require_port(
        self,
        port_name: str,
    ):
        port = self.ports.get(
            port_name
        )

        if port is None:
            raise KeyError(
                f"Port '{port_name}' not found"
            )

        if not port.enabled:
            raise RuntimeError(
                f"Port '{port_name}' is disabled"
            )

        return port

    def _physical_pin(
        self,
        port_name: str,
    ) -> str | None:
        port = self._require_port(
            port_name
        )

        if not port.physical_port:
            return None

        return port.physical_port

    def write(
        self,
        port_name: str,
        value: Any,
    ) -> Any:
        port = self._require_port(
            port_name
        )

        if port.direction not in (
            "output",
            "bidirectional",
        ):
            raise ValueError(
                f"Port '{port_name}' is not an output"
            )

        result = None

        if (
            self.hardware is not None
            and port.physical_port
        ):
            result = self.hardware.write(
                port.physical_port,
                value,
            )

        self.ports.set_value(
            port_name,
            value,
        )

        return result

    def read(
        self,
        port_name: str,
    ) -> Any:
        port = self._require_port(
            port_name
        )

        if port.direction not in (
            "input",
            "bidirectional",
            "output",
        ):
            raise ValueError(
                f"Port '{port_name}' cannot be read"
            )

        if (
            self.hardware is not None
            and port.physical_port
            and port.direction
            in (
                "input",
                "bidirectional",
            )
        ):
            value = self.hardware.read(
                port.physical_port
            )

            self.ports.set_value(
                port_name,
                value,
            )

            return value

        return self.ports.get_value(
            port_name
        )

    def pwm(
        self,
        port_name: str,
        duty: Any,
    ) -> Any:
        port = self._require_port(
            port_name
        )

        if port.direction not in (
            "output",
            "bidirectional",
        ):
            raise ValueError(
                f"Port '{port_name}' is not an output"
            )

        if not port.physical_port:
            self.ports.set_value(
                port_name,
                duty,
            )
            return None

        if self.hardware is None:
            self.ports.set_value(
                port_name,
                duty,
            )
            return None

        result = self.hardware.pwm(
            port.physical_port,
            duty,
        )

        self.ports.set_value(
            port_name,
            duty,
        )

        return result

    def configure(
        self,
        name: str,
        direction: str,
        data_type: str = "unknown",
        device_id: str | None = None,
        physical_port: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        self.ports.register(
            name=name,
            direction=direction,
            data_type=data_type,
            device_id=device_id,
            physical_port=physical_port,
            metadata=metadata,
        )

    def bind_hardware(
        self,
        hardware: HardwareController,
    ) -> None:
        self.hardware = hardware

    def unbind_hardware(self) -> None:
        self.hardware = None

    def is_hardware_bound(self) -> bool:
        return self.hardware is not None
