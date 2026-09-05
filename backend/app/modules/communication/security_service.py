from app.modules.communication.auth_context import (
    CommunicationAuthContext,
)
from app.modules.communication.auth_validator import (
    communication_auth_validator,
)
from app.modules.communication.channel_policy_registry import (
    communication_channel_policy_registry,
)
from app.modules.communication.message_envelope import (
    CommunicationMessageEnvelope,
)
from app.modules.communication.message_validator import (
    communication_message_validator,
)


class CommunicationSecurityService:

    def validate(
        self,
        envelope: (
            CommunicationMessageEnvelope
        ),
        auth_context: (
            CommunicationAuthContext
            | None
        ) = None,
    ):
        message_validation = (
            communication_message_validator
            .validate(envelope)
        )

        if not message_validation.valid:
            return {
                "allowed": False,
                "message_validation": (
                    message_validation
                    .to_dict()
                ),
                "auth": None,
                "policy": None,
            }

        policy = (
            communication_channel_policy_registry
            .get(
                envelope.topic
            )
        )

        if not policy:
            return {
                "allowed": True,
                "message_validation": (
                    message_validation
                    .to_dict()
                ),
                "auth": None,
                "policy": None,
            }

        if not policy.allows_source(
            envelope.source
        ):
            return {
                "allowed": False,
                "message_validation": (
                    message_validation
                    .to_dict()
                ),
                "auth": {
                    "allowed": False,
                    "reason": (
                        "source_not_allowed"
                    ),
                },
                "policy": (
                    policy.to_dict()
                ),
            }

        if not policy.allows_target(
            envelope.target
        ):
            return {
                "allowed": False,
                "message_validation": (
                    message_validation
                    .to_dict()
                ),
                "auth": {
                    "allowed": False,
                    "reason": (
                        "target_not_allowed"
                    ),
                },
                "policy": (
                    policy.to_dict()
                ),
            }

        auth = (
            communication_auth_validator
            .validate(
                context=auth_context,
                policy=policy,
            )
        )

        return {
            "allowed": auth[
                "allowed"
            ],
            "message_validation": (
                message_validation
                .to_dict()
            ),
            "auth": auth,
            "policy": (
                policy.to_dict()
            ),
        }


communication_security_service = (
    CommunicationSecurityService()
      )
