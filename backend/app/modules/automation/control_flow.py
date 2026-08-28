from enum import Enum


class ControlFlow(
    str,
    Enum,
):
    SEQUENCE = "sequence"
    CONDITION = "condition"
    LOOP = "loop"
    PARALLEL = "parallel"
    WAIT = "wait"
    EVENT = "event"
    STOP = "stop"

    @classmethod
    def normalize(cls, value):
        if isinstance(value, cls):
            return value

        text = str(value).strip().lower()

        for item in cls:
            if item.value == text:
                return item

        raise ValueError(
            f"Fluxo de controle inválido: {value}"
        )


class ControlFlowNode:
    def __init__(
        self,
        flow_type,
        name="",
        condition=None,
        metadata=None,
    ):
        self.flow_type = (
            ControlFlow.normalize(
                flow_type
            )
        )

        self.name = str(name)

        self.condition = condition

        self.children = []

        self.metadata = dict(
            metadata or {}
        )

        self.enabled = True

    def add(self, node):
        self.children.append(node)
        return node

    def remove(self, node):
        try:
            self.children.remove(node)
            return True
        except ValueError:
            return False

    def clear(self):
        self.children.clear()

    def should_execute(
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
                    evaluator(context)
                )
            except TypeError:
                return bool(
                    evaluator()
                )

        if callable(self.condition):
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

    def to_dict(self):
        return {
            "flow_type": (
                self.flow_type.value
            ),
            "name": self.name,
            "enabled": self.enabled,
            "children": [
                child.to_dict()
                if hasattr(
                    child,
                    "to_dict",
                )
                else str(child)
                for child in self.children
            ],
            "metadata": dict(
                self.metadata
            ),
        }
