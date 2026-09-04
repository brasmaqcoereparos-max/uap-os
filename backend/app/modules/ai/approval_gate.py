from app.modules.ai.safety_level import (
    AISafetyLevel,
)
from app.modules.ai.safety_result import (
    AISafetyResult,
)


class AIApprovalGate:

    def evaluate(
        self,
        result: AISafetyResult,
    ):
        if (
            result.level
            == AISafetyLevel.BLOCKED
        ):
            return {
                "allowed": False,
                "status": "blocked",
            }

        if (
            result.level
            == AISafetyLevel
            .REQUIRES_REVIEW
            and not result.approved
        ):
            return {
                "allowed": False,
                "status": (
                    "review_required"
                ),
            }

        return {
            "allowed": True,
            "status": "approved",
        }

    def approve(
        self,
        result: AISafetyResult,
    ):
        if (
            result.level
            == AISafetyLevel.BLOCKED
        ):
            return False

        result.approved = True

        return True


ai_approval_gate = (
    AIApprovalGate()
)
