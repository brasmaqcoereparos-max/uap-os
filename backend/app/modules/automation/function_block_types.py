class FunctionBlockTypes:

    MOTOR = "motor"

    SENSOR = "sensor"

    RELAY = "relay"

    TIMER = "timer"

    COUNTER = "counter"

    CONDITION = "condition"

    ROBOT = "robot"

    INPUT = "input"

    OUTPUT = "output"

    DELAY = "delay"

    @classmethod
    def all(cls):

        return [
            cls.MOTOR,
            cls.SENSOR,
            cls.RELAY,
            cls.TIMER,
            cls.COUNTER,
            cls.CONDITION,
            cls.ROBOT,
            cls.INPUT,
            cls.OUTPUT,
            cls.DELAY,
        ]
