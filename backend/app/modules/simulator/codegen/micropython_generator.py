from app.modules.simulator.codegen.base_generator import (
    BaseGenerator,
)


class MicroPythonGenerator(BaseGenerator):

    LANGUAGE = "MicroPython"

    def header(self):

        return """# UAP OS
from machine import Pin
import time

"""

    def footer(self):
        return ""

    def generate_node(self, node):

        block = node.block_type.lower()

        cfg = node.config

        if block == "start":
            return "# Start"

        if block == "delay":

            ms = cfg.get(
                "milliseconds",
                1000,
            )

            return f"time.sleep_ms({ms})"

        if block == "digital_write":

            pin = cfg.get("pin", 0)

            value = cfg.get("value", 1)

            return (
                f"Pin({pin}, Pin.OUT).value({value})"
            )

        if block == "digital_read":

            pin = cfg.get("pin", 0)

            return (
                f"Pin({pin}, Pin.IN).value()"
            )

        if block == "analog_write":

            return "# PWM"

        if block == "analog_read":

            return "# ADC"

        return f"# {node.name}"
