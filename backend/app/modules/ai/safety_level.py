from enum import Enum


class AISafetyLevel(
    str,
    Enum,
):
    SAFE = "safe"
    REQUIRES_REVIEW = (
        "requires_review"
    )
    BLOCKED = "blocked"
