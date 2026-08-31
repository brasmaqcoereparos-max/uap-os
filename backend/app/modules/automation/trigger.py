"""
Trigger universal da automação UAP.

O trigger representa o evento ou condição que permite
o disparo de uma regra.
"""

import uuid


class AutomationTrigger:

    def __init__(
        self,
        name,
        trigger_type,
        parameters=None,
        trigger_id=None,
        condition=None,
        enabled=True,
        metadata=None,
    ):
        self.trigger_id = (
            str(trigger_id)
            if trigger_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(name)

        self.trigger_type = str(
            trigger_type
        )

        self.parameters = dict(
            parameters or {}
        )

        self.condition = condition

        self.enabled = bool(
            enabled
        )

        self.metadata = dict(
            metadata or {}
        )

        self.activation_count = 0

        self.rejection_count = 0

        self.last_context = None
        self.last_result = None

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

    def remove_parameter(
        self,
        name,
    ):
        return self.parameters.pop(
            str(name),
            None,
        )

    def enable(self):
        self.enabled = True

        return self

    def disable(self):
        self.enabled = False

        return self

    def can_activate(
        self,
        context=None,
    ):
        if not self.enabled:
            self.last_result = False

            return False

        if self.condition is None:
            self.last_result = True

            return True

        evaluator = getattr(
            self.condition,
            "evaluate",
            None,
        )

        if callable(evaluator):
            try:
                result = bool(
                    evaluator(
                        context or {}
                    )
                )

            except TypeError:
                result = bool(
                    evaluator()
                )

        elif callable(
            self.condition
        ):
            try:
                result = bool(
                    self.condition(
                        context or {}
                    )
                )

            except TypeError:
                result = bool(
                    self.condition()
                )

        else:
            result = bool(
                self.condition
            )

        self.last_result = result

        return result

    def activate(
        self,
        context=None,
    ):
        self.last_context = dict(
            context or {}
        )

        if not self.can_activate(
            context=context
        ):
            self.rejection_count += 1

            return False

        self.activation_count += 1

        return True

    def reset(self):
        self.activation_count = 0
        self.rejection_count = 0

        self.last_context = None
        self.last_result = None

        return True

    def to_dict(self):
        return {
            "id": self.trigger_id,
            "name": self.name,
            "type": self.trigger_type,
            "parameters": dict(
                self.parameters
            ),
            "enabled": self.enabled,
            "activation_count": (
                self.activation_count
            ),
            "rejection_count": (
                self.rejection_count
            ),
            "last_result": (
                self.last_result
            ),
            "metadata": dict(
                self.metadata
            ),
            }
