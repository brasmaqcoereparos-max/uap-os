from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.command_dispatcher import (
    voice_command_dispatcher,
)
from app.modules.voice.processor import (
    voice_processor,
)
from app.modules.voice.session import (
    VoiceSession,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceSafePipeline:

    def process_transcript(
        self,
        transcript: VoiceTranscript,
        session: (
            VoiceSession | None
        ) = None,
    ):
        processed = (
            voice_processor.process(
                transcript=transcript,
                session=session,
            )
        )

        command_data = (
            processed.get(
                "command"
            )
        )

        if not command_data:
            processed[
                "dispatch"
            ] = None

            return processed

        command = VoiceCommand(
            command=command_data[
                "command"
            ],
            parameters=dict(
                command_data.get(
                    "parameters",
                    {},
                )
            ),
            source=command_data.get(
                "source",
                "voice",
            ),
            confidence=command_data.get(
                "confidence",
                1.0,
            ),
            requires_confirmation=(
                command_data.get(
                    "requires_confirmation",
                    False,
                )
            ),
        )

        dispatch = (
            voice_command_dispatcher
            .dispatch(command)
        )

        processed[
            "dispatch"
        ] = dispatch.to_dict()

        return processed


voice_safe_pipeline = (
    VoiceSafePipeline()
)
