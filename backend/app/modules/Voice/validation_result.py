from dataclasses import dataclass
from dataclasses import field


@dataclass
class VoiceValidationResult:
    valid: bool

    errors: list[str] = field(
        default_factory=list
    )

    requires_confirmation: (
        bool
    ) = False

    def add_error(
        self,
        message: str,
    ):
        self.errors.append(
            message
        )

        self.valid = False

        return self

    def to_dict(self):
        return {
            "valid": self.valid,
            "errors": list(
                self.errors
            ),
            "requires_confirmation": (
                self.requires_confirmation
            ),
        }
