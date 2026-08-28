from app.modules.automation.ai_parser import (
    automation_parser,
)

from app.modules.automation.ai_planner import (
    automation_planner,
)

from app.modules.automation.ai_validator import (
    ai_plan_validator,
)

from app.modules.automation.ai_graph_builder import (
    ai_graph_builder,
)


class AutomationAIBuilder:
    def build(
        self,
        text,
        include_graph=True,
    ):
        intent = automation_parser.parse(
            text
        )

        plan = (
            automation_planner.create_plan(
                intent
            )
        )

        validation = (
            ai_plan_validator.report(
                intent,
                plan,
            )
        )

        result = {
            "success": validation[
                "valid"
            ],
            "intent": intent,
            "plan": plan,
            "errors": validation[
                "errors"
            ],
        }

        if (
            include_graph
            and validation["valid"]
        ):
            result["graph"] = (
                ai_graph_builder.build(
                    plan
                )
            )

        return result


automation_ai_builder = (
    AutomationAIBuilder()
        )
