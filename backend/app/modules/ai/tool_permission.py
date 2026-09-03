from dataclasses import dataclass
from dataclasses import field


@dataclass
class AIToolPermission:
    tool: str

    allowed_sources: set[str] = field(
        default_factory=lambda: {
            "ai",
        }
    )

    allow_execution: bool = True

    requires_review: bool = True

    def allows(
        self,
        source: str,
    ):
        return (
            self.allow_execution
            and source
            in self.allowed_sources
        )

    def to_dict(self):
        return {
            "tool": self.tool,
            "allowed_sources": sorted(
                self.allowed_sources
            ),
            "allow_execution": (
                self.allow_execution
            ),
            "requires_review": (
                self.requires_review
            ),
        }
