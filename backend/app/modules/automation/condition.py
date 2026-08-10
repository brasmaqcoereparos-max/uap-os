class AutomationCondition:

    def __init__(
        self,
        left,
        operator,
        right,
    ):

        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):

        if self.operator == "==":
            return self.left == self.right

        if self.operator == "!=":
            return self.left != self.right

        if self.operator == ">":
            return self.left > self.right

        if self.operator == "<":
            return self.left < self.right

        if self.operator == ">=":
            return self.left >= self.right

        if self.operator == "<=":
            return self.left <= self.right

        return False
