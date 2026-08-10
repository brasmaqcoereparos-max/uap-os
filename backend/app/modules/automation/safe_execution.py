class SafeExecution:

    def __init__(self):

        self.enabled = True

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def can_execute(
        self,
        approved=False,
    ):

        return (
            self.enabled
            and approved
        )


safe_execution = SafeExecution()
