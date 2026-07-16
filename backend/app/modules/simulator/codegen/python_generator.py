from app.modules.simulator.codegen.base_generator import (
    BaseGenerator,
)


class PythonGenerator(BaseGenerator):

    LANGUAGE = "Python"

    def header(self):

        return """# UAP OS

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

            return (
                f"time.sleep({ms/1000})"
            )

        if block == "digital_write":

            return (
                f"print('Digital Write Pin {cfg.get('pin',0)} = {cfg.get('value',0)}')"
            )

        if block == "digital_read":

            return (
                f"print('Digital Read Pin {cfg.get('pin',0)}')"
            )

        if block == "analog_write":

            return (
                f"print('Analog Write Pin {cfg.get('pin',0)} = {cfg.get('value',0)}')"
            )

        if block == "analog_read":

            return (
                f"print('Analog Read Pin {cfg.get('pin',0)}')"
            )

        return f"print('{node.name}')"
