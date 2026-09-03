import uuid

from app.modules.ai.execution_proposal import (
    AIExecutionProposal,
)
from app.modules.ai.planner import (
    ai_planner,
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
            id=str(uuid.uuid4()),
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

        proposal = (
            AIExecutionProposal(
                plan=result["plan"],
            )
        )

        return {
            "task": task.to_dict(),
            "plan": (
                result["plan"]
                .to_dict()
            ),
            "validation": (
                result["validation"]
                .to_dict()
            ),
            "proposal": (
                proposal.to_dict()
            ),
        }


ai_planner_service = (
    AIPlannerService()
)
