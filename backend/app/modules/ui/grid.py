from dataclasses import dataclass


@dataclass
class UIGrid:
    enabled: bool = True

    size: float = 10

    snap_enabled: bool = True

    def snap(
        self,
        value: float,
    ):
        if (
            not self.enabled
            or not self.snap_enabled
            or self.size <= 0
        ):
            return value

        return round(
            value / self.size
        ) * self.size

    def snap_point(
        self,
        x: float,
        y: float,
    ):
        return (
            self.snap(x),
            self.snap(y),
        )
