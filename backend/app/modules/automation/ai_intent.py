class AutomationIntent:
    def __init__(
        self,
        text="",
        goal="",
        metadata=None,
    ):
        self.text = str(text or "")
        self.goal = str(goal or "")

        self.devices = []
        self.actions = []
        self.conditions = []
        self.parameters = {}

        self.metadata = dict(
            metadata or {}
        )

    def set_goal(self, goal):
        self.goal = str(goal or "")
        return self.goal

    def add_device(self, device):
        if device not in self.devices:
            self.devices.append(device)

        return device

    def add_action(self, action):
        self.actions.append(action)
        return action

    def add_condition(self, condition):
        self.conditions.append(condition)
        return condition

    def set_parameter(
        self,
        name,
        value,
    ):
        self.parameters[
            str(name)
        ] = value

        return value

    def get_parameter(
        self,
        name,
        default=None,
    ):
        return self.parameters.get(
            str(name),
            default,
        )

    def has_goal(self):
        return bool(
            self.goal.strip()
        )

    def is_goal(self, goal):
        return (
            self.goal.strip().lower()
            == str(goal).strip().lower()
        )

    def to_dict(self):
        return {
            "text": self.text,
            "goal": self.goal,
            "devices": list(
                self.devices
            ),
            "actions": list(
                self.actions
            ),
            "conditions": list(
                self.conditions
            ),
            "parameters": dict(
                self.parameters
            ),
            "metadata": dict(
                self.metadata
            ),
        }
