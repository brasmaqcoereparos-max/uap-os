from app.modules.ai.plan_validator import (
    ai_plan_validator,
)
from app.modules.ai.task import (
    AITask,
)
from app.modules.ai.task_decomposer import (
    ai_task_decomposer,
)


class AIPlanner:

    def create_plan(
        self,
        task: AITask,
    ):
        plan = (
            ai_task_decomposer
            .decompose(task)
        )

        validation = (
            ai_plan_validator
            .validate(plan)
        )

        return {
            "plan": plan,
            "validation": validation,
        }


ai_planner = AIPlanner()
