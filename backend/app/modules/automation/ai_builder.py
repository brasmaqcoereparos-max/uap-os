from app.modules.automation.ai_parser import (
    automation_parser,
)

from app.modules.automation.ai_planner import (
    automation_planner,
)


class AutomationAIBuilder:

    def build(
        self,
        text,
    ):

        intent = automation_parser.parse(
            text
        )

        plan = automation_planner.create_plan(
            intent
        )

        return {
            "intent": intent,
            "plan": plan,
        }


automation_ai_builder = (
    AutomationAIBuilder()
)
