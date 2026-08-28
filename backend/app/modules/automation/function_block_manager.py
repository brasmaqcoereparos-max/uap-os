from app.modules.automation.function_block_factory import (
    function_block_factory,
)

from app.modules.automation.function_block_registry import (
    function_block_registry,
)


class FunctionBlockManager:
    def __init__(self):
        self.instances = {}

    def register_type(
        self,
        block_type,
        factory=None,
        replace=True,
    ):
        if factory is None:
            factory = (
                lambda *args,
                **kwargs: (
                    function_block_factory.create(
                        block_type,
                        *args,
                        **kwargs,
                    )
                )
            )

        return (
            function_block_registry.register(
                block_type,
                factory,
                replace=replace,
            )
        )

    def create(
        self,
        block_id,
        block_type,
        name=None,
        parameters=None,
        replace=False,
    ):
        block_id = str(
            block_id
        )

        if (
            block_id in self.instances
            and not replace
        ):
            raise ValueError(
                f"Bloco '{block_id}' "
                "já existe."
            )

        block = (
            function_block_factory.create(
                block_type=block_type,
                name=name,
                parameters=parameters,
            )
        )

        if hasattr(
            block,
            "block_id",
        ):
            block.block_id = block_id

        self.instances[
            block_id
        ] = block

        return block

    def get(
        self,
        block_id,
    ):
        return self.instances.get(
            str(block_id)
        )

    def exists(
        self,
        block_id,
    ):
        return (
            str(block_id)
            in self.instances
        )

    def remove(
        self,
        block_id,
    ):
        return (
            self.instances.pop(
                str(block_id),
                None,
            )
            is not None
        )

    def execute(
        self,
        block_id,
        context=None,
    ):
        block = self.get(
            block_id
        )

        if block is None:
            raise KeyError(
                f"Bloco não encontrado: "
                f"{block_id}"
            )

        execute = getattr(
            block,
            "execute",
            None,
        )

        if not callable(execute):
            raise TypeError(
                "Bloco não possui "
                "método execute()."
            )

        try:
            return execute(
                context or {}
            )
        except TypeError:
            return execute()

    def get_all(self):
        return dict(
            self.instances
        )

    def clear(self):
        self.instances.clear()

    def count(self):
        return len(
            self.instances
        )


function_block_manager = (
    FunctionBlockManager()
        )
