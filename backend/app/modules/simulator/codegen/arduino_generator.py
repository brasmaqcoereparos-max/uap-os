from app.modules.simulator.codegen.base_generator import (
    BaseGenerator,
)


class ArduinoGenerator(BaseGenerator):

    LANGUAGE = "Arduino"

    def header(self):

        return """void setup() {

}

void loop() {
"""

    def footer(self):

        return """
}
"""

    def generate_node(self, node):

        block = node.block_type.lower()

        cfg = node.config

        if block == "start":
            return "  // Start"

        if block == "delay":

            ms = cfg.get(
                "milliseconds",
                1000,
            )

            return f"  delay({ms});"

        if block == "digital_write":

            pin = cfg.get(
                "pin",
                0,
            )

            value = cfg.get(
                "value",
                1,
            )

            state = "HIGH" if value else "LOW"

            return (
                f"  digitalWrite({pin}, {state});"
            )

        if block == "digital_read":

            pin = cfg.get(
                "pin",
                0,
            )

            return (
                f"  digitalRead({pin});"
            )

        if block == "analog_write":

            pin = cfg.get(
                "pin",
                0,
            )

            value = cfg.get(
                "value",
                0,
            )

            return (
                f"  analogWrite({pin}, {value});"
            )

        if block == "analog_read":

            pin = cfg.get(
                "pin",
                0,
            )

            return (
                f"  analogRead({pin});"
            )

        if block == "if":

            variable = cfg.get(
                "variable",
                "value",
            )

            value = cfg.get(
                "value",
                1,
            )

            return (
                f"  if ({variable} == {value}) {{\n"
                f"  }}"
            )

        if block == "loop":

            count = cfg.get(
                "count",
                10,
            )

            return (
                f"  for(int i=0;i<{count};i++) {{\n"
                f"  }}"
            )

        return f"  // {node.name}"
