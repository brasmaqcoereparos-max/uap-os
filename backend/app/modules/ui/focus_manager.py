class UIFocusManager:

    def __init__(self):
        self._focused_id: (
            str | None
        ) = None

        self._order: list[
            str
        ] = []

    @property
    def focused_id(self):
        return self._focused_id

    def set_order(
        self,
        widget_ids: list[str],
    ):
        self._order = list(
            dict.fromkeys(
                widget_ids
            )
        )

        if (
            self._focused_id
            not in self._order
        ):
            self._focused_id = None

        return list(self._order)

    def focus(
        self,
        widget_id: str,
    ):
        if (
            self._order
            and widget_id
            not in self._order
        ):
            return False

        self._focused_id = (
            widget_id
        )

        return True

    def clear(self):
        self._focused_id = None

    def next(self):
        if not self._order:
            return None

        if (
            self._focused_id
            not in self._order
        ):
            self._focused_id = (
                self._order[0]
            )

            return self._focused_id

        index = self._order.index(
            self._focused_id
        )

        index = (
            index + 1
        ) % len(self._order)

        self._focused_id = (
            self._order[index]
        )

        return self._focused_id

    def previous(self):
        if not self._order:
            return None

        if (
            self._focused_id
            not in self._order
        ):
            self._focused_id = (
                self._order[-1]
            )

            return self._focused_id

        index = self._order.index(
            self._focused_id
        )

        index = (
            index - 1
        ) % len(self._order)

        self._focused_id = (
            self._order[index]
        )

        return self._focused_id


ui_focus_manager = UIFocusManager()
