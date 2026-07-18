class CompilerSemantic:

    def validate(

        self,

        nodes,

    ):

        errors = []

        names = set()

        for node in nodes:

            node_name = node.get("name")

            if node_name in names:

                errors.append(

                    f"Duplicate node: {node_name}"

                )

            names.add(node_name)

        return errors


compiler_semantic = CompilerSemantic()
