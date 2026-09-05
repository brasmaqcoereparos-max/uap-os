import asyncio

from app.modules.communication.inbound_handler import (
    communication_inbound_handler,
)
from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)


class CommunicationInboundProcessor:

    def __init__(self):
        self._running = False

    async def process_once(self):
        message = (
            communication_inbound_queue
            .pop()
        )

        if not message:
            return None

        result = (
            communication_inbound_handler
            .handle(message)
        )

        return result

    async def run(
        self,
        sleep_seconds: float = 0.05,
    ):
        self._running = True

        while self._running:
            await self.process_once()

            await asyncio.sleep(
                sleep_seconds
            )

    def stop(self):
        self._running = False

        return True

    @property
    def running(self):
        return self._running


communication_inbound_processor = (
    CommunicationInboundProcessor()
)
