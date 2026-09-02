from app.modules.voice.application_bridge import (
    voice_application_bridge,
)
from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.execution_result import (
    VoiceExecutionResult,
)


class VoiceExecutor:

    def execute(
        self,
        command: VoiceCommand,
    ):
        try:
            result = (
                voice_application_bridge
                .dispatch(
                    command.command,
                    command.parameters,
                )
            )

            return VoiceExecutionResult(
                executed=True,
                status="executed",
                result=result,
                command=(
                    command.to_dict()
                ),
            )

        except Exception as exc:
            return VoiceExecutionResult(
                executed=False,
                status="error",
                command=(
                    command.to_dict()
                ),
                errors=[
                    str(exc)
                ],
            )


voice_executor = VoiceExecutor()
