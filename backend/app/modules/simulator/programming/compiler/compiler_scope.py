
class CompilerScope:

    def __init__(self):

        self.stack = [{}]

    def push(self):

        self.stack.append({})

    def pop(self):

        if len(self.stack) > 1:

            self.stack.pop()

    def set(
        self,
        name,
        value,
    ):

        self.stack[-1][name] = value

    def get(
        self,
        name,
        default=None,
    ):

        for scope in reversed(self.stack):

            if name in scope:

                return scope[name]

        return default

    def clear(self):

        self.stack = [{}]


compiler_scope = CompilerScope()
