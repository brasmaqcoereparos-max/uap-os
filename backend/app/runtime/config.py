import os


class RuntimeConfig:

    ENGINE_CYCLE_TIME = float(
        os.getenv("ENGINE_CYCLE_TIME", "0.1")
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )

    MQTT_HOST = os.getenv(
        "MQTT_HOST",
        "localhost",
    )

    MQTT_PORT = int(
        os.getenv(
            "MQTT_PORT",
            "1883",
        )
    )

    MODBUS_PORT = int(
        os.getenv(
            "MODBUS_PORT",
            "502",
        )
    )

    SERIAL_BAUDRATE = int(
        os.getenv(
            "SERIAL_BAUDRATE",
            "115200",
        )
    )

    AUTO_RECONNECT = os.getenv(
        "AUTO_RECONNECT",
        "true",
    ).lower() == "true"


runtime_config = RuntimeConfig()
