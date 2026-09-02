class UITreeState:

    def __init__(self):
        self._expanded: set[
            str
        ] = set()

    def expand(
        self,
        node_id: str,
    ):
        self._expanded.add(
            node_id
        )

        return True

    def collapse(
        self,
        node_id: str,
    ):
        self._expanded.discard(
            node_id
        )

        return True

    def toggle(
        self,
        node_id: str,
    ):
        if node_id in self._expanded:
            self._expanded.remove(
                node_id
            )

            return False

        self._expanded.add(
            node_id
        )

        return True

    def is_expanded(
        self,
        node_id: str,
    ):
        return (
            node_id
            in self._expanded
        )

    def clear(self):
        self._expanded.clear()

    def snapshot(self):
        return sorted(
            self._expanded
        )


ui_tree_state = UITreeState()
