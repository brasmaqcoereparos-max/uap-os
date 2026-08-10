class AutomationAssistant:

    def explain(
        self,
        block,
    ):

        return {
            "name": block.name,
            "description": block.description,
            "inputs": list(block.inputs),
            "outputs": list(block.outputs),
            "parameters": dict(
                block.parameters
            ),
        }

    def suggest_next(
        self,
        block_type,
    ):

        suggestions = {
            "sensor": [
                "condition",
                "timer",
                "motor",
                "relay",
            ],
            "condition": [
                "motor",
                "relay",
                "valve",
                "alarm",
            ],
            "stock": [
                "alarm",
                "notification",
                "replenishment",
            ],
            "measurement": [
                "condition",
                "alarm",
                "stock",
            ],
            "vision": [
                "condition",
                "measurement",
                "stock",
            ],
        }

        return suggestions.get(
            block_type,
            [],
        )


automation_assistant = (
    AutomationAssistant()
          )
