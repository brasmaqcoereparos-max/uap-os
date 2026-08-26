from app.modules.vision.vision_decision import (
    vision_decision,
)


class VisionRules:

    def __init__(self):
        self._rules = {}

    def add(
        self,
        name,
        condition,
        action,
        data=None,
    ):

        rule = {
            "name": name,
            "condition": condition,
            "action": action,
            "data": data,
        }

        self._rules[name] = rule

        return rule

    def remove(self, name):
        return self._rules.pop(
            name,
            None,
        )

    def get(self, name):
        return self._rules.get(name)

    def list(self):
        return dict(self._rules)

    def clear(self):
        self._rules.clear()

    def evaluate(self, analysis):

        return vision_decision.evaluate(
            analysis,
            list(self._rules.values()),
        )


vision_rules = VisionRules()
