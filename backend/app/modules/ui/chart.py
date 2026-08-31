from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.data_series import (
    UIDataSeries,
)


@dataclass
class UIChart:
    id: str
    name: str

    chart_type: str = "line"

    title: str = ""

    series: list[
        UIDataSeries
    ] = field(
        default_factory=list
    )

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_series(
        self,
        series: UIDataSeries,
    ):
        if self.get_series(series.id):
            raise ValueError(
                "Series already exists: "
                f"{series.id}"
            )

        self.series.append(series)

        return series

    def get_series(
        self,
        series_id: str,
    ):
        for series in self.series:
            if series.id == series_id:
                return series

        return None

    def remove_series(
        self,
        series_id: str,
    ):
        series = self.get_series(
            series_id
        )

        if not series:
            return False

        self.series.remove(series)

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "chart_type": (
                self.chart_type
            ),
            "title": self.title,
            "series": [
                series.to_dict()
                for series in self.series
            ],
            "properties": dict(
                self.properties
            ),
        }
