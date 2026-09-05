import json
from typing import Any

from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class CommunicationSerialProvider:

    @property
    def name(self):
        return "serial-real"

    def available(self):
        try:
            import serial  # noqa: F401

            return True

        except ImportError:
            return False

    def send(
        self,
        destination: str,
        payload: dict[str, Any],
        baudrate: int = 115200,
        timeout: float = 2.0,
    ):
        if not self.available():
            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=False,
                    destination=destination,
                    error=(
                        "pyserial "
                        "is not installed"
                    ),
                )
            )

        try:
            import serial

            raw = (
                json.dumps(payload)
                + "\n"
            ).encode(
                "utf-8"
            )

            with serial.Serial(
                port=destination,
                baudrate=baudrate,
                timeout=timeout,
            ) as connection:
                connection.write(raw)

            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=True,
                    destination=destination,
                    response={
                        "bytes": len(raw),
                    },
                )
            )

        except Exception as exc:
            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=False,
                    destination=destination,
                    error=str(exc),
                )
            )


communication_serial_provider = (
    CommunicationSerialProvider()
          )
