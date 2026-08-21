"""
Tipos básicos de blocos visuais de automação.
"""

from enum import Enum


class BlockType(str, Enum):
    START = "start"
    END = "end"

    INPUT = "input"
    OUTPUT = "output"

    SENSOR = "sensor"
    ACTUATOR = "actuator"

    CONDITION = "condition"
    ACTION = "action"

    DELAY = "delay"
    TIMER = "timer"

    LOOP = "loop"
    VARIABLE = "variable"

    CAMERA = "camera"
    VISION = "vision"

    MOTOR = "motor"
    SERVO = "servo"

    HTTP = "http"
    MQTT = "mqtt"

    SAFETY = "safety"
    EMERGENCY_STOP = "emergency_stop"


class BlockCategory(str, Enum):
    CONTROL = "control"
    INPUT = "input"
    OUTPUT = "output"
    LOGIC = "logic"
    TIME = "time"
    COMMUNICATION = "communication"
    VISION = "vision"
    HARDWARE = "hardware"
    SAFETY = "safety"


def is_valid_block_type(
    value: str,
) -> bool:
    return value in {
        item.value
        for item in BlockType
    }
