import uuid
from typing import Any

from app.modules.communication.auth_context import (
    CommunicationAuthContext,
)
from app.modules.communication.message_envelope import (
    CommunicationMessageEnvelope,
)
from app.modules.communication.message_router import (
    communication_message_router,
)
from app.modules.communication.security_defaults import (
    install_default_communication_security,
)
from app.modules.communication.security_service import (
    communication_security_service,
)


class SecureCommunicationMessageBus:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            (
                install_default_communication_security()
            )

            self._initialized = True

        return self

    def publish(
        self,
        topic: str,
        source: str,
        payload: (
            dict[str, Any] | None
        ) = None,
        target: str | None = None,
        auth_context: (
            CommunicationAuthContext
            | None
        ) = None,
    ):
        self.initialize()

        envelope = (
            CommunicationMessageEnvelope(
                id=str(uuid.uuid4()),
                topic=topic,
                source=source,
                target=target,
                payload=dict(
                    payload or {}
                ),
            )
        )

        security = (
            communication_security_service
            .validate(
                envelope=envelope,
                auth_context=auth_context,
            )
        )

        if not security[
            "allowed"
        ]:
            return {
                "delivered": False,
                "security": security,
                "delivery": None,
            }

        delivery = (
            communication_message_router
            .route(envelope)
        )

        return {
            "delivered": (
                delivery.delivered
            ),
            "security": security,
            "delivery": (
                delivery.to_dict()
            ),
        }


secure_communication_message_bus = (
    SecureCommunicationMessageBus()
)
