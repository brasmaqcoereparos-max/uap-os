from app.modules.motion.drivers.driver_base import MotionDriverBase


class DCMotorDriver(MotionDriverBase):

    def __init__(self):

        super().__init__()

        self.speed = 0

    def move(

        self,

        speed,

    ):

        self.speed = speed

    def stop(self):

        self.speed = 0
