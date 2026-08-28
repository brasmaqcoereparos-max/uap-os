from app.modules.automation.block import (
    AutomationBlock,
)

from app.modules.automation.block_library import (
    block_library,
)

from app.modules.automation.block_types import (
    BlockType,
)


DEFAULT_BLOCKS = [
    (
        BlockType.START.value,
        "Início",
        "control",
        "play",
    ),
    (
        BlockType.END.value,
        "Fim",
        "control",
        "stop",
    ),
    (
        BlockType.INPUT.value,
        "Entrada",
        "input",
        "input",
    ),
    (
        BlockType.OUTPUT.value,
        "Saída",
        "output",
        "output",
    ),
    (
        BlockType.DIGITAL_INPUT.value,
        "Entrada digital",
        "input",
        "toggle-on",
    ),
    (
        BlockType.DIGITAL_OUTPUT.value,
        "Saída digital",
        "output",
        "toggle-off",
    ),
    (
        BlockType.ANALOG_INPUT.value,
        "Entrada analógica",
        "input",
        "gauge",
    ),
    (
        BlockType.ANALOG_OUTPUT.value,
        "Saída analógica",
        "output",
        "sliders",
    ),
    (
        BlockType.SENSOR.value,
        "Sensor",
        "sensors",
        "sensor",
    ),
    (
        BlockType.ACTUATOR.value,
        "Atuador",
        "actuators",
        "bolt",
    ),
    (
        BlockType.MOTOR.value,
        "Motor",
        "motion",
        "motor",
    ),
    (
        BlockType.SERVO.value,
        "Servo",
        "motion",
        "servo",
    ),
    (
        BlockType.STEPPER.value,
        "Motor de passo",
        "motion",
        "stepper",
    ),
    (
        BlockType.RELAY.value,
        "Relé",
        "actuators",
        "relay",
    ),
    (
        BlockType.TIMER.value,
        "Temporizador",
        "time",
        "timer",
    ),
    (
        BlockType.DELAY.value,
        "Espera",
        "time",
        "clock",
    ),
    (
        BlockType.CONDITION.value,
        "Condição",
        "logic",
        "branch",
    ),
    (
        BlockType.LOOP.value,
        "Repetição",
        "control",
        "repeat",
    ),
    (
        BlockType.VARIABLE.value,
        "Variável",
        "variables",
        "variable",
    ),
    (
        BlockType.CAMERA.value,
        "Câmera",
        "vision",
        "camera",
    ),
    (
        BlockType.VISION.value,
        "Visão",
        "vision",
        "eye",
    ),
    (
        BlockType.HTTP.value,
        "HTTP",
        "communication",
        "network",
    ),
    (
        BlockType.MQTT.value,
        "MQTT",
        "communication",
        "message",
    ),
    (
        BlockType.MODBUS.value,
        "Modbus",
        "communication",
        "network",
    ),
    (
        BlockType.FUNCTION.value,
        "Função",
        "control",
        "function",
    ),
    (
        BlockType.SERVICE.value,
        "Serviço",
        "services",
        "service",
    ),
    (
        BlockType.SAFETY.value,
        "Segurança",
        "safety",
        "shield",
    ),
    (
        BlockType.EMERGENCY_STOP.value,
        "Parada de emergência",
        "safety",
        "emergency-stop",
    ),
]


def register_default_blocks(
    replace=True,
):
    registered = []

    for (
        block_type,
        name,
        category,
        icon,
    ) in DEFAULT_BLOCKS:

        if (
            block_library.exists(
                block_type
            )
            and not replace
        ):
            continue

        block = AutomationBlock(
            block_type=block_type,
            name=name,
            category=category,
            icon=icon,
        )

        block.add_input(
            "in",
            port_type="flow",
            required=False,
        )

        block.add_output(
            "out",
            port_type="flow",
        )

        block_library.register(
            block,
            replace=replace,
        )

        registered.append(
            block
        )

    return registered
