from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationUIBridge:

    def publish(
        self,
        event: str,
        data: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=communication_topics.UI_EVENT,
            source="ui",
            payload={
                "event": event,
                "data": dict(
                    data or {}
                ),
            },
        )


communication_ui_bridge = (
    CommunicationUIBridge()
)
