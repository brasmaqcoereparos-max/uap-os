from __future__ import annotations

from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.dispatch_executor import (
    voice_dispatch_executor,
)
from app.modules.voice.multimodal_response import (
    voice_multimodal_response,
)
from app.modules.voice.processor import (
    voice_processor,
)
from app.modules.voice.response_builder import (
    voice_response_builder,
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
        *,
        build_response: bool = True,
        tts_provider: (
            str | None
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
            processed[
                "dispatch"
            ] = None

            processed[
                "execution"
            ] = None

            return self._finalize(
                processed,
                transcript=transcript,
                build_response=(
                    build_response
                ),
                tts_provider=(
                    tts_provider
                ),
            )

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

        processed[
            "dispatch"
        ] = result.get(
            "dispatch"
        )

        processed[
            "execution"
        ] = result.get(
            "execution"
        )

        return self._finalize(
            processed,
            transcript=transcript,
            build_response=(
                build_response
            ),
            tts_provider=(
                tts_provider
            ),
        )

    def _finalize(
        self,
        processed: dict,
        *,
        transcript: VoiceTranscript,
        build_response: bool,
        tts_provider: str | None,
    ):
        if not build_response:
            return processed

        response = (
            voice_response_builder
            .from_result(
                processed
            )
        )

        multimodal = (
            voice_multimodal_response
            .build(
                response=response,
                language=(
                    transcript.language
                    or "pt-BR"
                ),
                tts_provider=(
                    tts_provider
                ),
            )
        )

        processed[
            "response"
        ] = multimodal[
            "response"
        ]

        processed[
            "tts"
        ] = multimodal[
            "tts"
        ]

        processed[
            "feedback"
        ] = multimodal[
            "feedback"
        ]

        return processed


voice_safe_pipeline = (
    VoiceSafePipeline()
        )
