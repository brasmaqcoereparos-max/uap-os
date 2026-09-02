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


class VoiceStatus:

    def snapshot(self):
        return {
            "service": "voice",
            "status": "ok",
            "sessions": len(
                voice_service.sessions()
            ),
            "streams": len(
                voice_audio_stream_manager
                .list_all()
            ),
            "pending_confirmations": (
                len(
                    voice_confirmation_manager
                    .pending()
                )
            ),
            "recognizers": (
                voice_recognizer_manager
                .recognizers()
            ),
        }


voice_status = VoiceStatus()
