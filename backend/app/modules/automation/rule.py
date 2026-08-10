class AutomationRule:

    def __init__(
        self,
        name,
    ):

        self.name = name

        self.triggers = []

        self.conditions = []

        self.actions = []

    def add_trigger(
        self,
        trigger,
    ):

        self.triggers.append(trigger)

    def add_condition(
        self,
        condition,
    ):

        self.conditions.append(condition)

    def add_action(
        self,
        action,
    ):

        self.actions.append(action)

    def conditions_met(self):

        return all(
            condition.evaluate()
            for condition in self.conditions
            )
class AutomationRule:

    def __init__(
        self,
        name,
    ):

        self.name = name

        self.triggers = []

        self.conditions = []

        self.actions = []

    def add_trigger(
        self,
        trigger,
    ):

        self.triggers.append(trigger)

    def add_condition(
        self,
        condition,
    ):

        self.conditions.append(condition)

    def add_action(
        self,
        action,
    ):

        self.actions.append(action)

    def conditions_met(self):

        return all(
            condition.evaluate()
            for condition in self.conditions
            )
