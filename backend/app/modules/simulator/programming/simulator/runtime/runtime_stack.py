class RuntimeStack:

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

    def clear(self):

        self.stack.clear()

    def size(self):

        return len(self.stack)


runtime_stack = RuntimeStack()
