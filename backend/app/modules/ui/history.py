from copy import deepcopy
from typing import Any


class UIHistory:

    def __init__(
        self,
        limit: int = 100,
    ):
        self.limit = max(
            1,
            int(limit),
        )

        self._undo: list[
            dict[str, Any]
        ] = []

        self._redo: list[
            dict[str, Any]
        ] = []

    def push(
        self,
        snapshot: dict[str, Any],
    ):
        self._undo.append(
            deepcopy(snapshot)
        )

        if len(self._undo) > self.limit:
            self._undo.pop(0)

        self._redo.clear()

    def undo(
        self,
        current: dict[str, Any],
    ):
        if not self._undo:
            return None

        self._redo.append(
            deepcopy(current)
        )

        return self._undo.pop()

    def redo(
        self,
        current: dict[str, Any],
    ):
        if not self._redo:
            return None

        self._undo.append(
            deepcopy(current)
        )

        return self._redo.pop()

    def clear(self):
        self._undo.clear()
        self._redo.clear()

    def can_undo(self):
        return bool(self._undo)

    def can_redo(self):
        return bool(self._redo)


ui_history = UIHistory()
