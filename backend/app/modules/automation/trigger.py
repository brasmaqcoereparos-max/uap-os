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

        self.enabled = bool(enabled)

        self.metadata = dict(
            metadata or {}
        )

        self.activation_count = 0

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
            return False

        if self.condition is None:
            return True

        evaluator = getattr(
            self.condition,
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

        if callable(
            self.condition
        ):
            try:
                return bool(
                    self.condition(
                        context or {}
                    )
                )
            except TypeError:
                return bool(
                    self.condition()
                )

        return bool(
            self.condition
        )

    def activate(
        self,
        context=None,
    ):
        if not self.can_activate(
            context=context
        ):
            return False

        self.activation_count += 1

        return True

    def reset(self):
        self.activation_count = 0

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
            "metadata": dict(
                self.metadata
            ),
        }
