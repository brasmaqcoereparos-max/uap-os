from app.modules.voice.feedback import (
    VoiceFeedback,
)


class VoiceFeedbackManager:

    def listening(self):
        return VoiceFeedback(
            feedback_type="listening",
            message="Ouvindo",
            tone="listen",
        )

    def processing(self):
        return VoiceFeedback(
            feedback_type="processing",
            message="Processando",
            tone="processing",
        )

    def success(
        self,
        message: str = "Concluído",
    ):
        return VoiceFeedback(
            feedback_type="success",
            message=message,
            tone="success",
        )

    def error(
        self,
        message: str,
    ):
        return VoiceFeedback(
            feedback_type="error",
            message=message,
            tone="error",
        )

    def confirmation_required(self):
        return VoiceFeedback(
            feedback_type=(
                "confirmation_required"
            ),
            message=(
                "Confirme para continuar"
            ),
            tone="confirmation",
        )


voice_feedback_manager = (
    VoiceFeedbackManager()
)
