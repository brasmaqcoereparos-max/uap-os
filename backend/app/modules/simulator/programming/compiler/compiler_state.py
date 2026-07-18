class CompilerState:

    def __init__(self):

        self.state = {}

    def set(

        self,

        key,

        value,

    ):

        self.state[key] = value

    def get(

        self,

        key,

        default=None,

    ):

        return self.state.get(

            key,

            default,

        )

    def remove(

        self,

        key,

    ):

        self.state.pop(

            key,

            None,

        )

    def clear(self):

        self.state.clear()

    def all(self):

        return self.state.copy()


compiler_state = CompilerState()
