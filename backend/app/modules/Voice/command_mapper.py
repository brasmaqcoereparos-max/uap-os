from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.enums import (
    VoiceIntentType,
)
from app.modules.voice.intent import (
    VoiceIntent,
)


class VoiceCommandMapper:

    def map(
        self,
        intent: VoiceIntent,
    ):
        if (
            intent.intent_type
            == VoiceIntentType
            .NAVIGATION
        ):
            return VoiceCommand(
                command="ui.navigate",
                parameters=dict(
                    intent.parameters
                ),
                confidence=(
                    intent.confidence
                ),
            )

        if (
            intent.intent_type
            == VoiceIntentType
            .CONFIRMATION
        ):
            return VoiceCommand(
                command=(
                    "voice.confirm"
                ),
                confidence=(
                    intent.confidence
                ),
            )

        if (
            intent.intent_type
            == VoiceIntentType
            .CANCELLATION
        ):
            return VoiceCommand(
                command=(
                    "voice.cancel"
                ),
                confidence=(
                    intent.confidence
                ),
            )

        if (
            intent.intent_type
            == VoiceIntentType.COMMAND
        ):
            return VoiceCommand(
                command=(
                    "application.command"
                ),
                parameters=dict(
                    intent.parameters
                ),
                confidence=(
                    intent.confidence
                ),
                requires_confirmation=(
                    True
                ),
            )

        return None


voice_command_mapper = (
    VoiceCommandMapper()
)
