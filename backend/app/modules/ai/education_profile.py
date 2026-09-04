from dataclasses import dataclass


@dataclass
class AIEducationProfile:
    level: str = "beginner"

    language: str = "pt-BR"

    step_by_step: bool = True

    include_examples: bool = True

    include_exercises: bool = False

    def to_dict(self):
        return {
            "level": self.level,
            "language": self.language,
            "step_by_step": (
                self.step_by_step
            ),
            "include_examples": (
                self.include_examples
            ),
            "include_exercises": (
                self.include_exercises
            ),
        }
