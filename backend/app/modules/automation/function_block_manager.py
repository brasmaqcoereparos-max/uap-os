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
    ):

        function_block_registry.register(
            block_type,
            function_block_factory.create,
        )

    def create(
        self,
        block_id,
        block_type,
        name=None,
    ):

        block = function_block_factory.create(
            block_type,
            name,
        )

        self.instances[
            block_id
        ] = block

        return block

    def get(
        self,
        block_id,
    ):

        return self.instances.get(
            block_id
        )

    def remove(
        self,
        block_id,
    ):

        if block_id not in self.instances:
            return False

        self.instances.pop(
            block_id
        )

        return True

    def get_all(self):

        return dict(
            self.instances
        )


function_block_manager = (
    FunctionBlockManager()
)
