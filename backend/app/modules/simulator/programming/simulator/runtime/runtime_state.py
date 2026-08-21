"""
Estado global do runtime UAP.
"""


class RuntimeState:

    def __init__(self):

        self.running = False
        self.paused = False
        self.error = None
        self.variables = {}

    def start(self):

        self.running = True
        self.paused = False
        self.error = None

    def stop(self):

        self.running = False
        self.paused = False

    def pause(self):

        if self.running:
            self.paused = True

    def resume(self):

        if self.running:
            self.paused = False

    def set_error(
        self,
        error,
    ):

        self.error = str(error)

    def clear_error(self):

        self.error = None

    def set(
        self,
        name,
        value,
    ):

        self.variables[name] = value

    def get(
        self,
        name,
        default=None,
    ):

        return self.variables.get(
            name,
            default,
        )

    def delete(
        self,
        name,
    ):

        self.variables.pop(
            name,
            None,
        )

    def clear_variables(self):

        self.variables.clear()

    def reset(self):

        self.running = False
        self.paused = False
        self.error = None
        self.variables.clear()


runtime_state = RuntimeState()
