class AutomationPlan:
    def __init__(
        self,
        goal="",
        metadata=None,
    ):
        self.goal = str(goal or "")

        self.steps = []
        self.blocks = []
        self.connections = []

        self.explanation = ""

        self.metadata = dict(
            metadata or {}
        )

    def add_step(
        self,
        step,
        metadata=None,
    ):
        if isinstance(step, dict):
            item = dict(step)

            if "name" not in item:
                item["name"] = str(
                    item.get(
                        "description",
                        "Etapa",
                    )
                )

        else:
            item = {
                "name": str(step),
                "description": str(step),
                "metadata": dict(
                    metadata or {}
                ),
            }

        self.steps.append(item)

        return item

    def add_block(self, block):
        self.blocks.append(block)
        return block

    def add_connection(
        self,
        connection,
    ):
        self.connections.append(
            connection
        )

        return connection

    def set_explanation(
        self,
        explanation,
    ):
        self.explanation = str(
            explanation or ""
        )

        return self.explanation

    def clear(self):
        self.steps.clear()
        self.blocks.clear()
        self.connections.clear()

    def step_count(self):
        return len(self.steps)

    def to_dict(self):
        def serialize(value):
            method = getattr(
                value,
                "to_dict",
                None,
            )

            if callable(method):
                return method()

            return value

        return {
            "goal": self.goal,
            "steps": [
                serialize(item)
                for item in self.steps
            ],
            "blocks": [
                serialize(item)
                for item in self.blocks
            ],
            "connections": [
                serialize(item)
                for item
                in self.connections
            ],
            "explanation": (
                self.explanation
            ),
            "metadata": dict(
                self.metadata
            ),
            }
