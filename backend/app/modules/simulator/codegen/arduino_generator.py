from app.modules.simulator.codegen.base_generator import (
    BaseGenerator,
)


class ArduinoGenerator(BaseGenerator):

    LANGUAGE = "Arduino"

    def header(self):

        return """void setup(){

}

void loop(){

"""

    def footer(self):

        return """
}
"""

    def generate_node(self, node):

        return f"  // {node.name}"
