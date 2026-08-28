class AutomationCondition:
    OPERATORS = {
        "==",
        "!=",
        ">",
        "<",
        ">=",
        "<=",
        "in",
        "not_in",
        "is",
        "is_not",
        "truthy",
        "falsy",
    }

    def __init__(
        self,
        left=None,
        operator="==",
        right=None,
    ):
        self.left = left
        self.operator = str(operator)
        self.right = right

        if self.operator not in self.OPERATORS:
            raise ValueError(
                f"Operador inválido: {self.operator}"
            )

    @staticmethod
    def _resolve(value, context=None):
        if callable(value):
            try:
                return value(context or {})
            except TypeError:
                return value()

        if (
            isinstance(value, str)
            and value.startswith("$")
            and context is not None
        ):
            key = value[1:]
            return context.get(key)

        return value

    def evaluate(self, context=None):
        left = self._resolve(
            self.left,
            context,
        )

        right = self._resolve(
            self.right,
            context,
        )

        if self.operator == "==":
            return left == right

        if self.operator == "!=":
            return left != right

        if self.operator == ">":
            return left > right

        if self.operator == "<":
            return left < right

        if self.operator == ">=":
            return left >= right

        if self.operator == "<=":
            return left <= right

        if self.operator == "in":
            return left in right

        if self.operator == "not_in":
            return left not in right

        if self.operator == "is":
            return left is right

        if self.operator == "is_not":
            return left is not right

        if self.operator == "truthy":
            return bool(left)

        if self.operator == "falsy":
            return not bool(left)

        return False

    def to_dict(self):
        return {
            "left": self.left
            if not callable(self.left)
            else "<callable>",
            "operator": self.operator,
            "right": self.right
            if not callable(self.right)
            else "<callable>",
        }
