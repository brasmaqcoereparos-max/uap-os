from app.modules.vision.decision.decision_rule import (
    DecisionRule,
)


class DecisionRegistry:

    def __init__(self):
        self._rules = {}

    def register(
        self,
        name,
        conditions,
        actions,
        enabled=True,
        mode="all",
    ):

        rule = DecisionRule(
            name=name,
            conditions=conditions,
            actions=actions,
            enabled=enabled,
            mode=mode,
        )

        self._rules[name] = rule

        return rule

    def add(self, rule):

        if not isinstance(
            rule,
            DecisionRule,
        ):
            raise TypeError(
                "Regra inválida."
            )

        self._rules[
            rule.name
        ] = rule

        return rule

    def get(self, name):
        return self._rules.get(name)

    def remove(self, name):
        return self._rules.pop(
            name,
            None,
        )

    def list(self):
        return list(
            self._rules.values()
        )

    def count(self):
        return len(self._rules)

    def clear(self):
        self._rules.clear()


decision_registry = DecisionRegistry()
