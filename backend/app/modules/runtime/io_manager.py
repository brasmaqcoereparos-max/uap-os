from __future__ import annotations

from typing import Any

from app.modules.uhal.port_manager import PortManager


class IOManager:
    def __init__(
        self,
        ports: PortManager | None = None,
    ) -> None:
        self.ports = ports or PortManager()

    def write(
        self,
        port_name: str,
        value: Any,
    ) -> None:
        port = self.ports.get(port_name)

        if port is None:
            raise KeyError(
                f"Port '{port_name}' not found"
            )

        if port.direction not in (
            "output",
            "bidirectional",
        ):
            raise ValueError(
                f"Port '{port_name}' is not an output"
            )

        self.ports.set_value(
            port_name,
            value,
        )

    def read(
        self,
        port_name: str,
    ) -> Any:
        port = self.ports.get(port_name)

        if port is None:
            raise KeyError(
                f"Port '{port_name}' not found"
            )

        return self.ports.get_value(port_name)

    def configure(
        self,
        name: str,
        direction: str,
        data_type: str = "unknown",
    ) -> None:
        self.ports.register(
            name=name,
            direction=direction,
            data_type=data_type,
        )
