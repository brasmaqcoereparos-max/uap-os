from app.modules.voice.command_policy import (
    VoiceCommandPolicy,
)


class VoicePolicyRegistry:

    def __init__(self):
        self._policies: dict[
            str,
            VoiceCommandPolicy,
        ] = {}

    def register(
        self,
        policy: VoiceCommandPolicy,
    ):
        self._policies[
            policy.command
        ] = policy

        return policy

    def get(
        self,
        command: str,
    ):
        return self._policies.get(
            command
        )

    def remove(
        self,
        command: str,
    ):
        return self._policies.pop(
            command,
            None,
        )

    def list_all(self):
        return list(
            self._policies.values()
        )

    def clear(self):
        self._policies.clear()


voice_policy_registry = (
    VoicePolicyRegistry()
      )
