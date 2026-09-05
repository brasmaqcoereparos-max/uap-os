from app.modules.communication.channel_policy import (
    CommunicationChannelPolicy,
)


class CommunicationChannelPolicyRegistry:

    def __init__(self):
        self._policies: dict[
            str,
            CommunicationChannelPolicy,
        ] = {}

    def register(
        self,
        policy: (
            CommunicationChannelPolicy
        ),
    ):
        self._policies[
            policy.topic
        ] = policy

        return policy

    def get(
        self,
        topic: str,
    ):
        return self._policies.get(
            topic
        )

    def remove(
        self,
        topic: str,
    ):
        return self._policies.pop(
            topic,
            None,
        )

    def list_all(self):
        return list(
            self._policies.values()
        )

    def clear(self):
        self._policies.clear()


communication_channel_policy_registry = (
    CommunicationChannelPolicyRegistry()
)
