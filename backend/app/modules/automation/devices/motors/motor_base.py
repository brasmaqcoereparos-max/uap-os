from app.modules.automation.device import Device


class MotorBase(Device):

    def __init__(

        self,

        device_id,

        name,

    ):

        super().__init__(

            device_id,

            name,

        )

        self.speed = 0

        self.target_speed = 0

        self.acceleration = 100

        self.deceleration = 100

        self.direction = 1

        self.running = False

    def start(self):

        self.running = True

    def stop(self):

        self.running = False

    def set_speed(

        self,

        speed,

    ):

        self.target_speed = speed

    def set_direction(

        self,

        direction,

    ):

        self.direction = direction

    def set_acceleration(

        self,

        value,

    ):

        self.acceleration = value

    def set_deceleration(

        self,

        value,

    ):

        self.deceleration = value
