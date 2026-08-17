from app.modules.automation.map_cell import (
    MapCell,
)


class RobotMap:

    def __init__(self):

        self.cells = {}

    def set_cell(
        self,
        x,
        y,
        state,
    ):

        key = (
            x,
            y,
        )

        cell = self.cells.get(key)

        if cell is None:

            cell = MapCell(
                x,
                y,
            )

            self.cells[key] = cell

        cell.set_state(state)

    def get_cell(
        self,
        x,
        y,
    ):

        return self.cells.get(
            (
                x,
                y,
            )
        )

    def get_all(self):

        return list(
            self.cells.values()
        )

    def clear(self):

        self.cells.clear()
