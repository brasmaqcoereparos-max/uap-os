"""
Regra universal de automação UAP.

Fluxo:

Trigger(s)
    ↓
Condition(s)
    ↓
Action(s)
"""

import uuid


class AutomationRule:

    def __init__(
        self,
        name,
        rule_id=None,
        description="",
        enabled=True,
        metadata=None,
    ):
        self.rule_id = (
            str(rule_id)
            if rule_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(
            name
        )

        self.description = str(
            description
        )

        self.triggers = []
        self.conditions = []
        self.actions = []

        self.enabled = bool(
            enabled
        )

        self.metadata = dict(
            metadata or {}
        )

        self.execution_count = 0
        self.last_result = None

        self.evaluation_count = 0
        self.rejected_count = 0

    def add_trigger(
        self,
        trigger,
    ):
        self.triggers.append(
            trigger
        )

        return trigger

    def add_condition(
        self,
        condition,
    ):
        self.conditions.append(
            condition
        )

        return condition

    def add_action(
        self,
        action,
    ):
        self.actions.append(
            action
        )

        return action

    def remove_trigger(
        self,
        trigger,
    ):
        try:
            self.triggers.remove(
                trigger
            )

            return True

        except ValueError:
            return False

    def remove_condition(
        self,
        condition,
    ):
        try:
            self.conditions.remove(
                condition
            )

            return True

        except ValueError:
            return False

    def remove_action(
        self,
        action,
    ):
        try:
            self.actions.remove(
                action
            )

            return True

        except ValueError:
            return False

    @staticmethod
    def _evaluate_item(
        item,
        context=None,
    ):
        evaluator = getattr(
            item,
            "evaluate",
            None,
        )

        if callable(evaluator):
            try:
                return bool(
                    evaluator(
                        context or {}
                    )
                )

            except TypeError:
                return bool(
                    evaluator()
                )

        if callable(item):
            try:
                return bool(
                    item(
                        context or {}
                    )
                )

            except TypeError:
                return bool(
                    item()
                )

        return bool(
            item
        )

    def triggers_met(
        self,
        context=None,
    ):
        if not self.triggers:
            return True

        for trigger in self.triggers:
            checker = getattr(
                trigger,
                "can_activate",
                None,
            )

            if callable(checker):
                try:
                    result = checker(
                        context=context
                    )

                except TypeError:
                    result = checker()

                if not result:
                    return False

            elif not self._evaluate_item(
                trigger,
                context,
            ):
                return False

        return True

    def conditions_met(
        self,
        context=None,
    ):
        return all(
            self._evaluate_item(
                condition,
                context,
            )
            for condition
            in self.conditions
        )

    def can_execute(
        self,
        context=None,
    ):
        self.evaluation_count += 1

        result = (
            self.enabled
            and self.triggers_met(
                context
            )
            and self.conditions_met(
                context
            )
        )

        if not result:
            self.rejected_count += 1

        return result

    def enable(self):
        self.enabled = True

        return self

    def disable(self):
        self.enabled = False

        return self

    def reset_statistics(self):
        self.execution_count = 0

        self.evaluation_count = 0
        self.rejected_count = 0

        self.last_result = None

        return True

    def to_dict(self):

        def serialize(item):
            method = getattr(
                item,
                "to_dict",
                None,
            )

            if callable(method):
                return method()

            return str(
                item
            )

        return {
            "id": self.rule_id,
            "name": self.name,
            "description": (
                self.description
            ),
            "enabled": self.enabled,
            "triggers": [
                serialize(item)
                for item
                in self.triggers
            ],
            "conditions": [
                serialize(item)
                for item
                in self.conditions
            ],
            "actions": [
                serialize(item)
                for item
                in self.actions
            ],
            "execution_count": (
                self.execution_count
            ),
            "evaluation_count": (
                self.evaluation_count
            ),
            "rejected_count": (
                self.rejected_count
            ),
            "last_result": (
                self.last_result
            ),
            "metadata": dict(
                self.metadata
            ),
        }
