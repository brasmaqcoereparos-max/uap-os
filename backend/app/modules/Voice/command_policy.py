from dataclasses import dataclass
from dataclasses import field


@dataclass
class VoiceCommandPolicy:
    command: str

    enabled: bool = True
    requires_confirmation: bool = False

    allowed_sources: set[str] = field(
        default_factory=lambda: {
            "voice",
        }
    )

    def allows_source(
        self,
        source: str,
    ):
        return source in self.allowed_sources

    def to_dict(self):
        return {
            "command": self.command,
            "enabled": self.enabled,
            "requires_confirmation": (
                self.requires_confirmation
            ),
            "allowed_sources": sorted(
                self.allowed_sources
            ),
        }
