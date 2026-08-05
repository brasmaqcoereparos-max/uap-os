class PIDController:

    def __init__(

        self,

        kp=1.0,

        ki=0.0,

        kd=0.0,

    ):

        self.kp = kp

        self.ki = ki

        self.kd = kd

        self.integral = 0

        self.last_error = 0

    def update(

        self,

        target,

        current,

    ):

        error = target - current

        self.integral += error

        derivative = error - self.last_error

        self.last_error = error

        return (

            self.kp * error

            + self.ki * self.integral

            + self.kd * derivative

        )
