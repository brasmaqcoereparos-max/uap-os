from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.policy_defaults import (
    install_default_voice_policies,
)
from app.modules.voice.policy_registry import (
    voice_policy_registry,
)
from app.modules.voice.validation_result import (
    VoiceValidationResult,
)


class VoiceCommandValidator:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            install_default_voice_policies()

            self._initialized = True

        return self

    def validate(
        self,
        command: VoiceCommand,
    ):
        self.initialize()

        result = VoiceValidationResult(
            valid=True
        )

        if not command.command.strip():
            return result.add_error(
                "Voice command is empty"
            )

        if (
            command.confidence < 0
            or command.confidence > 1
        ):
            result.add_error(
                "Invalid confidence value"
            )

        policy = (
            voice_policy_registry.get(
                command.command
            )
        )

        if not policy:
            return result.add_error(
                "Voice command is not "
                "allowed"
            )

        if not policy.enabled:
            result.add_error(
                "Voice command is disabled"
            )

        if not policy.allows_source(
            command.source
        ):
            result.add_error(
                "Voice command source "
                "is not allowed"
            )

        result.requires_confirmation = (
            command.requires_confirmation
            or policy.requires_confirmation
        )

        return result


voice_command_validator = (
    VoiceCommandValidator()
          )
