from __future__ import annotations

from typing import Any

from .base import CommunicationChannel


class SerialChannel(CommunicationChannel):
    protocol = "serial"

    def __init__(
        self,
        port: str,
        baudrate: int = 115200,
    ) -> None:
        self.port = port
        self.baudrate = baudrate
        self._connected = False
        self._serial: Any = None

    async def connect(self, **kwargs: Any) -> None:
        try:
            import serial
        except ImportError as exc:
            raise RuntimeError(
                "pyserial is required for serial communication"
            ) from exc

        self._serial = serial.Serial(
            self.port,
            self.baudrate,
            timeout=1,
            **kwargs,
        )

        self._connected = True

    async def disconnect(self) -> None:
        if self._serial is not None:
            self._serial.close()

        self._serial = None
        self._connected = False

    async def send(self, data: Any) -> Any:
        if not self.is_connected():
            raise RuntimeError(
                "Serial channel is not connected"
            )

        if isinstance(data, str):
            payload = data.encode()
        elif isinstance(data, bytes):
            payload = data
        else:
            payload = str(data).encode()

        self._serial.write(payload)

        return len(payload)

    async def receive(self) -> Any:
        if not self.is_connected():
            raise RuntimeError(
                "Serial channel is not connected"
            )

        return self._serial.readline()

    def is_connected(self) -> bool:
        return self._connected
