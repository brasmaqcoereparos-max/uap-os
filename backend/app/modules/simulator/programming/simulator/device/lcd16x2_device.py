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
        super().__init__(
            name=name,
            category="display",
            description="Display LCD 16x2",
            icon="display",
        )

        self.columns = 16
        self.rows = 2

        self.lines = [
            "",
            "",
        ]

        self.cursor_row = 0
        self.cursor_column = 0

        self.backlight = True

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

        return (
            self.cursor_row,
            self.cursor_column,
        )

    def write(
        self,
        text,
    ):
        if not self.enabled:
            return False

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

        self.lines[row] = (
            current[:self.columns]
        )

        self.cursor_column = column

        return self.lines[row]

    def write_line(
        self,
        row,
        text,
    ):
        self.set_cursor(
            row,
            0,
        )

        self.lines[
            self.cursor_row
        ] = ""

        return self.write(text)

    def clear(self):
        self.lines = [
            "",
            "",
        ]

        self.set_cursor(
            0,
            0,
        )

        return True

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

    def get_lines(self):
        return list(self.lines)

    def set_backlight(
        self,
        enabled,
    ):
        self.backlight = bool(
            enabled
        )

        return self.backlight

    def update(self):
        return self.get_lines()

    def reset(self):
        self.clear()
        self.backlight = True

        return True

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "columns": self.columns,
            "rows": self.rows,
            "lines": list(
                self.lines
            ),
            "cursor_row": (
                self.cursor_row
            ),
            "cursor_column": (
                self.cursor_column
            ),
            "backlight": (
                self.backlight
            ),
        })

        return data
