"""
Tipos oficiais de blocos visuais do UAP.
"""

from enum import Enum

from app.modules.automation.block_category import (
    BlockCategory,
)


class BlockType(
    str,
    Enum,
):
    START = "start"
    END = "end"

    INPUT = "input"
    OUTPUT = "output"

    DIGITAL_INPUT = (
        "digital_input"
    )

    DIGITAL_OUTPUT = (
        "digital_output"
    )

    ANALOG_INPUT = (
        "analog_input"
    )

    ANALOG_OUTPUT = (
        "analog_output"
    )

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
    STEPPER = "stepper"

    RELAY = "relay"

    HTTP = "http"
    MQTT = "mqtt"
    MODBUS = "modbus"

    FUNCTION = "function"
    SERVICE = "service"

    SAFETY = "safety"

    EMERGENCY_STOP = (
        "emergency_stop"
    )

    @classmethod
    def normalize(
        cls,
        value,
    ):
        if isinstance(
            value,
            cls,
        ):
            return value

        text = str(
            value
        ).strip().lower()

        for item in cls:
            if item.value == text:
                return item

        raise ValueError(
            "Tipo de bloco "
            f"inválido: {value}"
        )

    @classmethod
    def values(cls):
        return [
            item.value
            for item in cls
        ]


def is_valid_block_type(
    value: str,
) -> bool:
    try:
        BlockType.normalize(
            value
        )

        return True

    except (
        TypeError,
        ValueError,
    ):
        return False


__all__ = [
    "BlockType",
    "BlockCategory",
    "is_valid_block_type",
    ]
