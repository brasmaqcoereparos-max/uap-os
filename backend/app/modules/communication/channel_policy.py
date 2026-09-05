from dataclasses import dataclass
from dataclasses import field

from app.modules.communication.security_level import (
    CommunicationSecurityLevel,
)


@dataclass
class CommunicationChannelPolicy:
    topic: str

    security_level: (
        CommunicationSecurityLevel
    ) = (
        CommunicationSecurityLevel
        .INTERNAL
    )

    allowed_sources: set[str] = field(
        default_factory=set
    )

    allowed_targets: set[str] = field(
        default_factory=set
    )

    require_authentication: bool = True

    enabled: bool = True

    def allows_source(
        self,
        source: str,
    ):
        if not self.allowed_sources:
            return True

        return (
            source
            in self.allowed_sources
        )

    def allows_target(
        self,
        target: str | None,
    ):
        if target is None:
            return True

        if not self.allowed_targets:
            return True

        return (
            target
            in self.allowed_targets
        )

    def to_dict(self):
        return {
            "topic": self.topic,
            "security_level": (
                self.security_level.value
            ),
            "allowed_sources": sorted(
                self.allowed_sources
            ),
            "allowed_targets": sorted(
                self.allowed_targets
            ),
            "require_authentication": (
                self.require_authentication
            ),
            "enabled": self.enabled,
  }
