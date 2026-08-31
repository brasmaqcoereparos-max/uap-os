"""
Motor central de regras da automação UAP.

Responsabilidades:
- registrar regras;
- remover e localizar regras;
- avaliar regras;
- executar regras através do RuleExecutor;
- preservar compatibilidade com regras antigas que possuam evaluate().

Fluxo:

Context
   ↓
AutomationEngine
   ↓
AutomationRule.can_execute()
   ↓
RuleExecutor
   ↓
Actions
"""

from app.modules.automation.rule_executor import (
    rule_executor,
)


class AutomationEngine:

    def __init__(self):
        self.rules = {}

        self.enabled = True

        self.evaluation_count = 0
        self.execution_count = 0

        self.last_results = []

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

        if (
            name in self.rules
            and not replace
        ):
            raise ValueError(
                f"Regra já registrada: {name}"
            )

        self.rules[
            name
        ] = rule

        return rule

    def remove_rule(
        self,
        name,
    ):
        return self.rules.pop(
            str(name),
            None,
        )

    def get_rule(
        self,
        name,
    ):
        return self.rules.get(
            str(name)
        )

    def has_rule(
        self,
        name,
    ):
        return (
            str(name)
            in self.rules
        )

    def list_rules(self):
        return list(
            self.rules.values()
        )

    def clear(self):
        count = len(
            self.rules
        )

        self.rules.clear()
        self.last_results = []

        return count

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False

        return True

    def is_enabled(self):
        return self.enabled

    @staticmethod
    def _can_execute(
        rule,
        context,
    ):
        can_execute = getattr(
            rule,
            "can_execute",
            None,
        )

        if callable(
            can_execute
        ):
            try:
                return bool(
                    can_execute(
                        context
                    )
                )

            except TypeError:
                return bool(
                    can_execute()
                )

        evaluate = getattr(
            rule,
            "evaluate",
            None,
        )

        if callable(
            evaluate
        ):
            try:
                return bool(
                    evaluate(
                        context
                    )
                )

            except TypeError:
                return bool(
                    evaluate()
                )

        return False

    def evaluate(
        self,
        context=None,
    ):
        if not self.enabled:
            return []

        context = dict(
            context or {}
        )

        results = []

        for name, rule in (
            self.rules.items()
        ):
            if not getattr(
                rule,
                "enabled",
                True,
            ):
                continue

            result = (
                self._can_execute(
                    rule,
                    context,
                )
            )

            results.append({
                "rule": name,
                "result": result,
            })

        self.evaluation_count += 1

        self.last_results = results

        return results

    def execute_rule(
        self,
        name,
        device=None,
        context=None,
        stop_on_error=True,
    ):
        if not self.enabled:
            return False

        rule = self.get_rule(
            name
        )

        if rule is None:
            return False

        result = (
            rule_executor.execute(
                rule,
                device=device,
                context=context,
                stop_on_error=(
                    stop_on_error
                ),
            )
        )

        self.execution_count += 1

        return result

    def execute(
        self,
        context=None,
        device=None,
        stop_on_error=True,
    ):
        if not self.enabled:
            return []

        context = dict(
            context or {}
        )

        results = []

        for name, rule in (
            self.rules.items()
        ):
            if not getattr(
                rule,
                "enabled",
                True,
            ):
                continue

            if not self._can_execute(
                rule,
                context,
            ):
                results.append({
                    "rule": name,
                    "executed": False,
                    "result": False,
                })

                continue

            result = (
                rule_executor.execute(
                    rule,
                    device=device,
                    context=context,
                    stop_on_error=(
                        stop_on_error
                    ),
                )
            )

            self.execution_count += 1

            results.append({
                "rule": name,
                "executed": True,
                "result": result,
            })

        self.last_results = results

        return results

    def count(self):
        return len(
            self.rules
        )

    def reset_statistics(self):
        self.evaluation_count = 0
        self.execution_count = 0

        self.last_results = []

        return True

    def to_dict(self):
        return {
            "enabled": self.enabled,
            "count": self.count(),
            "evaluation_count": (
                self.evaluation_count
            ),
            "execution_count": (
                self.execution_count
            ),
            "rules": [
                (
                    rule.to_dict()
                    if hasattr(
                        rule,
                        "to_dict",
                    )
                    else str(rule)
                )
                for rule
                in self.rules.values()
            ],
        }


automation_engine = (
    AutomationEngine()
    )
