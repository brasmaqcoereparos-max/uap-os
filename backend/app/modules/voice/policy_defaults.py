from app.modules.voice.command_policy import (
    VoiceCommandPolicy,
)
from app.modules.voice.policy_registry import (
    voice_policy_registry,
)


class VoicePolicyDefaults:

    @staticmethod
    def install():
        policies = [
            VoiceCommandPolicy(
                command="ui.navigate",
            ),
            VoiceCommandPolicy(
                command="voice.confirm",
            ),
            VoiceCommandPolicy(
                command="voice.cancel",
            ),
            VoiceCommandPolicy(
                command=(
                    "application.command"
                ),
                requires_confirmation=True,
            ),
        ]

        for policy in policies:
            voice_policy_registry.register(
                policy
            )

        return policies


def install_default_voice_policies():
    return VoicePolicyDefaults.install()
