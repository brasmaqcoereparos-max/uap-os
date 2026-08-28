from copy import deepcopy


class AutomationUndo:
    def __init__(
        self,
        max_states=100,
    ):
        self.undo_stack = []
        self.redo_stack = []

        self.max_states = int(
            max_states
        )

    @property
    def stack(self):
        return self.undo_stack

    def save(self, state):
        self.undo_stack.append(
            deepcopy(state)
        )

        self.redo_stack.clear()

        if (
            self.max_states > 0
            and len(self.undo_stack)
            > self.max_states
        ):
            excess = (
                len(self.undo_stack)
                - self.max_states
            )

            del self.undo_stack[
                :excess
            ]

        return True

    def undo(
        self,
        current_state=None,
    ):
        if not self.undo_stack:
            return None

        if current_state is not None:
            self.redo_stack.append(
                deepcopy(
                    current_state
                )
            )

        return deepcopy(
            self.undo_stack.pop()
        )

    def redo(
        self,
        current_state=None,
    ):
        if not self.redo_stack:
            return None

        if current_state is not None:
            self.undo_stack.append(
                deepcopy(
                    current_state
                )
            )

        return deepcopy(
            self.redo_stack.pop()
        )

    def can_undo(self):
        return bool(
            self.undo_stack
        )

    def can_redo(self):
        return bool(
            self.redo_stack
        )

    def clear(self):
        self.undo_stack.clear()
        self.redo_stack.clear()

    def status(self):
        return {
            "undo_count": len(
                self.undo_stack
            ),
            "redo_count": len(
                self.redo_stack
            ),
            "can_undo": self.can_undo(),
            "can_redo": self.can_redo(),
        }


automation_undo = AutomationUndo()
