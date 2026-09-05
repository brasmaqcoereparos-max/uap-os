from typing import Any

from app.modules.communication.communication_facade import (
    communication_facade,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)


class CommunicationAutomationBridge:

    def publish(
        self,
        automation_id: str,
        event: str,
        data: dict[str, Any] | None = None,
    ):
        return communication_facade.publish(
            topic=(
                communication_topics
                .AUTOMATION_EVENT
            ),
            source=(
                f"automation:"
                f"{automation_id}"
            ),
            payload={
                "automation_id": (
                    automation_id
                ),
                "event": event,
                "data": dict(
                    data or {}
                ),
            },
        )


communication_automation_bridge = (
    CommunicationAutomationBridge()
)
