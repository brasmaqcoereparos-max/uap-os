class AutomationDecision:
    def __init__(
        self,
        name="decision",
    ):
        self.name = str(name)

        self.result = False
        self.last_condition = None

    def evaluate(
        self,
        condition,
        context=None,
    ):
        self.last_condition = condition

        if condition is None:
            self.result = False
            return self.result

        evaluator = getattr(
            condition,
            "evaluate",
            None,
        )

        if callable(evaluator):
            try:
                self.result = bool(
                    evaluator(
                        context or {}
                    )
                )
            except TypeError:
                self.result = bool(
                    evaluator()
                )

            return self.result

        if callable(condition):
            try:
                self.result = bool(
                    condition(
                        context or {}
                    )
                )
            except TypeError:
                self.result = bool(
                    condition()
                )

            return self.result

        self.result = bool(
            condition
        )

        return self.result

    def choose(
        self,
        condition,
        when_true=None,
        when_false=None,
        context=None,
    ):
        result = self.evaluate(
            condition,
            context=context,
        )

        selected = (
            when_true
            if result
            else when_false
        )

        if callable(selected):
            try:
                return selected(
                    context or {}
                )
            except TypeError:
                return selected()

        return selected

    def reset(self):
        self.result = False
        self.last_condition = None

    def to_dict(self):
        return {
            "name": self.name,
            "result": self.result,
        }
