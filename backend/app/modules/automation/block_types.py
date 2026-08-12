class BlockTypes:

    START = "start"

    MOVE = "move"

    POSITION = "position"

    WAIT = "wait"

    OUTPUT = "output"

    INPUT = "input"

    CONDITION = "condition"

    LOOP = "loop"

    END = "end"

    @classmethod
    def all(cls):

        return [
            cls.START,
            cls.MOVE,
            cls.POSITION,
            cls.WAIT,
            cls.OUTPUT,
            cls.INPUT,
            cls.CONDITION,
            cls.LOOP,
            cls.END,
        ]from enum import Enum


class BlockType(Enum):

    INPUT = "input"

    OUTPUT = "output"

    SENSOR = "sensor"

    ACTUATOR = "actuator"

    MOTOR = "motor"

    RELAY = "relay"

    VALVE = "valve"

    TIMER = "timer"

    CONDITION = "condition"

    COMPARISON = "comparison"

    COUNTER = "counter"

    LOOP = "loop"

    EVENT = "event"

    VARIABLE = "variable"

    STOCK = "stock"

    MEASUREMENT = "measurement"

    VISION = "vision"

    ROBOT = "robot"

    MOTION = "motion"

    AI = "ai"
