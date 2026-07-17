class ExecutionSignal:

    def __init__(self):

        self.signals = {}

    def set(
        self,
        name,
        value,
    ):

        self.signals[name] = value

    def get(
        self,
        name,
        default=False,
    ):

        return self.signals.get(
            name,
            default,
        )

    def toggle(
        self,
        name,
    ):

        self.signals[name] = not self.get(name)

    def clear(self):

        self.signals.clear()

    def all(self):

        return self.signals.copy()


execution_signal = ExecutionSignal()
