from dataclasses import dataclass
from dataclasses import field


@dataclass
class RuntimeGuardResult:
    allowed: bool

    status: str

    reasons: list[str] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "allowed": self.allowed,
            "status": self.status,
            "reasons": list(
                self.reasons
            ),
        }
