import asyncio
import json

from app.modules.communication.websocket_config import (
    CommunicationWebSocketConfig,
)


class CommunicationWebSocketProvider:

    @property
    def name(self):
        return "websocket-real"

    def available(self):
        try:
            import websockets  # noqa: F401

            return True

        except ImportError:
            return False

    async def _send_async(
        self,
        config: CommunicationWebSocketConfig,
        payload: dict,
    ):
        import websockets

        async with websockets.connect(
            config.url,
            additional_headers=(
                config.headers
            ),
            open_timeout=(
                config.timeout_seconds
            ),
        ) as websocket:
            await websocket.send(
                json.dumps(payload)
            )

            return {
                "sent": True,
                "url": config.url,
            }

    def send(
        self,
        destination: str,
        payload: dict,
    ):
        if not self.available():
            return {
                "success": False,
                "provider": self.name,
                "error": (
                    "websockets "
                    "is not installed"
                ),
            }

        config = (
            CommunicationWebSocketConfig(
                url=destination
            )
        )

        try:
            result = asyncio.run(
                self._send_async(
                    config,
                    payload,
                )
            )

            return {
                "success": True,
                "provider": self.name,
                "result": result,
            }

        except Exception as exc:
            return {
                "success": False,
                "provider": self.name,
                "error": str(exc),
            }


communication_websocket_provider = (
    CommunicationWebSocketProvider()
)
