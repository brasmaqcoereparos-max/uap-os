class FPSController:

    def __init__(self):

        self.fps = 60

    @property
    def interval(self):

        return 1.0 / self.fps

    def set_fps(

        self,

        fps,

    ):

        self.fps = max(

            1,

            int(fps),

        )


fps_controller = FPSController()
