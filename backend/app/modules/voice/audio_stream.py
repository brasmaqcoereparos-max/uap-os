from __future__ import annotations

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

        self._sample_rate: (
            int | None
        ) = None

        self._channels: (
            int | None
        ) = None

        self._sample_width: (
            int | None
        ) = None

        self._last_sequence: (
            int | None
        ) = None

    def _validate_chunk(
        self,
        chunk: VoiceAudioChunk,
    ) -> None:
        if chunk.sample_rate <= 0:
            raise ValueError(
                "sample_rate must be "
                "greater than zero"
            )

        if chunk.channels <= 0:
            raise ValueError(
                "channels must be "
                "greater than zero"
            )

        if chunk.sample_width <= 0:
            raise ValueError(
                "sample_width must be "
                "greater than zero"
            )

        if chunk.sequence < 0:
            raise ValueError(
                "sequence cannot be negative"
            )

        if (
            self._last_sequence is not None
            and chunk.sequence
            <= self._last_sequence
        ):
            raise ValueError(
                "Audio chunk sequence must "
                "increase monotonically"
            )

        if self._sample_rate is None:
            return

        if (
            chunk.sample_rate
            != self._sample_rate
        ):
            raise ValueError(
                "Audio sample_rate changed "
                "inside the same stream"
            )

        if (
            chunk.channels
            != self._channels
        ):
            raise ValueError(
                "Audio channel count changed "
                "inside the same stream"
            )

        if (
            chunk.sample_width
            != self._sample_width
        ):
            raise ValueError(
                "Audio sample_width changed "
                "inside the same stream"
            )

    def write(
        self,
        chunk: VoiceAudioChunk,
    ):
        if self.closed:
            raise RuntimeError(
                "Voice audio stream "
                "is closed"
            )

        self._validate_chunk(
            chunk
        )

        if self._sample_rate is None:
            self._sample_rate = (
                chunk.sample_rate
            )

            self._channels = (
                chunk.channels
            )

            self._sample_width = (
                chunk.sample_width
            )

        self._last_sequence = (
            chunk.sequence
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

    def audio_format(self):
        return {
            "sample_rate": (
                self._sample_rate
            ),
            "channels": (
                self._channels
            ),
            "sample_width": (
                self._sample_width
            ),
        }

    def snapshot(self):
        return {
            "stream_id": (
                self.stream_id
            ),
            "closed": self.closed,
            "audio_format": (
                self.audio_format()
            ),
            "last_sequence": (
                self._last_sequence
            ),
            "buffer": (
                self.buffer.snapshot()
            ),
        }
