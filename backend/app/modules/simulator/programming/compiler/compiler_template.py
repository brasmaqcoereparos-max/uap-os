class CompilerTemplate:

    def render(

        self,

        text,

        values,

    ):

        for key, value in values.items():

            text = text.replace(

                "{{" + key + "}}",

                str(value),

            )

        return text


compiler_template = CompilerTemplate()
