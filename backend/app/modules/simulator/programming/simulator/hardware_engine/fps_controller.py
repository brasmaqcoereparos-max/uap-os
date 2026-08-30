"""
Controle de frequência do motor de simulação UAP.
"""


class FPSController:

    DEFAULT_FPS = 60
    MIN_FPS = 1
    MAX_FPS = 1000

    def __init__(
        self,
        fps=60,
    ):
        self.fps = (
            self.DEFAULT_FPS
        )

        self.set_fps(
            fps
        )

    def set_fps(
        self,
        fps,
    ):
        fps = int(fps)

        fps = max(
            self.MIN_FPS,
            fps,
        )

        fps = min(
            self.MAX_FPS,
            fps,
        )

        self.fps = fps

        return self.fps

    def get_fps(self):
        return self.fps

    def interval(self):
        return (
            1.0
            / self.fps
        )

    def interval_ms(self):
        return (
            self.interval()
            * 1000.0
        )

    def set_interval(
        self,
        seconds,
    ):
        seconds = float(
            seconds
        )

        if seconds <= 0:
            raise ValueError(
                "Intervalo precisa ser "
                "maior que zero."
            )

        return self.set_fps(
            round(
                1.0 / seconds
            )
        )

    def to_dict(self):
        return {
            "fps": self.fps,
            "interval": (
                self.interval()
            ),
            "interval_ms": (
                self.interval_ms()
            ),
            }
