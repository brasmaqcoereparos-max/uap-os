"""
Controle de frequência do motor de simulação UAP.
"""


class FPSController:

    def __init__(
        self,
        fps=60,
    ):

        self.fps = max(
            1,
            int(fps),
        )

    def set_fps(
        self,
        fps,
    ):

        self.fps = max(
            1,
            int(fps),
        )

    def get_fps(self):

        return self.fps

    def interval(self):

        return 1.0 / self.fps
