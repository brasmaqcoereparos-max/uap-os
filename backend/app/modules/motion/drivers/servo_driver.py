from app.modules.motion.drivers.driver_base import MotionDriverBase


class ServoDriver(MotionDriverBase):

    def __init__(self):

        super().__init__()

        self.position = 0.0

    def move(

        self,

        target,

    ):

        self.position = target

    def stop(self):

        pass
