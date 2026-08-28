class FunctionBlockTypes:

    START = "start"
    END = "end"

    MOTOR = "motor"
    SERVO = "servo"
    STEPPER = "stepper"

    SENSOR = "sensor"

    RELAY = "relay"
    VALVE = "valve"
    SOLENOID = "solenoid"

    TIMER = "timer"
    COUNTER = "counter"

    CONDITION = "condition"

    ROBOT = "robot"

    INPUT = "input"
    OUTPUT = "output"

    DELAY = "delay"

    VARIABLE = "variable"

    FUNCTION = "function"

    CAMERA = "camera"

    HTTP = "http"
    MQTT = "mqtt"
    MODBUS = "modbus"

    SAFETY = "safety"

    @classmethod
    def all(cls):
        return [
            cls.START,
            cls.END,
            cls.MOTOR,
            cls.SERVO,
            cls.STEPPER,
            cls.SENSOR,
            cls.RELAY,
            cls.VALVE,
            cls.SOLENOID,
            cls.TIMER,
            cls.COUNTER,
            cls.CONDITION,
            cls.ROBOT,
            cls.INPUT,
            cls.OUTPUT,
            cls.DELAY,
            cls.VARIABLE,
            cls.FUNCTION,
            cls.CAMERA,
            cls.HTTP,
            cls.MQTT,
            cls.MODBUS,
            cls.SAFETY,
        ]

    @classmethod
    def exists(
        cls,
        block_type,
    ):
        return str(
            block_type
        ) in cls.all()
