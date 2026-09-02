class UITreeSelection:

    def __init__(self):
        self._selected: list[
            str
        ] = []

        self._anchor: (
            str | None
        ) = None

    @property
    def anchor(self):
        return self._anchor

    def select(
        self,
        node_id: str,
        additive: bool = False,
    ):
        if not additive:
            self._selected.clear()

        if node_id not in self._selected:
            self._selected.append(
                node_id
            )

        self._anchor = node_id

        return list(
            self._selected
        )

    def deselect(
        self,
        node_id: str,
    ):
        if node_id not in self._selected:
            return False

        self._selected.remove(
            node_id
        )

        if self._anchor == node_id:
            self._anchor = (
                self._selected[-1]
                if self._selected
                else None
            )

        return True

    def toggle(
        self,
        node_id: str,
    ):
        if node_id in self._selected:
            self.deselect(
                node_id
            )
        else:
            self.select(
                node_id,
                additive=True,
            )

        return list(
            self._selected
        )

    def selected(self):
        return list(
            self._selected
        )

    def contains(
        self,
        node_id: str,
    ):
        return (
            node_id
            in self._selected
        )

    def clear(self):
        self._selected.clear()
        self._anchor = None


ui_tree_selection = (
    UITreeSelection()
      )
