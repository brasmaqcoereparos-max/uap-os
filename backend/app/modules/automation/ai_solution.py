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

        intent = automation_parser.parse(
            text
        )

        plan = automation_planner.create_plan(
            intent
        )

        errors = ai_plan_validator.validate(
            intent,
            plan,
        )

        if errors:

            return {
                "success": False,
                "errors": errors,
            }

        graph = ai_graph_builder.build(
            plan
        )

        explanation = ai_explanation.explain(
            intent,
            plan,
        )

        return {
            "success": True,
            "intent": intent,
            "plan": plan,
            "graph": graph,
            "explanation": explanation,
        }


ai_solution_builder = AISolutionBuilder()
