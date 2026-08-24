import os


def _float_env(name, default):
    try:
        value = float(
            os.getenv(name, default)
        )
        return max(0.001, value)
    except (
        TypeError,
        ValueError,
    ):
        return float(default)


def _int_env(name, default):
    try:
        return int(
            os.getenv(name, default)
        )
    except (
        TypeError,
        ValueError,
    ):
        return int(default)


def _bool_env(name, default=True):

    value = os.getenv(
        name,
        "true" if default else "false",
    )

    return str(value).strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


class RuntimeConfig:

    ENGINE_CYCLE_TIME = _float_env(
        "ENGINE_CYCLE_TIME",
        "0.1",
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO",
    ).upper()

    MQTT_HOST = os.getenv(
        "MQTT_HOST",
        "localhost",
    )

    MQTT_PORT = _int_env(
        "MQTT_PORT",
        "1883",
    )

    MODBUS_PORT = _int_env(
        "MODBUS_PORT",
        "502",
    )

    SERIAL_BAUDRATE = _int_env(
        "SERIAL_BAUDRATE",
        "115200",
    )

    AUTO_RECONNECT = _bool_env(
        "AUTO_RECONNECT",
        True,
    )


runtime_config = RuntimeConfig()
