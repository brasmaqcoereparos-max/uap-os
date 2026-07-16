from app.modules.simulator.codegen.base_generator import (
    BaseGenerator,
)


class PythonGenerator(BaseGenerator):

    LANGUAGE = "Python"

    def generate_node(self, node):

        return f"# {node.name}"
