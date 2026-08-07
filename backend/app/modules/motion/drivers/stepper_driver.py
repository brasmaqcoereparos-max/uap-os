from app.modules.motion.drivers.driver_base import MotionDriverBase


class StepperDriver(MotionDriverBase):

    def __init__(self):

        super().__init__()

        self.steps = 0

    def move(

        self,

        target,

    ):

        self.steps = target

    def stop(self):

        pass
