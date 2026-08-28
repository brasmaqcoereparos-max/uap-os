from app.modules.automation.function_block import (
    FunctionBlock,
)

from app.modules.automation.function_block_library import (
    function_block_library,
)

from app.modules.automation.function_block_registry import (
    function_block_registry,
)


class FunctionBlockFactory:

    def create(
        self,
        block_type,
        name=None,
        parameters=None,
    ):
        block_type = str(
            block_type
        )

        custom_factory = (
            function_block_registry.get(
                block_type
            )
        )

        if custom_factory is not None:
            block = custom_factory()

        else:
            if not (
                function_block_library.contains(
                    block_type
                )
            ):
                raise ValueError(
                    "Tipo de Function Block "
                    f"desconhecido: "
                    f"{block_type}"
                )

            category = (
                function_block_library.category_of(
                    block_type
                )
                or "control"
            )

            block = FunctionBlock(
                block_type=block_type,
                name=name,
                category=category,
            )

        if name is not None:
            block.name = str(name)

        for key, value in (
            parameters or {}
        ).items():
            block.set_parameter(
                key,
                value,
            )

        return block

    def create_many(
        self,
        definitions,
    ):
        result = []

        for definition in (
            definitions or []
        ):
            if not isinstance(
                definition,
                dict,
            ):
                continue

            result.append(
                self.create(
                    block_type=(
                        definition.get(
                            "type"
                        )
                    ),
                    name=(
                        definition.get(
                            "name"
                        )
                    ),
                    parameters=(
                        definition.get(
                            "parameters",
                            {},
                        )
                    ),
                )
            )

        return result


function_block_factory = (
    FunctionBlockFactory()
            )
