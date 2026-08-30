"""
Representação visual de um fio no circuito UAP.
"""

import math
import uuid


class Wire:

    def __init__(
        self,
        start,
        end,
        wire_id=None,
        points=None,
        wire_type="signal",
        label="",
        metadata=None,
    ):
        self.wire_id = (
            str(wire_id)
            if wire_id is not None
            else str(uuid.uuid4())
        )

        self.id = self.wire_id

        self.start = start
        self.end = end

        self.points = list(
            points or []
        )

        self.wire_type = str(
            wire_type
        )

        self.label = str(label)

        self.enabled = True

        self.metadata = dict(
            metadata or {}
        )

    def set_start(
        self,
        start,
    ):
        self.start = start
        return start

    def set_end(
        self,
        end,
    ):
        self.end = end
        return end

    def add_point(
        self,
        x,
        y,
    ):
        point = (
            float(x),
            float(y),
        )

        self.points.append(
            point
        )

        return point

    def insert_point(
        self,
        index,
        x,
        y,
    ):
        point = (
            float(x),
            float(y),
        )

        self.points.insert(
            int(index),
            point,
        )

        return point

    def remove_point(
        self,
        index,
    ):
        index = int(index)

        if not (
            0
            <= index
            < len(self.points)
        ):
            return None

        return self.points.pop(
            index
        )

    def clear_points(self):
        self.points.clear()

    @staticmethod
    def _xy(value):
        if isinstance(
            value,
            (tuple, list),
        ):
            if len(value) >= 2:
                return (
                    float(value[0]),
                    float(value[1]),
                )

        if isinstance(value, dict):
            return (
                float(
                    value.get(
                        "x",
                        0,
                    )
                ),
                float(
                    value.get(
                        "y",
                        0,
                    )
                ),
            )

        return (
            float(
                getattr(
                    value,
                    "x",
                    0,
                )
            ),
            float(
                getattr(
                    value,
                    "y",
                    0,
                )
            ),
        )

    def path(self):
        return [
            self._xy(self.start),
            *[
                self._xy(point)
                for point
                in self.points
            ],
            self._xy(self.end),
        ]

    def length(self):
        path = self.path()

        total = 0.0

        for index in range(
            1,
            len(path),
        ):
            x1, y1 = path[
                index - 1
            ]

            x2, y2 = path[
                index
            ]

            total += math.hypot(
                x2 - x1,
                y2 - y1,
            )

        return total

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def to_dict(self):
        return {
            "id": self.wire_id,
            "start": (
                self._xy(
                    self.start
                )
            ),
            "end": (
                self._xy(
                    self.end
                )
            ),
            "points": [
                self._xy(point)
                for point
                in self.points
            ],
            "type": self.wire_type,
            "label": self.label,
            "enabled": (
                self.enabled
            ),
            "length": (
                self.length()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
