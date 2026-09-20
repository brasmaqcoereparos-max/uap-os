import uuid

from app.modules.ai.execution_proposal import (
    AIExecutionProposal,
)
from app.modules.ai.planner import (
    ai_planner,
)
from app.modules.ai.safety_service import (
    ai_safety_service,
)
from app.modules.ai.task import (
    AITask,
)


class AIPlannerService:

    def plan(
        self,
        title: str,
        description: str = "",
        task_type: str = "general",
        parameters: dict | None = None,
    ):
        task = AITask(
            id=str(
                uuid.uuid4()
            ),
            title=title,
            description=description,
            task_type=task_type,
            parameters=dict(
                parameters or {}
            ),
        )

        result = (
            ai_planner.create_plan(
                task
            )
        )

        plan = result[
            "plan"
        ]

        validation = result[
            "validation"
        ]

        proposal = (
            AIExecutionProposal(
                plan=plan,
            )
        )

        proposal_data = (
            proposal.to_dict()
        )

        safety = (
            ai_safety_service.inspect(
                proposal_data
            )
        )

        if not validation.valid:
            proposal.requires_review = True
            proposal.approved = False

        if not safety.accepted:
            proposal.requires_review = True
            proposal.approved = False

        return {
            "task": task.to_dict(),
            "plan": plan.to_dict(),
            "validation": (
                validation.to_dict()
            ),
            "proposal": (
                proposal.to_dict()
            ),
            "safety": (
                safety.to_dict()
            ),
            "ready_for_execution": (
                validation.valid
                and safety.accepted
                and proposal.approved
            ),
        }

    def validate_for_execution(
        self,
        proposal: AIExecutionProposal,
    ):
        if not isinstance(
            proposal,
            AIExecutionProposal,
        ):
            raise TypeError(
                "proposal must be an "
                "AIExecutionProposal"
            )

        validation = (
            ai_planner.create_plan
        )

        safety = (
            ai_safety_service.inspect(
                proposal.to_dict()
            )
        )

        return {
            "approved": (
                proposal.approved
            ),
            "requires_review": (
                proposal.requires_review
            ),
            "safety": (
                safety.to_dict()
            ),
            "allowed": (
                proposal.approved
                and not proposal.requires_review
                and safety.accepted
            ),
        }


ai_planner_service = (
    AIPlannerService()
        )
