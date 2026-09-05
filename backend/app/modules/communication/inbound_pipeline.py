from app.modules.communication.filter_registry import (
    communication_filter_registry,
)
from app.modules.communication.inbound_bus_bridge import (
    communication_inbound_bus_bridge,
)
from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)


class CommunicationInboundPipeline:

    def process_next(
        self,
        filter_name: (
            str | None
        ) = None,
    ):
        message = (
            communication_inbound_queue
            .pop()
        )

        if not message:
            return {
                "processed": False,
                "reason": "queue_empty",
                "result": None,
            }

        if filter_name:
            message_filter = (
                communication_filter_registry
                .get(
                    filter_name
                )
            )

            if not message_filter:
                return {
                    "processed": False,
                    "reason": (
                        "filter_not_found"
                    ),
                    "result": None,
                }

            if not (
                message_filter.matches(
                    message
                )
            ):
                return {
                    "processed": False,
                    "reason": (
                        "filtered"
                    ),
                    "result": None,
                }

        result = (
            communication_inbound_bus_bridge
            .forward(message)
        )

        return {
            "processed": True,
            "reason": None,
            "result": result,
        }


communication_inbound_pipeline = (
    CommunicationInboundPipeline()
)
