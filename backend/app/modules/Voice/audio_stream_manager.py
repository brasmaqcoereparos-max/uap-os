import uuid

from app.modules.voice.audio_stream import (
    VoiceAudioStream,
)


class VoiceAudioStreamManager:

    def __init__(self):
        self._streams: dict[
            str,
            VoiceAudioStream,
        ] = {}

    def create(self):
        stream = VoiceAudioStream(
            stream_id=str(
                uuid.uuid4()
            )
        )

        self._streams[
            stream.stream_id
        ] = stream

        return stream

    def get(
        self,
        stream_id: str,
    ):
        return self._streams.get(
            stream_id
        )

    def remove(
        self,
        stream_id: str,
    ):
        return self._streams.pop(
            stream_id,
            None,
        )

    def list_all(self):
        return [
            stream.snapshot()
            for stream
            in self._streams.values()
        ]

    def clear(self):
        self._streams.clear()


voice_audio_stream_manager = (
    VoiceAudioStreamManager()
)
