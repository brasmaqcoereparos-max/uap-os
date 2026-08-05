class PeripheralValidator:

    REQUIRED = (

        "name",

        "manufacturer",

        "category",

    )

    def validate(

        self,

        peripheral,

    ):

        for field in self.REQUIRED:

            if not hasattr(

                peripheral,

                field,

            ):

                raise ValueError(

                    f"Campo obrigatório ausente: {field}"

                )

        return True


peripheral_validator = PeripheralValidator()
