from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.command_dispatcher import (
    voice_command_dispatcher,
)
from app.modules.voice.confirmation_executor import (
    voice_confirmation_executor,
)
from app.modules.voice.executor import (
    voice_executor,
)


class VoiceDispatchExecutor:

    def dispatch_and_execute(
        self,
        command: VoiceCommand,
    ):
        dispatch = (
            voice_command_dispatcher
            .dispatch(
                command
            )
        )

        if not dispatch.accepted:
            return {
                "dispatch": (
                    dispatch.to_dict()
                ),
                "execution": None,
            }

        if (
            dispatch.status
            == "confirmation_required"
        ):
            return {
                "dispatch": (
                    dispatch.to_dict()
                ),
                "execution": None,
            }

        execution = (
            voice_executor.execute(
                command
            )
        )

        return {
            "dispatch": (
                dispatch.to_dict()
            ),
            "execution": (
                execution.to_dict()
            ),
        }

    def execute_confirmed(
        self,
        confirmation_id: str,
    ):
        execution = (
            voice_confirmation_executor
            .execute(
                confirmation_id
            )
        )

        return execution.to_dict()


voice_dispatch_executor = (
    VoiceDispatchExecutor()
          )
