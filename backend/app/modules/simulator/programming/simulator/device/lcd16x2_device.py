"""
Display LCD 16x2 simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class LCD16x2Device(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.columns = 16
        self.rows = 2

        self.lines = [
            "",
            "",
        ]

        self.cursor_row = 0
        self.cursor_column = 0

    def set_cursor(
        self,
        row,
        column,
    ):

        self.cursor_row = max(
            0,
            min(
                self.rows - 1,
                int(row),
            ),
        )

        self.cursor_column = max(
            0,
            min(
                self.columns - 1,
                int(column),
            ),
        )

    def write(
        self,
        text,
    ):

        text = str(text)

        row = self.cursor_row
        column = self.cursor_column

        current = self.lines[row]

        if len(current) < self.columns:
            current = current.ljust(
                self.columns
            )

        for char in text:

            if column >= self.columns:
                break

            current = (
                current[:column]
                + char
                + current[column + 1:]
            )

            column += 1

        self.lines[row] = current

        self.cursor_column = column

    def clear(self):

        self.lines = [
            "",
            "",
        ]

        self.set_cursor(
            0,
            0,
        )

    def read_line(
        self,
        row,
    ):

        row = max(
            0,
            min(
                self.rows - 1,
                int(row),
            ),
        )

        return self.lines[row]

    def update(self):
        pass

    def reset(self):

        self.clear()
