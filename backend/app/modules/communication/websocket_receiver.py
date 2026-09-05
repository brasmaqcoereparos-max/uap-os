import asyncio
import json

from app.modules.communication.inbound_message import (
    CommunicationInboundMessage,
)
from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)
from app.modules.communication.websocket_session import (
    CommunicationWebSocketSession,
)


class CommunicationWebSocketReceiver:

    def __init__(self):
        self._session = None
        self._running = False

    def available(self):
        try:
            import websockets  # noqa: F401

            return True

        except ImportError:
            return False

    async def listen(
        self,
        url: str,
        headers: dict | None = None,
    ):
        if not self.available():
            raise RuntimeError(
                "websockets is not installed"
            )

        import websockets

        session = (
            CommunicationWebSocketSession(
                url=url
            )
        )

        self._session = session
        self._running = True

        async with websockets.connect(
            url,
            additional_headers=headers,
        ) as websocket:
            session.connect()

            while self._running:
                raw = await websocket.recv()

                try:
                    payload = json.loads(
                        raw
                    )

                except Exception:
                    payload = raw

                communication_inbound_queue
                .push(
                    CommunicationInboundMessage(
                        source="websocket",
                        channel=url,
                        payload=payload,
                    )
                )

        session.disconnect()

    def stop(self):
        self._running = False

        return True

    def status(self):
        if not self._session:
            return {
                "connected": False,
                "url": None,
            }

        return (
            self._session.to_dict()
        )


communication_websocket_receiver = (
    CommunicationWebSocketReceiver()
)
