from __future__ import annotations

from typing import Any

from .manager import CommunicationManager
from .message import UAPMessage
from .message_router import MessageRouter


class CommunicationHub:
    """
    Camada central de comunicação do UAP.

    Permite conectar o UAP Box a:
    - microcontroladores
    - Raspberry Pi
    - ESP32
    - computadores
    - máquinas
    - módulos externos
    """

    def __init__(self) -> None:
        self.channels = CommunicationManager()
        self.router = MessageRouter()

    def register_channel(
        self,
        name: str,
        channel: Any,
    ) -> None:
        self.channels.register(
            name,
            channel,
        )

    def register_handler(
        self,
        message_type: str,
        handler: Any,
    ) -> None:
        self.router.register(
            message_type,
            handler,
        )

    def route(
        self,
        message: UAPMessage,
    ) -> int:
        return self.router.route(message)

    async def send_message(
        self,
        channel: str,
        message: UAPMessage,
    ) -> Any:
        return await self.channels.send(
            channel,
            message.encode(),
        )

    async def receive_message(
        self,
        channel: str,
    ) -> UAPMessage:
        data = await self.channels.receive(
            channel
        )

        return UAPMessage.decode(data)

    def status(self) -> dict[str, Any]:
        return {
            "channels": self.channels.list(),
        }
