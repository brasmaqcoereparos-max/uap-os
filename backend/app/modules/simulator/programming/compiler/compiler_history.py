class CompilerHistory:

    def __init__(self):

        self.history = []

        self.limit = 100

    def add(self, session):

        self.history.append(session)

        if len(self.history) > self.limit:

            self.history.pop(0)

    def last(self):

        if not self.history:

            return None

        return self.history[-1]

    def all(self):

        return self.history.copy()

    def clear(self):

        self.history.clear()


compiler_history = CompilerHistory()
