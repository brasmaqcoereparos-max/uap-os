from dataclasses import dataclass
from dataclasses import field


@dataclass
class AIEducationResponse:
    title: str

    explanation: str

    steps: list[str] = field(
        default_factory=list
    )

    examples: list[str] = field(
        default_factory=list
    )

    exercises: list[str] = field(
        default_factory=list
    )

    warnings: list[str] = field(
        default_factory=list
    )

    def to_dict(self):
        return {
            "title": self.title,
            "explanation": (
                self.explanation
            ),
            "steps": list(
                self.steps
            ),
            "examples": list(
                self.examples
            ),
            "exercises": list(
                self.exercises
            ),
            "warnings": list(
                self.warnings
            ),
        }
