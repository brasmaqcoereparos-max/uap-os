from app.modules.voice.audio_chunk import (
    VoiceAudioChunk,
)


class VoiceAudioBuffer:

    def __init__(self):
        self._chunks: list[
            VoiceAudioChunk
        ] = []

    def append(
        self,
        chunk: VoiceAudioChunk,
    ):
        self._chunks.append(
            chunk
        )

        self._chunks.sort(
            key=lambda item: (
                item.sequence
            )
        )

        return chunk

    def chunks(self):
        return list(
            self._chunks
        )

    def data(self):
        return b"".join(
            chunk.data
            for chunk
            in self._chunks
        )

    def size(self):
        return sum(
            chunk.size
            for chunk
            in self._chunks
        )

    def final(self):
        return any(
            chunk.final
            for chunk
            in self._chunks
        )

    def clear(self):
        self._chunks.clear()

    def snapshot(self):
        return {
            "chunks": len(
                self._chunks
            ),
            "size": self.size(),
            "final": self.final(),
  }
