class CompilerStack:

    def __init__(self):

        self.stack = []

    def push(
        self,
        value,
    ):

        self.stack.append(value)

    def pop(self):

        if not self.stack:

            return None

        return self.stack.pop()

    def peek(self):

        if not self.stack:

            return None

        return self.stack[-1]

    def size(self):

        return len(self.stack)

    def clear(self):

        self.stack.clear()


compiler_stack = CompilerStack()
