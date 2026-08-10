from enum import Enum


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
