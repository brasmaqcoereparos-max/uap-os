class AutomationDecision:

    def __init__(self):

        self.result = False

    def evaluate(
        self,
        condition,
    ):

        self.result = condition.evaluate()

        return self.result
