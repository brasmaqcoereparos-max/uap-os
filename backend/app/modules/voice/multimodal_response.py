from app.modules.voice.feedback_manager import (
    voice_feedback_manager,
)
from app.modules.voice.response import (
    VoiceResponse,
)
from app.modules.voice.tts_manager import (
    voice_tts_manager,
)


class VoiceMultimodalResponse:

    def build(
        self,
        response: VoiceResponse,
        language: str = "pt-BR",
        tts_provider: (
            str | None
        ) = None,
    ):
        tts = None

        if (
            response.speak
            and response.text
        ):
            tts = (
                voice_tts_manager
                .synthesize(
                    text=response.text,
                    language=language,
                    provider_name=(
                        tts_provider
                    ),
                )
            )

        if response.level == "error":
            feedback = (
                voice_feedback_manager
                .error(
                    response.text
                )
            )

        elif (
            response.level
            == "warning"
        ):
            feedback = (
                voice_feedback_manager
                .confirmation_required()
            )

        else:
            feedback = (
                voice_feedback_manager
                .success(
                    response.text
                )
            )

        return {
            "response": (
                response.to_dict()
            ),
            "tts": (
                tts.to_dict()
                if tts
                else None
            ),
            "feedback": (
                feedback.to_dict()
            ),
        }


voice_multimodal_response = (
    VoiceMultimodalResponse()
)
