from app.modules.communication.inbound_message import (
    CommunicationInboundMessage,
)


class CommunicationInboundHandler:

    def handle(
        self,
        message: CommunicationInboundMessage,
    ):
        return {
            "handled": True,
            "message": (
                message.to_dict()
            ),
        }


communication_inbound_handler = (
    CommunicationInboundHandler()
)
