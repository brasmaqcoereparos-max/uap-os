class ExecutionStack:

    def __init__(self):

        self.stack = []

    def push(
        self,
        node_id,
    ):

        self.stack.append(node_id)

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

    def empty(self):

        return len(self.stack) == 0

    def all(self):

        return self.stack.copy()


execution_stack = ExecutionStack()
