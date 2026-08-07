from app.modules.motion.drivers.driver_base import MotionDriverBase


class EncoderDriver(MotionDriverBase):

    def __init__(self):

        super().__init__()

        self.position = 0

    def read(self):

        return self.position

    def reset(self):

        self.position = 0
