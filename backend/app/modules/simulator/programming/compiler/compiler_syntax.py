class CompilerSyntax:

    def validate(

        self,

        nodes,

    ):

        errors = []

        for node in nodes:

            if "id" not in node:

                errors.append(

                    "Node without id."

                )

            if "block_type" not in node:

                errors.append(

                    f"Node {node.get('name')} without block_type."

                )

        return errors


compiler_syntax = CompilerSyntax()
