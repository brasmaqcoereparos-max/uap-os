from app.modules.voice.activation_manager import (
    voice_activation_manager,
)
from app.modules.voice.audio_stream_manager import (
    voice_audio_stream_manager,
)
from app.modules.voice.confirmation_manager import (
    voice_confirmation_manager,
)
from app.modules.voice.recognizer_manager import (
    voice_recognizer_manager,
)
from app.modules.voice.service import (
    voice_service,
)
from app.modules.voice.tts_manager import (
    voice_tts_manager,
)


class VoiceHealth:

    def check(self):
        return {
            "healthy": True,
            "sessions": len(
                voice_service.sessions()
            ),
            "audio_streams": len(
                voice_audio_stream_manager
                .list_all()
            ),
            "pending_confirmations": len(
                voice_confirmation_manager
                .pending()
            ),
            "recognizers": (
                voice_recognizer_manager
                .recognizers()
            ),
            "tts_providers": (
                voice_tts_manager
                .providers()
            ),
            "activation_timeout_seconds": (
                voice_activation_manager
                .timeout_seconds
            ),
        }


voice_health = VoiceHealth()
