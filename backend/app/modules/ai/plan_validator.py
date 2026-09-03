from app.modules.ai.plan import (
    AIPlan,
)
from app.modules.ai.plan_validation import (
    AIPlanValidationResult,
)


class AIPlanValidator:

    def validate(
        self,
        plan: AIPlan,
    ):
        result = (
            AIPlanValidationResult(
                valid=True
            )
        )

        if not plan.objective.strip():
            result.add_error(
                "Plan objective is empty"
            )

        if not plan.steps:
            result.add_error(
                "Plan has no steps"
            )

            return result

        ids = {
            step.id
            for step
            in plan.steps
        }

        if len(ids) != len(
            plan.steps
        ):
            result.add_error(
                "Duplicate plan step ids"
            )

        for step in plan.steps:
            for dependency in (
                step.depends_on
            ):
                if dependency not in ids:
                    result.add_error(
                        "Unknown dependency: "
                        f"{dependency}"
                    )

                if dependency == step.id:
                    result.add_error(
                        "Step cannot depend "
                        "on itself"
                    )

        return result


ai_plan_validator = (
    AIPlanValidator()
)
