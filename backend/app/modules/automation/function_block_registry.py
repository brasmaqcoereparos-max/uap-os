class FunctionBlockRegistry:

    def __init__(self):
        self.blocks = {}

    def register(
        self,
        block_type,
        factory,
        replace=True,
    ):
        key = str(
            block_type
        )

        if (
            key in self.blocks
            and not replace
        ):
            raise ValueError(
                f"Function Block "
                f"'{key}' já registrado."
            )

        if not callable(factory):
            raise TypeError(
                "Factory precisa "
                "ser executável."
            )

        self.blocks[key] = factory

        return factory

    def unregister(
        self,
        block_type,
    ):
        return self.blocks.pop(
            str(block_type),
            None,
        )

    def get(
        self,
        block_type,
    ):
        return self.blocks.get(
            str(block_type)
        )

    def exists(
        self,
        block_type,
    ):
        return str(
            block_type
        ) in self.blocks

    def create(
        self,
        block_type,
        *args,
        **kwargs,
    ):
        factory = self.get(
            block_type
        )

        if factory is None:
            return None

        return factory(
            *args,
            **kwargs,
        )

    def get_all(self):
        return dict(
            self.blocks
        )

    def list_types(self):
        return list(
            self.blocks.keys()
        )

    def count(self):
        return len(
            self.blocks
        )

    def clear(self):
        self.blocks.clear()


function_block_registry = (
    FunctionBlockRegistry()
)
