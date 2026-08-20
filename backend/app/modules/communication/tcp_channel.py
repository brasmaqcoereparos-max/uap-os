from __future__ import annotations

import asyncio
from typing import Any

from .base import CommunicationChannel


class TCPChannel(CommunicationChannel):
    protocol = "tcp"

    def __init__(
        self,
        host: str,
        port: int,
    ) -> None:
        self.host = host
        self.port = port
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None

    async def connect(self, **kwargs: Any) -> None:
        self._reader, self._writer = (
            await asyncio.open_connection(
                self.host,
                self.port,
            )
        )

    async def disconnect(self) -> None:
        if self._writer is not None:
            self._writer.close()
            await self._writer.wait_closed()

        self._reader = None
        self._writer = None

    async def send(self, data: Any) -> Any:
        if self._writer is None:
            raise RuntimeError(
                "TCP channel is not connected"
            )

        if isinstance(data, bytes):
            payload = data
        else:
            payload = str(data).encode()

        self._writer.write(payload)
        await self._writer.drain()

        return len(payload)

    async def receive(self) -> bytes:
        if self._reader is None:
            raise RuntimeError(
                "TCP channel is not connected"
            )

        return await self._reader.read(4096)

    def is_connected(self) -> bool:
        return (
            self._reader is not None
            and self._writer is not None
        )
