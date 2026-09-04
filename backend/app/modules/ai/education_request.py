from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ai.education_profile import (
    AIEducationProfile,
)


@dataclass
class AIEducationRequest:
    topic: str

    question: str = ""

    profile: AIEducationProfile = field(
        default_factory=(
            AIEducationProfile
        )
    )

    context: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "topic": self.topic,
            "question": self.question,
            "profile": (
                self.profile.to_dict()
            ),
            "context": dict(
                self.context
            ),
              }
