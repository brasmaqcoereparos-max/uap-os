from app.modules.voice.activation_manager import (
    voice_activation_manager,
)
from app.modules.voice.session_context_manager import (
    voice_session_context_manager,
)
from app.modules.voice.wake_word_manager import (
    voice_wake_word_manager,
)


class VoiceInteractionController:

    def prepare_text(
        self,
        session_id: str,
        text: str,
    ):
        wake = (
            voice_wake_word_manager
            .strip(text)
        )

        if wake[
            "detected"
        ]:
            voice_activation_manager
            .activate(
                session_id
            )

        if not (
            voice_activation_manager
            .is_active(
                session_id
            )
        ):
            return {
                "accepted": False,
                "reason": (
                    "wake_word_required"
                ),
                "text": (
                    wake["text"]
                ),
                "wake_word": (
                    wake[
                        "wake_word"
                    ]
                ),
            }

        context = (
            voice_session_context_manager
            .get_or_create(
                session_id
            )
        )

        context.add_user(
            wake["text"]
        )

        return {
            "accepted": True,
            "reason": None,
            "text": wake["text"],
            "wake_word": (
                wake["wake_word"]
            ),
            "context": (
                context.history()
            ),
        }


voice_interaction_controller = (
    VoiceInteractionController()
      )
