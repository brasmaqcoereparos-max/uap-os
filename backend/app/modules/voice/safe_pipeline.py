from __future__ import annotations

from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.dispatch_executor import (
    voice_dispatch_executor,
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

        command_data = processed.get(
            "command"
        )

        if not command_data:
            processed["dispatch"] = None
            processed["execution"] = None

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
            confidence=float(
                command_data.get(
                    "confidence",
                    1.0,
                )
            ),
            requires_confirmation=bool(
                command_data.get(
                    "requires_confirmation",
                    False,
                )
            ),
        )

        result = (
            voice_dispatch_executor
            .dispatch_and_execute(
                command
            )
        )

        processed["dispatch"] = (
            result.get(
                "dispatch"
            )
        )

        processed["execution"] = (
            result.get(
                "execution"
            )
        )

        return processed


voice_safe_pipeline = (
    VoiceSafePipeline()
)
