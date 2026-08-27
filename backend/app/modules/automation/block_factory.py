from app.modules.automation.block import (
    AutomationBlock,
)

from app.modules.automation.block_library import (
    block_library,
)


class BlockFactory:
    def create(
        self,
        block_type,
        name=None,
        parameters=None,
        metadata=None,
    ):
        template = (
            block_library.get(
                block_type
            )
        )

        if template is None:
            return None

        block = template.clone(
            new_id=True
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

        if metadata:
            block.metadata.update(
                dict(metadata)
            )

        return block

    def create_custom(
        self,
        block_type,
        name,
        description="",
        category="basic",
        icon="",
        color="",
        inputs=None,
        outputs=None,
        parameters=None,
    ):
        block = AutomationBlock(
            block_type=block_type,
            name=name,
            description=description,
            category=category,
            icon=icon,
            color=color,
        )

        for port in (
            inputs or []
        ):
            if isinstance(
                port,
                dict,
            ):
                block.add_input(
                    name=port.get(
                        "name",
                        "input",
                    ),
                    port_type=port.get(
                        "type",
                        "generic",
                    ),
                    required=port.get(
                        "required",
                        False,
                    ),
                    multiple=port.get(
                        "multiple",
                        False,
                    ),
                    description=port.get(
                        "description",
                        "",
                    ),
                    icon=port.get(
                        "icon",
                        "",
                    ),
                )

            else:
                block.add_input(
                    port
                )

        for port in (
            outputs or []
        ):
            if isinstance(
                port,
                dict,
            ):
                block.add_output(
                    name=port.get(
                        "name",
                        "output",
                    ),
                    port_type=port.get(
                        "type",
                        "generic",
                    ),
                    multiple=port.get(
                        "multiple",
                        True,
                    ),
                    description=port.get(
                        "description",
                        "",
                    ),
                    icon=port.get(
                        "icon",
                        "",
                    ),
                )

            else:
                block.add_output(
                    port
                )

        for key, value in (
            parameters or {}
        ).items():

            if (
                isinstance(
                    value,
                    dict,
                )
                and "type" in value
            ):
                block.add_parameter(
                    parameter=key,
                    parameter_type=(
                        value.get(
                            "type",
                            "text",
                        )
                    ),
                    default=value.get(
                        "default"
                    ),
                    description=value.get(
                        "description",
                        "",
                    ),
                    required=value.get(
                        "required",
                        False,
                    ),
                    options=value.get(
                        "options"
                    ),
                    minimum=value.get(
                        "minimum"
                    ),
                    maximum=value.get(
                        "maximum"
                    ),
                    unit=value.get(
                        "unit"
                    ),
                    visible=value.get(
                        "visible",
                        True,
                    ),
                    advanced=value.get(
                        "advanced",
                        False,
                    ),
                )

            else:
                block.set_parameter(
                    key,
                    value,
                )

        return block


block_factory = BlockFactory()
