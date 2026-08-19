from __future__ import annotations

import asyncio
import socket
from typing import Any


class NetworkDiscoveryProvider:
    protocol = "network"

    def __init__(
        self,
        port: int = 4210,
        timeout: float = 0.5,
    ) -> None:
        self.port = port
        self.timeout = timeout

    async def _probe(
        self,
        host: str,
    ) -> dict[str, Any] | None:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(host, self.port),
                timeout=self.timeout,
            )

            writer.close()
            await writer.wait_closed()

            return {
                "protocol": self.protocol,
                "address": host,
                "port": self.port,
                "state": "online",
            }

        except Exception:
            return None

    async def discover_async(
        self,
        hosts: list[str],
    ) -> list[dict[str, Any]]:
        results = await asyncio.gather(
            *(self._probe(host) for host in hosts)
        )

        return [
            result
            for result in results
            if result is not None
        ]

    def discover(
        self,
        hosts: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        if hosts is None:
            local_ip = self._local_ip()

            if local_ip == "127.0.0.1":
                return []

            prefix = local_ip.rsplit(".", 1)[0]

            hosts = [
                f"{prefix}.{number}"
                for number in range(1, 255)
            ]

        return asyncio.run(
            self.discover_async(hosts)
        )

    @staticmethod
    def _local_ip() -> str:
        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM,
            ) as sock:
                sock.connect(("8.8.8.8", 80))
                return sock.getsockname()[0]
        except OSError:
            return "127.0.0.1"
