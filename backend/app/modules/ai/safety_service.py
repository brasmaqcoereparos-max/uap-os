from app.modules.ai.approval_gate import (
    ai_approval_gate,
)
from app.modules.ai.proposal_validator import (
    ai_proposal_validator,
)
from app.modules.ai.safe_result import (
    AISafeResult,
)


class AISafetyService:

    def inspect(
        self,
        data: dict,
    ):
        safety = (
            ai_proposal_validator
            .validate(data)
        )

        gate = (
            ai_approval_gate
            .evaluate(safety)
        )

        return AISafeResult(
            accepted=gate[
                "allowed"
            ],
            status=gate[
                "status"
            ],
            data=dict(data),
            safety=(
                safety.to_dict()
            ),
        )

    def approve(
        self,
        data: dict,
    ):
        safety = (
            ai_proposal_validator
            .validate(data)
        )

        approved = (
            ai_approval_gate
            .approve(safety)
        )

        gate = (
            ai_approval_gate
            .evaluate(safety)
        )

        return AISafeResult(
            accepted=(
                approved
                and gate[
                    "allowed"
                ]
            ),
            status=gate[
                "status"
            ],
            data=dict(data),
            safety=(
                safety.to_dict()
            ),
        )


ai_safety_service = (
    AISafetyService()
)
