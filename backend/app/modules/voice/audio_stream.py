from app.modules.voice.audio_buffer import (
    VoiceAudioBuffer,
)
from app.modules.voice.audio_chunk import (
    VoiceAudioChunk,
)


class VoiceAudioStream:

    def __init__(
        self,
        stream_id: str,
    ):
        self.stream_id = stream_id

        self.buffer = (
            VoiceAudioBuffer()
        )

        self.closed = False

    def write(
        self,
        chunk: VoiceAudioChunk,
    ):
        if self.closed:
            raise RuntimeError(
                "Voice audio stream "
                "is closed"
            )

        self.buffer.append(
            chunk
        )

        if chunk.final:
            self.closed = True

        return chunk

    def close(self):
        self.closed = True

        return self

    def snapshot(self):
        return {
            "stream_id": (
                self.stream_id
            ),
            "closed": self.closed,
            "buffer": (
                self.buffer.snapshot()
            ),
        }
