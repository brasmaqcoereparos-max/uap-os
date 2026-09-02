from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceAudioChunk:
    data: bytes

    sample_rate: int = 16000
    channels: int = 1
    sample_width: int = 2

    sequence: int = 0
    final: bool = False

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    @property
    def size(self):
        return len(self.data)

    def to_dict(self):
        return {
            "size": self.size,
            "sample_rate": (
                self.sample_rate
            ),
            "channels": self.channels,
            "sample_width": (
                self.sample_width
            ),
            "sequence": self.sequence,
            "final": self.final,
            "metadata": dict(
                self.metadata
            ),
              }
