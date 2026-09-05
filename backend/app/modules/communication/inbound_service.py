from app.modules.communication.inbound_handler import (
    communication_inbound_handler,
)
from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)


class CommunicationInboundService:

    def receive_next(self):
        message = (
            communication_inbound_queue
            .pop()
        )

        if not message:
            return {
                "received": False,
                "message": None,
                "result": None,
            }

        result = (
            communication_inbound_handler
            .handle(message)
        )

        return {
            "received": True,
            "message": (
                message.to_dict()
            ),
            "result": result,
        }

    def pending(self):
        return (
            communication_inbound_queue
            .snapshot()
        )

    def clear(self):
        communication_inbound_queue.clear()

        return True


communication_inbound_service = (
    CommunicationInboundService()
)
