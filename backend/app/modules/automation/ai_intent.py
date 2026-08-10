class AutomationIntent:

    def __init__(
        self,
        text="",
    ):

        self.text = text

        self.goal = ""

        self.devices = []

        self.actions = []

        self.conditions = []

        self.parameters = {}

    def set_goal(
        self,
        goal,
    ):

        self.goal = goal

    def add_device(
        self,
        device,
    ):

        self.devices.append(device)

    def add_action(
        self,
        action,
    ):

        self.actions.append(action)

    def add_condition(
        self,
        condition,
    ):

        self.conditions.append(condition)

    def set_parameter(
        self,
        name,
        value,
    ):

        self.parameters[name] = value
