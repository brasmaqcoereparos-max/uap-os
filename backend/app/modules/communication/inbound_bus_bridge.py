import uuid

from app.modules.communication.ack_manager import (
    communication_ack_manager,
)
from app.modules.communication.dead_letter import (
    CommunicationDeadLetter,
)
from app.modules.communication.dead_letter_queue import (
    communication_dead_letter_queue,
)
from app.modules.communication.message_bus import (
    communication_message_bus,
)
from app.modules.communication.message_deduplicator import (
    communication_message_deduplicator,
)


class CommunicationInboundBusBridge:

    def forward(
        self,
        message,
    ):
        message_id = str(
            uuid.uuid4()
        )

        if (
            communication_message_deduplicator
            .is_duplicate(
                message
            )
        ):
            ack = (
                communication_ack_manager
                .create(
                    message_id=message_id,
                    acknowledged=False,
                    reason="duplicate",
                )
            )

            return {
                "forwarded": False,
                "reason": "duplicate",
                "ack": ack.to_dict(),
            }

        try:
            payload = (
                message.payload
                if isinstance(
                    message.payload,
                    dict,
                )
                else {
                    "value": (
                        message.payload
                    )
                }
            )

            result = (
                communication_message_bus
                .publish(
                    topic=message.channel,
                    source=message.source,
                    payload=payload,
                )
            )

            ack = (
                communication_ack_manager
                .create(
                    message_id=message_id,
                    acknowledged=(
                        result.delivered
                    ),
                    reason=(
                        None
                        if result.delivered
                        else "not_delivered"
                    ),
                )
            )

            if not result.delivered:
                communication_dead_letter_queue.push(
                    CommunicationDeadLetter(
                        message=(
                            message.to_dict()
                        ),
                        reason=(
                            "not_delivered"
                        ),
                    )
                )

            return {
                "forwarded": (
                    result.delivered
                ),
                "delivery": (
                    result.to_dict()
                ),
                "ack": ack.to_dict(),
            }

        except Exception as exc:
            communication_dead_letter_queue.push(
                CommunicationDeadLetter(
                    message=(
                        message.to_dict()
                    ),
                    reason=str(exc),
                )
            )

            ack = (
                communication_ack_manager
                .create(
                    message_id=message_id,
                    acknowledged=False,
                    reason=str(exc),
                )
            )

            return {
                "forwarded": False,
                "delivery": None,
                "ack": ack.to_dict(),
            }


communication_inbound_bus_bridge = (
    CommunicationInboundBusBridge()
                )
