class AutomationEngine:
    def __init__(self):
        self.rules = {}
        self.enabled = True

    def add_rule(
        self,
        rule,
        replace=True,
    ):
        name = getattr(
            rule,
            "name",
            None,
        )

        if not name:
            raise ValueError(
                "A regra precisa possuir um nome."
            )

        name = str(name)

        if name in self.rules and not replace:
            raise ValueError(
                f"Regra já registrada: {name}"
            )

        self.rules[name] = rule

        return rule

    def remove_rule(self, name):
        return self.rules.pop(
            str(name),
            None,
        )

    def get_rule(self, name):
        return self.rules.get(
            str(name)
        )

    def has_rule(self, name):
        return str(name) in self.rules

    def list_rules(self):
        return list(
            self.rules.values()
        )

    def clear(self):
        self.rules.clear()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def evaluate(
        self,
        context=None,
    ):
        if not self.enabled:
            return []

        context = dict(context or {})
        results = []

        for name, rule in self.rules.items():
            if not getattr(
                rule,
                "enabled",
                True,
            ):
                continue

            evaluate = getattr(
                rule,
                "evaluate",
                None,
            )

            if not callable(evaluate):
                continue

            try:
                result = evaluate(context)
            except TypeError:
                result = evaluate()

            results.append({
                "rule": name,
                "result": result,
            })

        return results

    def count(self):
        return len(self.rules)

    def to_dict(self):
        return {
            "enabled": self.enabled,
            "count": self.count(),
            "rules": [
                (
                    rule.to_dict()
                    if hasattr(rule, "to_dict")
                    else str(rule)
                )
                for rule in self.rules.values()
            ],
        }


automation_engine = AutomationEngine()
