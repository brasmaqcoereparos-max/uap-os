from app.modules.communication.channel_policy import (
    CommunicationChannelPolicy,
)
from app.modules.communication.channel_policy_registry import (
    communication_channel_policy_registry,
)
from app.modules.communication.communication_topics import (
    communication_topics,
)
from app.modules.communication.security_level import (
    CommunicationSecurityLevel,
)


class CommunicationSecurityDefaults:

    @staticmethod
    def install():
        policies = [
            CommunicationChannelPolicy(
                topic=(
                    communication_topics
                    .SYSTEM_EVENT
                ),
                security_level=(
                    CommunicationSecurityLevel
                    .INTERNAL
                ),
                require_authentication=True,
            ),
            CommunicationChannelPolicy(
                topic=(
                    communication_topics
                    .DEVICE_COMMAND
                ),
                security_level=(
                    CommunicationSecurityLevel
                    .RESTRICTED
                ),
                require_authentication=True,
            ),
            CommunicationChannelPolicy(
                topic=(
                    communication_topics
                    .RUNTIME_EVENT
                ),
                security_level=(
                    CommunicationSecurityLevel
                    .PROTECTED
                ),
                require_authentication=True,
            ),
            CommunicationChannelPolicy(
                topic=(
                    communication_topics
                    .AI_EVENT
                ),
                security_level=(
                    CommunicationSecurityLevel
                    .PROTECTED
                ),
                require_authentication=True,
            ),
        ]

        for policy in policies:
            (
                communication_channel_policy_registry
                .register(policy)
            )

        return policies


def install_default_communication_security():
    return (
        CommunicationSecurityDefaults
        .install()
            )
