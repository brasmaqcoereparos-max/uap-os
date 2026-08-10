from app.modules.automation.ai_intent import (
    AutomationIntent,
)


class AutomationParser:

    def parse(
        self,
        text,
    ):

        intent = AutomationIntent(text)

        normalized = text.lower()

        if "estoque" in normalized:
            intent.set_goal("stock")

        elif "motor" in normalized:
            intent.set_goal("motor")

        elif "sensor" in normalized:
            intent.set_goal("sensor")

        elif "robô" in normalized:
            intent.set_goal("robot")

        elif "medir" in normalized:
            intent.set_goal("measurement")

        elif "câmera" in normalized:
            intent.set_goal("vision")

        else:
            intent.set_goal("general")

        return intent


automation_parser = AutomationParser()
