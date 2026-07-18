class CompilerValidator:

    def validate(self, canvas):

        errors = []

        nodes = canvas.all_nodes()

        if len(nodes) == 0:

            errors.append(

                "Canvas vazio."

            )

        return errors


compiler_validator = CompilerValidator()
