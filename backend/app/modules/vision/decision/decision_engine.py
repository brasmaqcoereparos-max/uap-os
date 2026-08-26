from app.modules.vision.decision.condition_evaluator import (
    condition_evaluator,
)


class DecisionEngine:

    def evaluate_rule(
        self,
        rule,
        analysis,
    ):

        if not rule.enabled:
            return False

        conditions = rule.conditions

        if not conditions:
            return False

        results = [
            condition_evaluator.evaluate(
                condition,
                analysis,
            )
            for condition in conditions
        ]

        mode = str(
            rule.mode
        ).strip().lower()

        if mode == "any":
            return any(results)

        return all(results)

    def evaluate(
        self,
        rules,
        analysis,
    ):

        matched = []

        for rule in rules:

            if self.evaluate_rule(
                rule,
                analysis,
            ):
                matched.append(rule)

        return matched


decision_engine = DecisionEngine()
