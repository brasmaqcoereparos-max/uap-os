class AutomationEngine:

    def __init__(self):

        self.rules = {}

    def add_rule(
        self,
        rule,
    ):

        self.rules[rule.name] = rule

    def remove_rule(
        self,
        name,
    ):

        self.rules.pop(
            name,
            None,
        )

    def get_rule(
        self,
        name,
    ):

        return self.rules.get(name)

    def list_rules(self):

        return list(
            self.rules.values()
        )


automation_engine = AutomationEngine()
