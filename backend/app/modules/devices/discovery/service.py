from __future__ import annotations

import socket
from typing import Any


class DeviceDiscoveryService:
    """
    Serviço base para descoberta de dispositivos.

    A arquitetura permite adicionar posteriormente
    descoberta específica por Wi-Fi, Bluetooth, USB,
    Ethernet, RS485 e CAN.
    """

    def __init__(self) -> None:
        self._providers: dict[str, Any] = {}

    def register_provider(self, name: str, provider: Any) -> None:
        self._providers[name] = provider

    def providers(self) -> list[str]:
        return list(self._providers.keys())

    def discover(self, protocol: str | None = None) -> list[dict[str, Any]]:
        if protocol:
            provider = self._providers.get(protocol)

            if provider is None:
                return []

            return list(provider.discover())

        devices: list[dict[str, Any]] = []

        for provider in self._providers.values():
            try:
                devices.extend(provider.discover())
            except Exception:
                continue

        return devices

    @staticmethod
    def local_hostname() -> str:
        return socket.gethostname()

    @staticmethod
    def local_ip() -> str:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.connect(("8.8.8.8", 80))
                return sock.getsockname()[0]
        except OSError:
            return "127.0.0.1"
