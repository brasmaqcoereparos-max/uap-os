from app.modules.simulator.programming.compiler.compiler_token import (
    CompilerToken,
)


class CompilerTokenizer:

    def tokenize(

        self,

        text,

    ):

        tokens = []

        for line_number, line in enumerate(

            text.splitlines(),

            start=1,

        ):

            for value in line.split():

                tokens.append(

                    CompilerToken(

                        "WORD",

                        value,

                        line_number,

                    )

                )

        return tokens


compiler_tokenizer = CompilerTokenizer()
