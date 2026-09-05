from app.modules.communication.auth_context import (
    CommunicationAuthContext,
)
from app.modules.communication.channel_policy import (
    CommunicationChannelPolicy,
)


class CommunicationAuthValidator:

    def validate(
        self,
        context: (
            CommunicationAuthContext
            | None
        ),
        policy: (
            CommunicationChannelPolicy
        ),
    ):
        if not policy.enabled:
            return {
                "allowed": False,
                "reason": (
                    "channel_disabled"
                ),
            }

        if (
            policy
            .require_authentication
        ):
            if (
                context is None
                or not context
                .authenticated
            ):
                return {
                    "allowed": False,
                    "reason": (
                        "authentication_required"
                    ),
                }

        return {
            "allowed": True,
            "reason": None,
        }


communication_auth_validator = (
    CommunicationAuthValidator()
      )
