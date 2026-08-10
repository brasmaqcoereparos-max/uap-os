class AutomationUndo:

    def __init__(self):

        self.stack = []

    def save(self, state):

        self.stack.append(state)

    def undo(self):

        if not self.stack:
            return None

        return self.stack.pop()

    def clear(self):

        self.stack.clear()


automation_undo = AutomationUndo()
