class BoardValidator:

    REQUIRED_FIELDS = (

        "name",

        "manufacturer",

        "cpu",

        "frequency",

        "gpio_count",

    )

    def validate(

        self,

        board,

    ):

        for field in self.REQUIRED_FIELDS:

            if not hasattr(

                board,

                field,

            ):

                raise ValueError(

                    f"Campo obrigatório ausente: {field}"

                )

        return True


board_validator = BoardValidator()
