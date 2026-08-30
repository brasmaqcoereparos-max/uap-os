"""
Gerenciamento de seleção no circuito visual UAP.
"""


class SelectionManager:

    def __init__(self):
        self.selected = []

    def clear(self):
        previous = self.all()

        for component in previous:
            deselect = getattr(
                component,
                "deselect",
                None,
            )

            if callable(deselect):
                deselect()

            elif hasattr(
                component,
                "selected",
            ):
                component.selected = (
                    False
                )

        self.selected.clear()

        return previous

    def add(
        self,
        component,
    ):
        if component is None:
            return False

        if component not in (
            self.selected
        ):
            self.selected.append(
                component
            )

        select = getattr(
            component,
            "select",
            None,
        )

        if callable(select):
            select()

        elif hasattr(
            component,
            "selected",
        ):
            component.selected = True

        return component

    def remove(
        self,
        component,
    ):
        if component not in (
            self.selected
        ):
            return False

        self.selected.remove(
            component
        )

        deselect = getattr(
            component,
            "deselect",
            None,
        )

        if callable(deselect):
            deselect()

        elif hasattr(
            component,
            "selected",
        ):
            component.selected = (
                False
            )

        return True

    def toggle(
        self,
        component,
    ):
        if component in (
            self.selected
        ):
            self.remove(component)
            return False

        self.add(component)
        return True

    def contains(
        self,
        component,
    ):
        return (
            component
            in self.selected
        )

    def first(self):
        if not self.selected:
            return None

        return self.selected[0]

    def last(self):
        if not self.selected:
            return None

        return self.selected[-1]

    def all(self):
        return self.selected.copy()

    def count(self):
        return len(self.selected)

    def move_all(
        self,
        dx,
        dy,
    ):
        moved = 0

        for component in (
            self.selected
        ):
            mover = getattr(
                component,
                "move_by",
                None,
            )

            if callable(mover):
                mover(
                    dx,
                    dy,
                )

                moved += 1

        return moved


selection_manager = (
    SelectionManager()
    )
