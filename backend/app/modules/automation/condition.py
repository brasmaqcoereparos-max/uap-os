"""
Condição universal da automação UAP.

Suporta:
- comparação;
- contexto;
- valores dinâmicos;
- funções;
- variáveis usando $nome.
"""


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

        self.operator = str(
            operator
        )

        self.right = right

        if (
            self.operator
            not in self.OPERATORS
        ):
            raise ValueError(
                f"Operador inválido: "
                f"{self.operator}"
            )

        self.evaluation_count = 0

        self.true_count = 0
        self.false_count = 0

        self.last_result = None
        self.last_error = None

    @staticmethod
    def _resolve(
        value,
        context=None,
    ):
        context = (
            context or {}
        )

        if callable(value):
            try:
                return value(
                    context
                )

            except TypeError:
                return value()

        if (
            isinstance(
                value,
                str,
            )
            and value.startswith("$")
        ):
            key = value[1:]

            current = context

            for part in key.split("."):
                if isinstance(
                    current,
                    dict,
                ):
                    current = current.get(
                        part
                    )
                else:
                    current = getattr(
                        current,
                        part,
                        None,
                    )

                if current is None:
                    break

            return current

        return value

    def evaluate(
        self,
        context=None,
    ):
        self.evaluation_count += 1
        self.last_error = None

        try:
            left = self._resolve(
                self.left,
                context,
            )

            right = self._resolve(
                self.right,
                context,
            )

            if self.operator == "==":
                result = (
                    left == right
                )

            elif self.operator == "!=":
                result = (
                    left != right
                )

            elif self.operator == ">":
                result = (
                    left > right
                )

            elif self.operator == "<":
                result = (
                    left < right
                )

            elif self.operator == ">=":
                result = (
                    left >= right
                )

            elif self.operator == "<=":
                result = (
                    left <= right
                )

            elif self.operator == "in":
                result = (
                    left in right
                )

            elif self.operator == "not_in":
                result = (
                    left not in right
                )

            elif self.operator == "is":
                result = (
                    left is right
                )

            elif self.operator == "is_not":
                result = (
                    left is not right
                )

            elif self.operator == "truthy":
                result = bool(
                    left
                )

            elif self.operator == "falsy":
                result = not bool(
                    left
                )

            else:
                result = False

            result = bool(
                result
            )

            self.last_result = result

            if result:
                self.true_count += 1
            else:
                self.false_count += 1

            return result

        except Exception as exc:
            self.last_result = False
            self.last_error = str(exc)
            self.false_count += 1

            raise

    def reset_statistics(self):
        self.evaluation_count = 0

        self.true_count = 0
        self.false_count = 0

        self.last_result = None
        self.last_error = None

        return True

    def to_dict(self):
        return {
            "left": (
                self.left
                if not callable(
                    self.left
                )
                else "<callable>"
            ),
            "operator": (
                self.operator
            ),
            "right": (
                self.right
                if not callable(
                    self.right
                )
                else "<callable>"
            ),
            "evaluation_count": (
                self.evaluation_count
            ),
            "true_count": (
                self.true_count
            ),
            "false_count": (
                self.false_count
            ),
            "last_result": (
                self.last_result
            ),
            "last_error": (
                self.last_error
            ),
        }
