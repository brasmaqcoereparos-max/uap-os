"""
Histórico de ações do circuito visual UAP.
"""


class History:

    def __init__(
        self,
        max_size=500,
    ):
        self.undo_stack = []
        self.redo_stack = []

        self.max_size = int(
            max_size
        )

        if self.max_size <= 0:
            self.max_size = 500

    def push(
        self,
        action,
    ):
        self.undo_stack.append(
            action
        )

        self.redo_stack.clear()

        self._trim()

        return action

    def undo(self):
        if not self.undo_stack:
            return None

        action = (
            self.undo_stack.pop()
        )

        self.redo_stack.append(
            action
        )

        undo_method = getattr(
            action,
            "undo",
            None,
        )

        if callable(undo_method):
            undo_method()

        return action

    def redo(self):
        if not self.redo_stack:
            return None

        action = (
            self.redo_stack.pop()
        )

        self.undo_stack.append(
            action
        )

        redo_method = getattr(
            action,
            "redo",
            None,
        )

        if callable(redo_method):
            redo_method()

        self._trim()

        return action

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

    def undo_count(self):
        return len(
            self.undo_stack
        )

    def redo_count(self):
        return len(
            self.redo_stack
        )

    def last(self):
        if not self.undo_stack:
            return None

        return self.undo_stack[-1]

    def set_max_size(
        self,
        value,
    ):
        value = int(value)

        if value <= 0:
            raise ValueError(
                "max_size deve ser "
                "maior que zero."
            )

        self.max_size = value
        self._trim()

        return self.max_size

    def _trim(self):
        overflow = (
            len(self.undo_stack)
            - self.max_size
        )

        if overflow > 0:
            del self.undo_stack[
                :overflow
            ]

    def to_dict(self):
        return {
            "undo_count": (
                self.undo_count()
            ),
            "redo_count": (
                self.redo_count()
            ),
            "can_undo": (
                self.can_undo()
            ),
            "can_redo": (
                self.can_redo()
            ),
            "max_size": (
                self.max_size
            ),
        }


history = History()
