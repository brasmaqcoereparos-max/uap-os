from app.modules.automation.block import (
    AutomationBlock,
)


class BlockLibrary:
    def __init__(self):
        self.blocks = {}

    def register(
        self,
        block,
        replace=True,
    ):
        if not isinstance(
            block,
            AutomationBlock,
        ):
            raise TypeError(
                "Somente AutomationBlock "
                "pode ser registrado."
            )

        key = str(
            block.block_type
        )

        if (
            key in self.blocks
            and not replace
        ):
            raise ValueError(
                f"Bloco '{key}' "
                "já registrado."
            )

        self.blocks[key] = block

        return block

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

    def create(
        self,
        block_type,
    ):
        template = self.get(
            block_type
        )

        if template is None:
            return None

        return template.clone(
            new_id=True
        )

    def exists(
        self,
        block_type,
    ):
        return (
            str(block_type)
            in self.blocks
        )

    def list(
        self,
        category=None,
    ):
        blocks = list(
            self.blocks.values()
        )

        if category is None:
            return blocks

        expected = str(
            getattr(
                category,
                "value",
                category,
            )
        )

        return [
            block
            for block in blocks
            if (
                block.category.value
                == expected
            )
        ]

    def search(
        self,
        text,
    ):
        query = str(
            text
        ).strip().lower()

        if not query:
            return self.list()

        return [
            block
            for block
            in self.blocks.values()
            if (
                query
                in block.name.lower()
                or query
                in block.description.lower()
                or query
                in block.block_type.lower()
            )
        ]

    def categories(self):
        return sorted(
            {
                block.category.value
                for block
                in self.blocks.values()
            }
        )

    def count(self):
        return len(
            self.blocks
        )

    def clear(self):
        self.blocks.clear()

    def to_dict(self):
        return {
            block_type: (
                block.to_dict()
            )
            for block_type, block
            in self.blocks.items()
        }


block_library = BlockLibrary()
