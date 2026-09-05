from dataclasses import dataclass
from dataclasses import field


@dataclass
class CommunicationMessageValidation:
    valid: bool

    errors: list[str] = field(
        default_factory=list
    )

    warnings: list[str] = field(
        default_factory=list
    )

    def add_error(
        self,
        message: str,
    ):
        self.errors.append(
            message
        )

        self.valid = False

        return self

    def add_warning(
        self,
        message: str,
    ):
        self.warnings.append(
            message
        )

        return self

    def to_dict(self):
        return {
            "valid": self.valid,
            "errors": list(
                self.errors
            ),
            "warnings": list(
                self.warnings
            ),
        }
