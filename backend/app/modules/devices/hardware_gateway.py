from __future__ import annotations

from typing import Any

from app.modules.communication.message import UAPMessage


class HardwareGateway:
    """
    Ponte entre o núcleo UAP e qualquer controlador externo.

    Exemplos:
    - Raspberry Pi
    - ESP32
    - Arduino
    - PLC
    - computador
    - máquina dedicada
    """

    def __init__(self) -> None:
        self._devices: dict[str, Any] = {}

    def register(
        self,
        device_id: str,
        channel: Any,
    ) -> None:
        self._devices[device_id] = channel

    def unregister(
        self,
        device_id: str,
    ) -> bool:
        return self._devices.pop(
            device_id,
            None,
        ) is not None

    def list(self) -> list[str]:
        return list(self._devices.keys())

    async def send(
        self,
        device_id: str,
        message: UAPMessage,
    ) -> Any:
        channel = self._devices.get(device_id)

        if channel is None:
            raise KeyError(
                f"Hardware '{device_id}' not registered"
            )

        return await channel.send(
            message.encode()
        )

    async def receive(
        self,
        device_id: str,
    ) -> UAPMessage:
        channel = self._devices.get(device_id)

        if channel is None:
            raise KeyError(
                f"Hardware '{device_id}' not registered"
            )

        data = await channel.receive()

        return UAPMessage.decode(data)
