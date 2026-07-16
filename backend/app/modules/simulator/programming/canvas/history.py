
class CanvasHistory:

    def __init__(self):

        self.undo_stack = []

        self.redo_stack = []

    def save(self, state):

        self.undo_stack.append(state)

        self.redo_stack.clear()

    def undo(self):

        if not self.undo_stack:
            return None

        return self.undo_stack.pop()

    def redo(self):

        if not self.redo_stack:
            return None

        return self.redo_stack.pop()


history = CanvasHistory()
