from enum import Enum


class BlockCategory(
    str,
    Enum,
):
    BASIC = "basic"
    CONTROL = "control"

    INPUT = "input"
    OUTPUT = "output"

    LOGIC = "logic"
    TIME = "time"
    VARIABLES = "variables"

    MOTION = "motion"
    ROBOTICS = "robotics"

    SENSORS = "sensors"
    ACTUATORS = "actuators"

    HARDWARE = "hardware"
    ELECTRONICS = "electronics"

    INVENTORY = "inventory"

    VISION = "vision"

    COMMUNICATION = (
        "communication"
    )

    AI = "ai"
    SAFETY = "safety"

    SERVICES = "services"

    UI = "ui"

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
            value or "basic"
        ).strip().lower()

        for item in cls:
            if item.value == text:
                return item

        raise ValueError(
            "Categoria de bloco "
            f"inválida: {value}"
        )

    @classmethod
    def values(cls):
        return [
            item.value
            for item in cls
        ]
