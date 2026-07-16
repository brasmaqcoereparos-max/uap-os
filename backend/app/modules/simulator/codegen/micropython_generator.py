from app.modules.simulator.codegen.base_generator import (
    BaseGenerator,
)


class MicroPythonGenerator(BaseGenerator):

    LANGUAGE = "MicroPython"

    def generate_node(self, node):

        return f"# {node.name}"
