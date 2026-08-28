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

from app.modules.automation.ai_explanation import (
    ai_explanation,
)


class AISolutionBuilder:
    def build(self, text):
        if not str(
            text or ""
        ).strip():
            return {
                "success": False,
                "errors": [
                    "Automation request "
                    "is empty"
                ],
            }

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

        if not validation["valid"]:
            return {
                "success": False,
                "errors": validation[
                    "errors"
                ],
                "intent": intent,
                "plan": plan,
            }

        graph = ai_graph_builder.build(
            plan
        )

        explanation = (
            ai_explanation.explain(
                intent,
                plan,
            )
        )

        plan.set_explanation(
            explanation["text"]
        )

        return {
            "success": True,
            "intent": intent,
            "plan": plan,
            "graph": graph,
            "explanation": (
                explanation
            ),
        }


ai_solution_builder = (
    AISolutionBuilder()
        )
