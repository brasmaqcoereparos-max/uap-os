from __future__ import annotations

from typing import Any

from .base import CommunicationChannel


class BluetoothChannel(CommunicationChannel):
    protocol = "bluetooth"

    def __init__(
        self,
        address: str,
        port: int = 1,
    ) -> None:
        self.address = address
        self.port = port
        self._client: Any = None
        self._connected = False

    async def connect(self, **kwargs: Any) -> None:
        try:
            import bluetooth
        except ImportError as exc:
            raise RuntimeError(
                "Bluetooth library is required"
            ) from exc

        self._client = bluetooth.BluetoothSocket(
            bluetooth.RFCOMM
        )

        self._client.connect(
            (self.address, self.port)
        )

        self._connected = True

    async def disconnect(self) -> None:
        if self._client is not None:
            self._client.close()

        self._client = None
        self._connected = False

    async def send(self, data: Any) -> Any:
        if not self.is_connected():
            raise RuntimeError(
                "Bluetooth channel is not connected"
            )

        if not isinstance(data, bytes):
            data = str(data).encode("utf-8")

        return self._client.send(data)

    async def receive(self) -> bytes:
        if not self.is_connected():
            raise RuntimeError(
                "Bluetooth channel is not connected"
            )

        return self._client.recv(4096)

    def is_connected(self) -> bool:
        return self._connected
